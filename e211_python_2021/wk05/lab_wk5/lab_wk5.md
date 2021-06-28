---
jupyter:
  jupytext:
    formats: py:percent,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Lab Week 5

## EOSC 211

### Learning Objectives:

1. Write code with user-specified variables

2. Use formatted text with f string literals

3. Use conditional statements `if elif else`

second pass: the flow goes like
1) andrew imports the data and uses plt.annotation to label a user specified lat/lon/height on the map

2) student implements the slope equation to calculate variables "slope" and conditionals to figure out a variable "aspect"

3) talk about handling edge cases, arr[-1] and more conditionals to avoid "falling off the edge of the map"

4) final product: one code cell that, when run, takes in a user-specified lat/lon pair and outputs a scientific figure with the point labelled lat/lon/height/slope/aspect

```python
from e211_lib import e211 
from matplotlib import pyplot as plt
import numpy as np
```

```python
# get the data, hide the import function in e211 library
topo = e211.load_topo("lab5_topo.mat")
topo.shape # rows, columns
```

```python
plt.contourf(topo)
```

```python
# create lat and lon arrays just like week 3 lab
lats = np.linspace(-89, 90, topo.shape[0]) # added 0.5 deg to each point for simplicity
lons = np.linspace(0, 359, topo.shape[1])
```

`topo` is indexed from 0 to 359 (L to R), 0 to 179 (B to T). Lons matches the indexing nicely, lats can be correctly interpreted via `y = lats - 90`. the proper way to do this for any size of image would be to use `np.where(lats=usr_input)` but it looks complicated and may be confusing. (`lats` is indexed T to B, opposite `topo`) Arguments passed to `contourf` will accept the actual lon/lat coord but indexing `topo` requires the corrected index. Best approach = ???

```python
# take in a lat/lon point as input. old lab uses matlab's graphical input function
usrlat =  30 #int(input("lat: "))
usrlon =  100 #int(input("lon: "))

# get the indices of topo that match user specified lat and lon
ilat, ilon = usrlat - 90, usrlon

# make the plot (see lab 3)
img = plt.contourf(lons, lats, topo)
plt.xlabel("longitude (deg)")
plt.ylabel("latitude (deg)")

# use the "annotate" function to label the chosen point on the plot
plt.annotate("X", (usrlon, usrlat), color="red")
the_label = f"lat: {usrlat}$^o$\nlon: {usrlon}$^o$\nheight: {topo[ilat, ilon]}m"
plt.annotate(the_label, (usrlon + 10, usrlat));
```

<!-- #region -->
## 4  Calculate the topography slope

Once the point selection algorithm is working, you can start adding code to it to solve the follow-ing problem:What is the east/west slope (in degrees) at the point you clicked?The east/westslope is a height difference between the point immediately to the RIGHT (or EAST) of the oneyou picked and the one immediately to the LEFT (or WEST) of it,  divided by the horizontaldistance of these two points. Then take the arc-tangent to get the result in degrees:

$$
Slope \approx tan^{-1}\left(\frac{topo(i, j+1) - topo(i, j-1)}{\Delta LON \times 111e3 \times cos(LAT)}\right)
$$



| Symbol  | Variable      |  Units   |
|:--|:----------------------------------|:------------|
| $topo$     | topography array      | $height$ ($m$) |
| $i,j$  | lat, lon indices      | --  |
| $\Delta LON$  | change in longitude between two points      | $degrees$  |
| $111e3$  | at the equator, 1 degree=111000m      | $m/deg$  |
| $LAT$  | latitude of the point selected      | $degrees$  |
| $cos(LAT)$  | a correction factor to take into account longitude convergence at the poles     | --  |

1.  Add the code to make this work for points well within the DEM (i.e. away from the edges of the map). Make sure the trigonometric functions you use are for degrees and not radians. You may find the functions `np.deg2rad()` and `np.rad2deg()` helpful
<!-- #endregion -->

```python
slope = np.rad2deg(np.arctan((topo[ilat, ilon + 1] 
                              - topo[ilat, ilon - 1]) 
                              / (2 * 111e3 
                              * np.cos(np.deg2rad(usrlat)))))
slope, topo[ilat, ilon]
```

2.  Then use the built-in functiondisp(and you MUST use disp) to output to the screen:

(a)  The latitude and longitude of the selected point

(b)  The elevation AND the slope at that point (in degrees)(c)  a  message  saying  “Flat”  if  the  slope  angle  is  between  -0.1  and  +0.1  degrees,  but“East-facing” or “West-facing” if the slope is larger and either east- or west-facing,respectively. An “east-facing” slope tilts DOWN towards the east.in a nicely formatted ways, something like:

       At 30.5 N, 100.5 E, Height is 4014 m and the slope is -0.187 degrees This is East-facing
       
(note - latitudes can be N or S, longitudes can always be E).

```python
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
out_msg = f"At {abs(usrlat)} {latdir}, {usrlon} E, the height is \
{topo[ilat, ilon]} m and the slope is {round(slope,3)} degrees. This is {slopedir}."

print(out_msg)
```

##  Selections - check arguments

Often with user input, your program has to first check their validity to make sure they don’t crashthe program.  Re-run your code a few times and click around in different places to make sure itworks.  What happens if you click on a point outside the image itself (i.e., on the gray border)?What values does your program return forixandiyif you do this?  Where does your programcrash?  You should notice that if you click outside of the DEM, your code will automaticallymodify your point and place it on the edge of the map nearest where you clicked.  That’s good,but in this scenario your slope calculation no longer works. Why?Modify your code so that your program can still calculate the slope if your point lies on theedge of the DEM. That is, you need to test for the special cases whenixhas a value of1orlength(long)and, if so, adjust your slope calculation accordingly. Remember that the worldis round!  You might find it useful to define new variablesirightandileftto represent thecolumn-indices to the right and to the left of the point you clicked. Think carefully aboutwherein your code you should put this addition.  If you’re having trouble with the logic, try writingsome pseudo-code to help you lay out the flow of your program.


python has no problems with this, since array[-1] accesses the last element of the array (which is what we want). 

modify the plotting function instead?

```python
if slope > 0.1:
    aspect = "west"
elif slope < -0.1:
    aspect = "east"
else:
    aspect = "flat"

# make the plot (see lab 3)
img = plt.contourf(lons, lats, topo)
plt.xlabel("longitude (deg)")
plt.ylabel("latitude (deg)")

# use the "annotate" function to label the chosen point on the plot
plt.annotate("X", (usrlon, usrlat), color="red")
the_label = f"lat: {usrlat}$^o$\nlon: {usrlon}$^o$\nheight: \
{topo[ilat, ilon]}m\nslope: {round(slope, 3)}$^o$\naspect: {aspect}"
plt.annotate(the_label, (usrlon + 10, usrlat));
```
