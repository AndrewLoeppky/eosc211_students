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
    # maintains fidelity to matlab datestr() function for all values tested
    # this should be tested more thorougly (AL 08/08/21)
    the_date = datetime.date.fromordinal(int(mdate) - 366)
    the_time = datetime.timedelta(days=(mdate % 1.0))
    the_date = datetime.datetime(
        the_date.year,
        the_date.month,
        the_date.day,
    )
    
    return the_date + the_time
