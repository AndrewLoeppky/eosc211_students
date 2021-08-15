---
jupytext:
  formats: ipynb,md:myst
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

# Data Structures

## EOSC 211

**Week 3 Day 1**

**Learning Objectives:**  
1. Introduce numpy arrays
2. Use some of numpy's built in functions to generate arrays efficiently
2. Use slicing to access and change elements of an array 

Useful references:

[Professor Kazarinoff](https://github.com/ProfessorKazarinoff/Problem-Solving-with-Python-37-Edition/blob/master/notebooks/05-NumPy-and-Arrays/05.03-Python-Lists-and-NumPy-Arrays.ipynb)

[Numpy Documentation](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

```{code-cell} ipython3
# import the numpy package - an extension of python's core built in functions
import numpy as np
```

### Question 1: Generating Arrays

Some built-in functions (functions that come with the numpy package) which may be useful:

```python
    np.arange()
    np.zeros()
    np.ones_like()
    np.linspace()
    my_array.shape
    my_array.T
```
    
There are several correct ways to do each of these; some strategies are better than others. Have a look at the [numpy documentation](https://numpy.org/doc/stable/reference/generated/numpy.array.html) for help using numpy's built in functions

**A) Represent the following vector as a numpy array called `var1`**

$$
(1.1, 2.2, 3.3, 4.4, 5.5) 
$$

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var1 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
```

**B) Create a numpy array called `var2` with numbers 0 to 10**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var2 = np.array([0,1,2,3,4,5,6,7,8,9,10])
# or
var2 = np.linspace(0,10,11)
# or
var2 = np.arange(0,11)
var2
```

**C) Create a numpy array called `var3` containing all odd numbers (in order) from 0 to 1000**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var3 = np.arange(1,1000,2)
```

**D) Represent the following matrix as a numpy array called `var4`**

$$
\begin{pmatrix}
1 & 1 \\
2 & 3 \\
5 & 8
\end{pmatrix}
$$

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var4 = np.array([[1,1],[2,3],[5,8]])
```

**E) Is `var4` a 2 x 3 array or a 3 x 2?**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var4.shape
```

**F) Make an array called `var5` that looks like this. (hint: you shouldn't have to type it all out)** 

$$
\begin{pmatrix}
1 & 2 & 5\\
1 & 3 & 8\\
\end{pmatrix}
$$

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var5 = var4.T
```

**G) Create an array called `var6` with 10 rows and 5 columns where all elements are zero**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var6 = np.zeros([10,5])
```

**H) Create an array called `var7` that has 5 rows and 10 columns where all elements are the number 1**

```{code-cell} ipython3
var7 = np.ones_like(var6.T)
# or 
var7 = np.ones([5,10])
```

## Question 2: Array Slicing

**A) Use slicing to get the 3rd element in `var1`. REMEMBER that in Python we count starting from zero, so the first element of an array would look like `my_array[0]`**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var1[2]
```

**B) The 2nd, 3rd, and 4th elements of `var1`**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var1[1:4]
```

**C) The last 20 elements in `var3`**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var3[-20:]
```

**D) The element in the third row and second column of `var4`**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var4[2,1]
```

**E) The last column of `var5`**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
var5[1,:]
# or
var5[-1,:]
```
