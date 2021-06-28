# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent,md
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Lab Week 5
#
# ## EOSC 211
#
# ### Learning Objectives:
#
# 1. Define variables using user input data
#
# 2. Use formatted text with f string literals to label plots
#
# 3. Change variable datatypes using *type casting*
#
# 3. Apply conditional statements `if elif else`
#
# second pass: the flow goes like
# 1) andrew imports the data and uses plt.annotation to label a user specified lat/lon/height on the map
#
# 2) student implements the slope equation to calculate variables "slope" and conditionals to figure out a variable "aspect"
#
# 3) talk about handling edge cases, arr[-1] and more conditionals to avoid "falling off the edge of the map"
#
# 4) final product: one code cell that, when run, takes in a user-specified lat/lon pair and outputs a scientific figure with the point labelled lat/lon/height/slope/aspect
#
#
#
# **Skills needed**
#
# - implement equations in code
# - knowledge of strings (f string literals, escape sequences \n)
# - use stackoverflow etc to figure out how to implement functions (deg2rad, np.where, a few others)
# - type casting
#

# %% [markdown]
# ## Part 1: The plt.annotate() Function and Formatted Text (Tutorial)
#
# preamble

# %%
from e211_lib import e211 
from matplotlib import pyplot as plt
import numpy as np

# %%
# get the data and query the size of the array
topo = e211.load_topo("lab5_topo.mat")
topo.shape # rows, columns

# %%
# create lat and lon arrays just like week 3 lab
lats = np.linspace(-89.5, 89.5, topo.shape[0])
lons = np.linspace(0.5, 359.5, topo.shape[1])

# see if our labels correctly match the plot
plt.contourf(lons, lats, topo)

# %% [markdown]
# Does everything look alright with our preliminary data visualization? We would like to reference points on our map by their latitude/longitude coordinates, which we can do with the [np.where()](https://numpy.org/doc/stable/reference/generated/numpy.where.html) function. For a given point on the map, we need to make sure to properly differentiate between the lat/lon coordinates of a location, the *array value* (i.e height above sea level), the *array index* that references that point in the array. `np.where()` returns the index of the array where the specified condition is `True`. For example, if we want to know the index of our `lats` array where the latitude is 30.5$^o$ N, we would do:

# %%
np.where(lats == 30.5)

# %% [markdown]
# The 120th value in the `lats` array is 30.5 degrees. Notice the datatype of the ouptut. Now, if we want to find the *value* of `topo` at the point 30.5$^o$ N, 100.5$^o$ E, we do:

# %%
topo[np.where(lats == 30.5), np.where(lons == 100.5)]  # row, column indexing

# %% [markdown]
# At 30.5$^o$ N, 100.5$^o$ E, the elevation os 4014m above sea level. Now, it would be nice to be able to display on the map where this point is and label the elevation. Better yet, what if we could prompt a user to select any lat/lon point, mark it with an X on the map, and label the point with the elevation? 
#
# Check out the docs for the functions [input](https://www.w3schools.com/python/ref_func_input.asp) and [plt.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html) to understand what is happening in the following cell. Later, you will modify this code to calculate and display the slope and aspect of a user-specified location on the map. 

# %%
# take in a lat/lon point as input and re-cast to datatype float
usrlat =  30.5 #float(input("lat: "))
usrlon =  100.5 #float(input("lon: "))

# assign new variables for the indexes of user specified lat lon
ilat = np.where(lats == usrlat)
ilon = np.where(lons == usrlon)

# make the (basic) plot
img = plt.contourf(lons, lats, topo)

# use the "annotate" function to label the chosen point on the plot
plt.annotate("X", (usrlon, usrlat), color="red")
the_label = f"lat: {usrlat} deg\nlon: {usrlon} deg\nheight: {topo[ilat, ilon]}m"
plt.annotate(the_label, (usrlon + 10, usrlat));

