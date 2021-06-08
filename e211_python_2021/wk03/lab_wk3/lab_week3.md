---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Lab Week 3

## EOSC 211

**Learning Objectives:**  
1. Take a real world problem in EOAS and think of it like a scientific programmer
2. Apply our knowledge of *Python* data types, indexing, slicing arrays
3. Use built in functions and imported packages
4. Generate a scientific figure with Matplotlib
5. Reverse-engineer someone else's code so make it work for you

+++

## Scientific Figure Checklist

* Title
* X and Y axis labels with units
* Legend (if needed to interpret data)
* Does the figure *make sense* just by looking at it? (does it need an outside explanation?)
* Does it *look good*?

+++

## Exercise 1: Visualize some oceanographic data from the web

get data from here https://oceancolor.gsfc.nasa.gov

link -> data -> level 3 browser -> drop down settings to "standard", "<any>", <any>", "monthly", "9km" -> right click -> save image as -> name it something sensible and save in working directory
    
mine is at `C:\Users\Owner\UBC_TLEF\eosc_211\e211_python_2021\wk03\lab_wk3\chlorophyl_march1999.png`
    

+++

Import the packages we need (explain what each one does)

```{code-cell} ipython3
# Import the necessary libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
```

import our data as a .png image

```{code-cell} ipython3
# load the image
chlordat_in = Image.open("chlorophyl_march1999.png")

# what type of data are we dealing with? use the built in function type()
type(chlordat_in)
```

png is a common image format, but we would like to do more than just look at the picture. Convert to numpy so we can do analyze our data and generate a proper *scientific figure* to present our results.

```{code-cell} ipython3
chlordat_arr = np.asarray(chlordat_in)

# now what is the data type?
type(chlordat_arr)
chlordat_arr.dtype
```

```{code-cell} ipython3
# cool, we made it into a numpy array. What are its dimensions?
np.shape(chlordat_arr)
```

What are the *values* stored in our array? chlorophyl concentrations from 0 - 20 mg/m3 are mapped to integers from 255 to 0. Discuss further as in the old lab

```{code-cell} ipython3
pcm = plt.imshow(chlordat_arr,origin='upper')
```

```{code-cell} ipython3
# lets try plotting our array as a pcolormesh (a common way to visualize 2D datasets or images)
pcm = plt.pcolormesh(chlordat_arr)
```

Okay, we seem to have the general features of our data, but something has gone awry converting from a 
png to an array. How can we fix this given what we know about *array slicing?*

```{code-cell} ipython3
chlordat_fixed = chlordat_arr[::-1,::]  # explain what this does, or get students to come up with this

# try plotting it again
pcm = plt.pcolormesh(chlordat_fixed)
```

Looking better, but the default colours hurt to look at and it's very hard to understand what this picture actually represents. We can look at the available *parameters* ( ways we can modify the figure) for a *pcolormesh* plot by doing

```{code-cell} ipython3
help(plt.pcolormesh)
```

```{code-cell} ipython3
pcm = plt.pcolormesh(chlordat_fixed, cmap='magma_r') # change the colormap with a keyword argument
plt.title("Chlorophyl Concentration March 1999"); # add a title to the figure
```

Here is a link to the [matplotlib documentation](https://matplotlib.org/stable/gallery/color/colormap_reference.html) where I got the `magma_r` colormap from (you can add `_r` to any color map to reverse it). 

Next: change the x and y labels to something something meaningful, like latitude and longitude.

```{code-cell} ipython3
help(plt.xticks)
```

```{code-cell} ipython3
# We'd like to label every 30 degrees and place them in the correct location on our image.
# Use our skills at creating, indexing and slicing numpy arrays to create "ticks" and "labels"

numlats = np.shape(chlordat_fixed)[0]  # how many latitude elements in the original image?
numlons = np.shape(chlordat_fixed)[1]  # how many longitude elements?

# create arrays to use as "ticks"
lat_ticks = np.linspace(0, numlats, 7) # what am i doing here?
lon_ticks = np.linspace(0, numlons, 7)

# create arrays to use as "labels"
lat_labels = np.linspace(-90, 90, 7)  # start, stop, number of elements
lon_labels = np.linspace(-180, 180, 7)


# plot it again with lat, lon ticks and labels
pcm = plt.pcolormesh(chlordat_fixed, cmap="magma_r")  # change the colormap with a keyword argument
plt.title("Chlorophyl Concentration March 1999")  # add a title to the figure
plt.xlabel("longitude (deg)")
plt.ylabel("latitude (deg)")
plt.xticks(lon_ticks, lon_labels)
plt.yticks(lat_ticks, lat_labels);
```

Add a colourbar so we can interpret our data, just like the one on the oceancolor website. 

```{code-cell} ipython3
pcm = plt.pcolormesh(chlordat_fixed, cmap="magma_r")
plt.title("Chlorophyl Concentration March 1999")  # add a title to the figure
plt.xlabel("longitude (deg)")
plt.ylabel("latitude (deg)")
plt.xticks(lon_ticks, lon_labels)
plt.yticks(lat_ticks, lat_labels)

# create the colorbar. ticks and labels are assigned much the same as with axis labels
cbar = plt.colorbar(pcm, ticks=np.linspace(250,0,6), label="Chlorophyl Concentration, OCI Algorithm (mg/m3)")
cbar.ax.set_yticklabels(np.linspace(0,20,6));
```

Go through our scientific figure checklist. This checks all the boxes. 9 lines of code to produce the plot. It might be a good idea to save this code somewhere to use as a reference for the next time you need to generate a scientific figure.

+++

## Exercise 2: Bathymetry

The old lab talks about processing unscaled vs scaled data, but we just did a ton of work to rescale our labels in question 1. Whats easy in matlab is hard in python and v.v?


Same idea as #1: get data, re-format it into something we can understand and parse with python, manipulate the data however we wish, then present the result in a concise, nicely formatted way.

This dataset is from old MATLAB code, which saves data using the `.mat` extension. A quick search shows that there is a python package called `loadmat` from the scipy library that will handle this file type

```{code-cell} ipython3
# import tools we need to process the new data type
from scipy.io import loadmat

help(loadmat)
```

```{code-cell} ipython3
# get data
bathyfile = loadmat("Bathyfile.mat")

# format data into something we can use
# loadmat outputs a dictionary of np arrays. This code extracts the dictionary values to variables
lon = bathyfile["bath"][0][0][0].flatten() # extract latitude array
lat = bathyfile["bath"][0][0][1].flatten() # extract longitude array
height = bathyfile["bath"][0][0][2]
height = height[::-1] # flip it over as with q1

# present data
pcm = plt.pcolormesh(height,cmap='BuGn')
plt.xticks(np.arange(len(lon))[::200], np.round(lon)[::200])
plt.yticks(np.arange(len(lat))[::50], np.round(lat)[::50]);
```

```{code-cell} ipython3

```

## Exercise 3:
