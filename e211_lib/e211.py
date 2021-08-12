# %%
'''
e211 Function library

author: Andrew Loeppky
course: eosc 211 - computer methods for earth, ocean and atmospheric scientists
''';

# %%
from PIL import Image
import numpy as np
from scipy.io import loadmat
import datetime


# %%

# %%
def load_temps(my_data):
    """
    loads temperature timeseries from Sand Heads. 
    Output is a tuple (temp, time) of np arrays
    """
    matfile = loadmat(my_data)
    temp = matfile["temperature"].flatten()
    time = matfile["time"].flatten()
    return temp, time


# %%
def load_oceancolor(my_image):
    """
    takes in a png image and returns a scaled numpy array. Scaling is set for
    https://oceancolor.gsfc.nasa.gov chlorophyl concentration files
    """
    img_in = Image.open(my_image)
    img_np = np.asarray(img_in)
    # default img -- 255->0mg/m3, 0->20mg/m3
    img_scaled = -(img_np - 255) * (20 / 256) # this should acrualbe log scaled
    return img_scaled


# %%
def load_mat(my_data):
    """
    designed to load the bathymetry data for lab week 3
    """
    # get data
    matfile = loadmat(my_data)

    # format data into something we can use
    # loadmat outputs a dictionary of np arrays. This code extracts the dictionary values to variables
    lon = matfile["bath"][0][0][0].flatten() # extract latitude array
    lat = matfile["bath"][0][0][1].flatten() # extract longitude array
    bath = matfile["bath"][0][0][2]
    return bath

# %%
def load_topo(my_data):
    """
    designed to load digital elevation model for lab wk5
    """
    matfile = loadmat(my_data)
    return matfile["topo"]


# %%
def load_aircraft(my_data):
    """
    designed to load aircraft gps path for lab wk6

    current state just returns the velocity array
    """
    matfile = loadmat(my_data)["gps"]
    vel = matfile["vel"][0][0][0]
    time = matfile["mtime"][0][0][0]  # current format = unix epoch + <days>

    return vel, time


# %%
def mdate_to_datetime(mdate):
    """
    converts matlab dates to python datetime objects

    matlab's date convention is days since Jan 1/0AD,
    years and days are 1-indexed (ie jan = 1 not 0)
    """
    # account for matlab's 1 indexed values by subtracting 1 year + 1 day
    # maintains fidelity to matlab datestr() function for ~20 values tested
    # this should be tested more thorougly (AL 08/08/21)
    the_date = datetime.date.fromordinal(int(mdate) - 366)
    the_time = datetime.timedelta(days=(mdate % 1.0))
    the_date = datetime.datetime(
        the_date.year,
        the_date.month,
        the_date.day,
    )
    
    return the_date + the_time


