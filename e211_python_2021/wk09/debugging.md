---
jupyter:
  jupytext:
    formats: ipynb,md
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

# Debugging

## EOSC 211

**Week 9 Day 1**

**Learning Objectives:**  
??


## Question 1

**Decide what the code fragment is trying to do, and how to fix the error so it performs the required task.**

```python
import numpy as np
A = np.random.rand(10,5) # creates a 10x5 matrix containing random numbers

# debug this code

def rowsum():
    rowsum = 0
    for k in range(len(A)):
        rowsum = rowsum + A[:,k]
```

```python
# andrew's soln

def rowsum(arr):
    """
    takes in a numpy array (n,m) arr and returns the sum of each column of the array (m,)
    """
    rowsum = np.zeros(len(arr[0,:])) # create an array with the same number of columns as arr
    for k in range(len(arr[0,:])): # loop through all the columns
        rowsum[k] = np.sum(arr[:,k])
    return rowsum

rowsum(A)
```

## Question 2

**This code is supposed to create a *running standard deviation*. Does it? If it doesn't, state why. If not, what is the problem?**

X=rand(1,10)
for k=1:length(X),
  Y(k)=std(X(max(1,k-3)):X(min(length(X),k+3)));
end;


```python
x = np.random.rand(10)
y = np.empty_like(x)
# debug this code
for k in range(len(x)):
    y[k] = np.std(x[min(0, k - 3) : max(len(x), k + 3)])
```

**A) What do you think this code is trying to do (be specific). Write down the steps in words**


your answer here


**B) Fix the code to perform the intended operation**

```python
# your code here
```

```python
# andrew's soln
#
# this is supposed to call the function np.std (calculate the standard deviation) for x[k-3:k+3],
# i.e. the running standard deviation. The min and max function calls handle the cases at the beginning and 
# end of the array where k-3 is a negative number (which refers to indexes from the end of the array). 
# the error is that the min and max functions are switched! It should call the GREATER of (0,k-3) and the
# LESSER of (len(x),k+3)
#

for k in range(len(x)):
    y[k] = np.std(x[max(0, k - 3) : min(len(x), k + 3)])
y
```

## Question 3

**Below is a list of common types of errors. Define them in your own words**


**A) Off-by-one error**:


**B) Fencepost error:**


## Question 4

**What do you see on the screen when you run this code (after fixing the error)?**


```python
x = 5
y = 3
for j in np.arange(0,5):
    y = y-1
    if j = 4:
        x +=4
```

```python
# your code here
```

```python
# andrew's soln
x = 5
y = 4
for j in np.arange(0,5):
    y = y-1
    if j == 4:
        x +=4
        
x, y
```
