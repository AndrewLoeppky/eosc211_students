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

### Intro

[link to 9 debugging commandments](https://www.tygertec.com/9-rules-debugging/)

Are we going to use a formal debugger? 

```python
import numpy as np
from matplotlib import pyplot as plt
```

```python
# get the datafile
the_file = np.genfromtxt("lab9_old/mgsva_MJJ.csv")

the_file.shape
```