# %% [markdown]
# ## Part 2:  Calculate the Topography Slope
#
# Your task is to solve the following problem: What is the east/west slope (in degrees) at the point you specify at the input? The east/west slope is a height difference between the point immediately to the RIGHT (or EAST) of the one you picked and the one immediately to the LEFT (or WEST) of it,  divided by the horizontal distance of these two points (think $slope = \frac{rise}{run}$). Then take the arc-tangent to get the result in degrees:
#
# $$
# Slope \approx tan^{-1}\left(\frac{topo(i, j+1) - topo(i, j-1)}{\Delta LON \times 111e3 \times cos(LAT)}\right)
# $$
#
#
#
# | Symbol  | Variable      |  Units   |
# |:--|:----------------------------------|:------------|
# | $topo$     | topography array      | $height$ ($m$) |
# | $i,j$  | lat, lon indices      | --  |
# | $\Delta LON$  | change in longitude between two points      | $degrees$  |
# | $111e3$  | at the equator, 1 degree=111000m      | $m/deg$  |
# | $LAT$  | latitude of the point selected      | $degrees$  |
# | $cos(LAT)$  | a correction factor to take into account longitude convergence at the poles     | --  |
#
# ### 2a
# In the cell below, write code to make this work for points well within the array (i.e. away from the edges of the map). Make sure the trigonometric functions you use are for degrees and not radians. You may find the functions `np.deg2rad()` and `np.rad2deg()` helpful. 

# %%
# your code here

# %%
# andrew's soln

# np.where returns a tuple containing an array as the index, which you can't add 1 to. This question is tricky,
# you need to index the np.where() tuple to get the answer, even though we passed it an array earlier and it 
# worked just fine
slope = np.rad2deg(np.arctan((topo[ilat, ilon[0][0] + 1] 
                              - topo[ilat, ilon[0][0] - 1]) 
                              / (2 * 111e3 
                              * np.cos(np.deg2rad(usrlat)))))
slope

# %% [markdown]
# ### 2b
#
# Use `if` `elif` `else` blocks to print the following message to the screen:
#
# (i)  The latitude and longitude of the selected point (note - latitudes can be N or S, longitudes can always be E)
#
# (ii)  The elevation AND the slope at that point (in degrees)
#
# (iii)  A  message  saying  “Flat”  if  the  slope  angle  is  between  -0.1  and  +0.1  degrees,  “East-facing,” or “West-facing” if the slope is larger and either east - or west-facing, respectively. An “east-facing” slope tilts DOWN towards the east. Use *f string literals* to compose the message in a nicely formatted way, something like:
#
#        At 30.5 N, 100.5 E, Height is 4014 m and the slope is -0.186 degrees. This is East-facing.
#        
# In part 3, you will create a scientific figure with the slope and aspect annotated on the plot. For now, print the message to the screen

# %%
# your code here

# %%
# andrew's soln

# formatting for latitude
if int(usrlat) < 0:
    latdir = "S"
else:
    latdir = "N"

# formatting for slope direction
if slope > 0.1:
    slopedir = "west-facing"
elif slope < -0.1:
    slopedir = "east-facing"
else:
    slopedir = "flat"

# make a formatted string
out_msg = f"At {usrlat} {latdir}, {usrlon} E, the height is \
{topo[ilat, ilon][0,0]} m and the slope is {np.round(slope,3)[0,0]} degrees. This is {slopedir}."

print(out_msg)

# %% [markdown]
# ##  Part 3: Selections - Check Arguments
#
#
# Often with user input, your program has to first check their validity to make sure they don’t crash the program or get an unwanted (incorrect) result. What if they enter a number that is not in the `lats` or `lons` arrays (ie 75 instead of 75.5 degrees)? What if they enter a value at the edge of the map (ie `usrlon = 355.5`, such that there is no $j+1$ element of the array? 
#
# We have already written code that will handle most user inputs, now we just need to handle the special cases at the edges of the map. We know that the earth is in fact round, but this isn't reflected in the way we have chosen to label points on the map here, as 0 and 360 are normally not next to one another on a number line.
#
# In the cell(s) below, write a self contained program (you can recycle code from earlier parts of the lab) that runs through the whole process of *import/input, data scrubbing, presentation.*
#
# #### Import/Input
# This part should be pretty trivial, just copy/paste the appropriate code from above
#
# #### Data Scrubbing
# Use `if` `elif` `else` statements and *type casting* to handle the possible special cases for user input
#
# #### Output
# Generate a scientific figure with the following:
#
# * An X marking the selected location
# * Text beside the X specifying the lat, lon, elevation, slope, and aspect (E or W facing) of the point
# * All the regular fix-ins for a scientific figure:
#
# <div class="alert alert-block alert-info">
# <b>Scientific Figure Checklist:</b> 
#
# - [ ] Title 
# - [ ] Axes labels with units 
# - [ ] Legend
# - [ ] Does the figure *make sense* just by looking at it? The data should be clear without referencing anything outside the figure
# - [ ] Does it *look good*? 
# </div>

# %%
# your code here

# %%
