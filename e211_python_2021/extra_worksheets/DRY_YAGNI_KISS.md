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

# DRY, YAGNI, and KISS

## EOSC 211

### Learning Goals

* Understand 3 principles of code design in order to solve problems with the appropriate level of complexity
* Apply the law of diminishing returns to code development

(exposition on DRY, YAGNI, KISS)

### Your Task

You are presented with the following problem:

$$
13.2 \times 8539 = \space x
$$
$$
14.2 \times 231 = \space y
$$
$$
11.0 \times 3333 = \space z
$$

Your job is to develop effective code to answer this question. 


#### Method 1: Use Python as a Calculator

Write a very simple code cell that performs the calculation. Time how long it takes you to obtain the answer.

```python
# your code here
```

```python
# soln
x = 13.2 * 8539
y = 14.2 * 231
z = 11.0 * 3333
```

#### Method 2: Generalize Your Code 

Method 2 appears to work, but what if we had to perform a larger number of similar calculations for some future problem? We can avoid writing out each varaible `x`, `y`, `z` and **repeating ourselves** by defining a function `multiply()` which takes in input arrays of arbitrary size and returns their product. Again, time how long it takes you to reach the solution.

```python
# your code here
```

```python
# soln
import numpy as np

def multiply(var1, var2):
    """
    returns the product of two inputs var1, var2
    """
    return var1 * var2

vec1 = np.array([13.2, 14.2, 11.0])
vec2 = np.array([8539, 231, 3333])

x, y, z = multiply(vec1, vec2)
```

<!-- #region -->
#### Method 3: Expand Your Code's Capabilities

We can expand on our `multiply()` function to make it even more general-use. In the cell below, modify your function such that it can take two input variables and add, subtract, multiply, or divide them. Have the function print to the screen both the input equations and the solutions, i.e.

```python
vec1 = np.array([13.2, 14.2, 11.0])
vec2 = np.array([8539, 231, 3333])

do_math(vec1, vec2, "+")
```
```
    13.2 + 8539 = 8552.2
    14.2 + 231 = 245.2
    11.0 + 3333 = 3344.0
```

If an invalid operation is entered, print a message `"please input a valid mathematical operation +, -, *, or /"`. How long does this take you to do this time?
<!-- #endregion -->

```python
# your code here
```

```python
# soln
def do_math(var1, var2, operation):
    """
    performs simple mathematical operations in an overly complicated way
    """
    if operation == "+":
        ans = var1 + var2
    elif operation == "-":
        ans = var1 - var2
    elif operation == "*":
        ans = var1 * var2
    elif operation == "/":
        ans = var1 / var2
    else:
        print("please enter a valid operation +, -, *, or /")
        
    for v1, v2, a in zip(var1, var2, ans):
        print(v1, operation, v2, "=", a)
    return None

do_math(vec1, vec2, "+")
```

### Reflection

In your opinion, which of the above methods is the best solution for the given problem? Evaluate all three methods in terms of DRY, YAGNI, and KISS. State which one you thought was the best use of your time as a scientific programmer.


your answer here
