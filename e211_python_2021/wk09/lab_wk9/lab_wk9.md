---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Lab Week 9

## EOSC 211

### Learning Objectives:

1. Debug code

(other possibilities):

2. use dictionary keys to reference complex datasets instead of RC indexing

3. work with purely functional code?

### Intro

[link to 9 debugging commandments](https://www.tygertec.com/9-rules-debugging/)

Are we going to use a formal debugger? 

or...

Pivot learning goals and use this week to talk about dictionaries?

```python
import numpy as np
from matplotlib import pyplot as plt
```

```python
# get the datafile
the_file = np.genfromtxt("lab9_old/mgsva_MJJ.csv",delimiter=",")

# extract variables from the csv
# (explicit + flat is better than implicit + nested)
lats = the_file[:,1]
lons = the_file[:,2]
u_vel = the_file[:,3]
v_vel = the_file[:,4]
#u_dev = the_file[:,5]
#v_dev = the_file[:,6]

# or
# (namespaces are a honking great idea)
var_dict = {"lats":the_file[:,1], 
            "lons":the_file[:,2], 
            "u_vel":the_file[:,3],
            "v_vel":the_file[:,4]}
            #"u_dev":the_file[:,5],
            #"v_dev":the_file[:,6]}
```

```python
def move_to_grid(lats, lons, u_vel, v_vel):
    """
    function to create 2D arrays out of FORTRAN formatted csv data
    
    in:
    csv file with columns 15000., lon, lat, u_vel, v_vel, u_dev, v_dev
    
    (dev is the standard deviation of each velocity measurement, 15000.
    is an artifact from FORTRAN formatting)
    
    out: 
    1D arrays: lat_0, lon_0
    2D arrays: u, v
    """
    # set up grids
    # initializing with NaNs also automatically deals with points where there is
    # no data (eg. on land) because those locations will simply contain NaNs
    lon_0 = np.arange(-179,180)
    lat_0 = np.arange(-89, 89)

    u = np.full([179, 360], np.nan)
    v = np.full([179, 360], np.nan)

    # Loop through all points in .csv file.
    #
    # For each, calculate the row/col indices
    # from the lat/longs.  Lats get converted
    # into row indices 'i', and longs into column
    # indices 'j'. Since we have a 1 degree spacing
    # we just have to add the right offset
    # to make this work - for example, for latitudes
    # latitude of -89 goes to row 0,
    # latitude of -88 goes to row 1, etc.
    #
    # Then write the
    # corresponding U/V data for that lat/long
    # into the right place (i.e. index (i,j) )
    # in the U/V matrices 

    
    for k in range(len(lats)):
        i = int(lons[k]) + 78  # row index
        j = int(lats[k]) + 179  # column index
        u[i,j] = u_vel[k]
        v[i,j] = v_vel[k]
        
    return lon_0, lat_0, u, v
```

```python
def mean2d(in_map, winlen):
    """
    Takes a 2D running mean of an input np array
    
    in:  winlen -- window length
         in_map -- numpy array on which to perform the running mean. 
        
    assumes in_map is a world map, and wraps longitude[-1] around to [0] 
    
    out: out_map -- the filtered map
    """
    # put the actual filtering operation in a subfunction
    def do_mean(in_map, winlen):
        # initialize the output array and relevant variables
        out_map = np.empty_like(in_map)
        nrows, ncols = in_map.shape
        wn = int((winlen - 1) / 2)
        
        # loop through each element in the map and perform the average
        # no attempts made yet to address edge effects
        for i in range(nrows):
            for j in range(ncols):
                # don't filter the land elements (not working.. why?)
                if not np.isnan(in_map[i,j]):
                    the_window = out_map[i - wn:i + wn + 1,j - wn:j + wn + 1]
                    # nanmean is a function that takes the mean
                    # while ignoring nan values
                    out_map[i,j] = np.nanmean(the_window) 
                else:              
                    out_map[i,j] = np.nan
        return out_map
      
    
    # check for odd winlen
    winlen = int(winlen)
    if winlen % 2 == 0:
        print("input arg winlen must be even")
        return None
    # winlen of 1 means "do nothing"    
    elif winlen == 1:
        return in_map
    # do the calculation and return result
    else:
        return do_mean(in_map, winlen)
    

```

```python
#lons, lats, u, v = move_to_grid(lats, lons, u_vel, v_vel)  # the standard way
lons, lats, u, v = move_to_grid(**var_dict)  # the honking great way

# calculate magnitude of current velocity
m = (u ** 2 + v ** 2) ** 0.5

# filter the velocity fields
filter_width = 11
u_filt = mean2d(u, filter_width)
v_filt = mean2d(v, filter_width)
m_filt = mean2d(m, filter_width)

# grab only the decfac^th element of each array on which to plot arrows
#arrow_mask = np.
```

```python
fig, ax = plt.subplots(figsize = (30,20))

ax.contourf(m_filt)
ax.quiver(u_filt, v_filt, pivot="middle")

```

```python
# splatting and doublesplatting tutorial snippet

my_list = [3,4]
my_dict = {"a":5, "b":6}

def print_vars(a, b):
    print(a)
    print(b)
    return None

print("normal function call:")
print_vars(1,2)  
print("splat from a list (or tuple)")
print_vars(*my_list)
print("double splat from a dictionary")
print_vars(**my_dict)
```

```python
np.nanmean(np.array([np.nan, np.nan,1]))
```

```python

```

```python

```

```python

```
