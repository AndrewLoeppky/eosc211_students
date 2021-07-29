---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Midterm Review

## EOSC 211

**Week 7 Day 1**

+++

## Question 1

**If  `a = np.array([7, 6, 5, 4, 3, 2, 1])`, what would be the values of  `b`, `c`, `d`, and `e` if:** 


`b = a[1:3:7]`

`c = [a / 2]`

`d = a[1:2] @ a[5:6]`

`e = np.array([[1, 1],[2, 2]]) @ np.array([a[0:2],a[1:3]])`

**Determine the output as well as the data type of the output**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
import numpy as np

a = np.array([7, 6, 5, 4, 3, 2, 1])
b = a[1:3:7]
c = [a / 2]
d = a[1:2] @ a[5:6]
e = np.array([[1, 1], [2, 2]]) @ np.array([a[0:2], a[1:3]])
for i in [a, b, c, d, e]:
    print(i, type(i))
```

## Question 2

**What is the result of the following expressions?**

**A)** `6 == 2 + 3 * 1`

**B)** `14 > np.arange(6,2,-1) * 3 + 1`

**C)** `3 ** 0 / 4 - -3 / np.array([4, 3])`

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
a = 6 == 2 + 3 * 1
b = 14 > np.arange(6,2,-1) * 3 + 1
c = 3 ** 0 / 4 - -3 / np.array([4, 3])

[print(letter) for letter in [a,b,c]]

## this is too easy?
```

## Question 3

**This cell is supposed to find local minimums in the input time series, i.e. points that have values less than their neighbours on either side, and return their indices in `x`. But it has some bugs in it. Explain what they are and fix them.**

+++

```python
# fix this code
# y is a 1x100 array given as input
a = np.linspace(0,4*np.pi,100)
y = np.sin(a)
k = 0
while k < 100:
    if y[k] < y[k + 1] and y[k] > y[k - 1]:
        x[k] = k
    k = k - 1
```

```{code-cell} ipython3
# andrew's soln
a = np.linspace(0,4 * np.pi,100)
y = np.sin(a)
x = np.array([]) # we need to create an empty array to add to
k = 1 # since we need to reference k-1, start at the second element of the array and end at the second last
while k < len(y)-1: # this is better than hardcoding the limits for k. what if y changes?
    if y[k] < y[k+1] and y[k] < y[k-1]:
        x = np.append(x,k) 
    k += 1 # iterate forward, not backward

print(x)
```