# %%
def clean_a1_data(dataset, save=False):
    """
    imports drifter dataset in .mat form, restructures into an array full of dictionaries
    each representing one drifter. See A1 for dictionary legend.

    save=True will save the output as a .npy file in the local directory as well as return
    the formatted array.
    """

    # import the whole dataset
    matdata = loadmat(dataset)
    matdata = matdata["D"].flatten()

    ##################################################################################
    # modify each element one by one, they all have slightly different shapes/dtypes #
    ##################################################################################

    drifter_id = np.concatenate(matdata["id"]).flatten()  # drifter ID

    design = np.concatenate(matdata["design"]).flatten()  # 1-6 which type of drifter

    tzone = np.concatenate(matdata["tzone"]).flatten()  # time zone

    mtime = matdata["mtime"]  # time in matlab ordinal (decimal days since jan1/0000)
    # create a new array datetime to replace messy mtime
    datetime = np.empty_like(mtime, dtype="O")
    for m in range(len(mtime)):
        timestamp = np.empty(len(mtime[m]), dtype="O")
        for n in range(len(mtime[m].flatten())):
            timestamp[n] = mdate_to_datetime(mtime[m][n, 0])
        datetime[m] = timestamp

    lon_in = matdata["lon"]  # drifter lons
    # create new variable lons containing restructured longitudes
    lons = np.empty_like(lon_in, dtype="O")
    for m in range(len(lon_in)):
        lon = np.empty(len(lon_in[m]))
        for n in range(len(lon_in[m])):
            lon[n] = lon_in[m][n]
        lons[m] = lon

    lat_in = matdata["lat"]  # drifter lats
    # same treatment for lats
    lats = np.empty_like(lat_in, dtype="O")
    for m in range(len(lat_in)):
        lat = np.empty(len(lat_in[m]))
        for n in range(len(lat_in[m])):
            lat[n] = lat_in[m][n]
        lats[m] = lat

    comment = np.concatenate(matdata["comment"]).flatten()  # metadata

    at_sea_in = matdata["atSea"]  # status codes for working/landed drifters

    # at_sea treatment echoes lats and lons
    at_sea = np.empty_like(at_sea_in, dtype="O")
    for m in range(len(at_sea_in)):
        sea = np.empty(len(at_sea_in[m]))
        for n in range(len(at_sea_in[m])):
            sea[n] = at_sea_in[m][n]
        at_sea[m] = sea

    ends_on_land = matdata[
        "endsOnLand"
    ].flatten()  # change from 1/0 logic to Python booleans
    ends_on_land[ends_on_land == 1] = True
    ends_on_land[ends_on_land == 0] = False

    found_on_land = matdata["foundOnLand"].flatten()  # use booleans not 1/0
    found_on_land[found_on_land == 1] = True
    found_on_land[found_on_land == 0] = False

    # convert data containing dates to datetime objs
    launchdate_in = np.concatenate(matdata["launchDate"]).flatten()
    launchdate = np.empty(len(launchdate_in), dtype="O")
    for i, ld in enumerate(launchdate_in):
        launchdate[i] = mdate_to_datetime(ld)

    enddate_in = np.concatenate(matdata["endDate"]).flatten()
    enddate = np.empty(len(enddate_in), dtype="O")
    for i, ed in enumerate(enddate_in):
        enddate[i] = mdate_to_datetime(ed)

    lifetime_in = np.concatenate(
        matdata["lifeTime"]
    ).flatten()  # decimal days from launchDate to endDate
    lifetime = (
        enddate - launchdate
    )  # ignore the original data and do datetime arithmetic. Get students to do this?

    refloated = matdata["refloated"]  # change to py logical
    refloated[refloated == 1] == True
    refloated[refloated == 0] == False

    first_ground_date_in = matdata["firstGrndDate"]
    first_ground_date = np.empty(len(first_ground_date_in), dtype="O")
    for i, fgd in enumerate(first_ground_date_in):
        if fgd == 0:
            first_ground_date[i] = enddate[i]
        else:
            first_ground_date[i] = mdate_to_datetime(fgd[0, 0])

            # - float: matlab time for first grounding
            # - matlab time of first of a string of atSea~=1, unless
            # the last point in the record has atSea==1 and
            # endsOnLand==1 in which case it is the time of the last
            # point.

    first_lifetime_in = matdata["firstLifeTime"]
    first_lifetime = first_ground_date - launchdate  # make students do this?

    # new datastructure: Each drifter is a dictionary with all vars above as keys, values are either arrays or numbers
    # save an array containing all the drifter "objects" (actually dictionaries...) array full of dictionaries full
    # of arrays!
    master_dataset = np.empty(len(drifter_id), dtype="O")
    for i, data in enumerate(master_dataset):
        master_dataset[i] = {
            "drifter_id": drifter_id[i],
            "design": design[i],
            "tzone": tzone[i],
            "datetime": datetime[i],
            "lons": lons[i],
            "lats": lats[i],
            "comment": comment[i],
            "at_sea": at_sea[i],
            "ends_on_land": ends_on_land[i],
            "found_on_land": found_on_land[i],
            "launchdate": launchdate[i],
            "enddate": enddate[i],
            "lifetime": lifetime[i],
            "refloated": refloated[i],
            "first_ground_date": first_ground_date[i],
            "first_lifetime": first_lifetime[i],
        }

    # save the dataset in local directory as a .npy file
    if save == True:
        np.save("drifter_data.npy", master_dataset)

    return master_dataset
