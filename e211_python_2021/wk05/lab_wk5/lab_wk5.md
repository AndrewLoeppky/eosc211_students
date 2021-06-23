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

1. objective

2. objective 2

first pass: Andrew solves the lab from the old course, but in python

```python
from e211_lib import e211 
from matplotlib import pyplot as plt
import numpy as np
```

```python

```

```python

```

```python
# get the data, hide the import function in e211 library
topo = e211.load_topo("lab5_topo.mat")
topo.shape
```

```python
# create lat and lon arrays just like week 3 lab
lats = np.linspace(-89.5, 89.5, topo.shape[0])
lons = np.linspace(0.5, 359.5, topo.shape[1])
```

```python
# take in a lat/lon point as input. old lab uses matlab's graphical input function
iy = np.where(lats==17)  ## int(input("lat: "))
ix = np.where(lons==114)  ## int(input("lon: "))

# make the plot (see lab 3)
img = plt.contourf(lons, lats, topo)
plt.xlabel("longitude (deg)")
plt.ylabel("latitude (deg)")
the_label=f'lat: {lats[iy]}$^o$\nlon: {lons[ix]}$^o$\nheight: {topo[ix,iy]}m'
arrowprops={'arrowstyle':'->'}
plt.annotate(the_label, (ix, iy), arrowprops=arrowprops)
```

```python

```

```python

```
