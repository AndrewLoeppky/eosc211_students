---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.10.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Loops and Vectorization

## EOSC 211

**Week 5 Day 1**

**Learning Objectives:**  
1. Make code more efficient and cleaner by using vector operations instead of loops
2. Get familiar with the timeit decorator




## Question 1

**Re-write the following function without a loop**

```python
import numpy as np
x1 = np.random.rand(1000000)
x2 = np.empty_like(x1)

# rewrite this code
def more_than_half(x1):
    x2 = np.empty_like(x1)
    for i in range(len(x1)):
        if x1[i] > 0.5:
            x2[i] = 1
        else:
            x2[i] = 0
    return x2
```

```python
# your code here
```

```python
# andrew's soln
def more_than_half(x1):
    x2 = np.zeros_like(x1)
    x2[np.where(x1 > 0.5)] = 1
    return x2

x2 = more_than_half(x1)
print(x1[:5])
print(x2[:5])
```

## Question 2

**Which of the two code snippets perform the operation faster? We can find out using the `timeit` module! The code below shows how long it takes for a simple function to run (the @ is called a *decorator function*, more info [here](my favorite decorator tutorial)). Modify the snippet below to time your functions for question 1.**

```python
from wk11_functions import timeit

@timeit
def count_one_million():
    for i in range(1000000):
        x = i
        
count_one_million()
```

```python
# your code here
```

```python
# andrew's soln


@timeit
def loop(x1):  ## just copy and paste the function body
    x2 = np.empty_like(x1)
    for i in range(len(x1)):
        if x1[i] > 0.5:
            x2[i] = 1
        else:
            x2[i] = 0
    return x2


@timeit
def vector(x1):
    x2 = np.zeros_like(x1)
    x2[np.where(x1 > 0.5)] = 1
    return x2


print(f"Loop:{loop(x1)}")
print(f"Vector:{vector(x1)}")
```

## Question 3

**The points on a circle, radius $R$, centered at $(x_c,y_c)$ are given by**

$$
x = x_c + R cos(\theta)
$$
$$
y = y_c + R sin(\theta)
$$

**where $\theta$ is the angle between the x-axis and the line from the center of the circle to any given point on the circle.  i.e. $\theta$ goes from $0$ to $2\pi$.**

**Write a function called `getcirc` that will take as input the variables `xc`, `yc`, `R` and the number of points on the circle `N` in that order and return numpy arrays `x` and `y` containing the x and y coordinates of the N points on the circle.**

**Add a subfunction called checkRN that checks that the radius R is positive and that the number of points is at least 20 (for a reasonably smooth circle).**


```python
# your code here
```

```python
# andrew's soln
def getcirc(xc, yc, R, N):
    """
    Generates a circle of radius "R", centered at point (xc, yc), 
    containing N points. 
    
    Returns circle coords x, y (numpy arrays)
    """
    def check_RN(R, N):
        """
        errors must not pass silently, unless explicitly silenced 
                                                             -T.P.
        """
        if R < 0:
            print("radius must be > 0")
        elif N < 20:
            print("number of points must be > 20")
        else:
            pass  
        
        return None
    
    check_RN(R, N)
    
    # or 
    assert (R > 0), "radius must be > 0"
    assert (N >= 20), "number of points must be >= 20"
    
    theta = np.linspace(0, 2 * np.pi, N)
    
    x = xc + R * np.cos(theta)
    y = yc + R * np.sin(theta)
    
    return x, y
```

```python
# test out my function
x, y = getcirc(1,1,10,20)

from matplotlib import pyplot as plt
plt.plot(x,y)
```
