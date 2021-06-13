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

