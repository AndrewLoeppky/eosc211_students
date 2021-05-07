---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Data Structures II

## EOSC 211

**Week 3 Day 2**

**Learning Objectives:**  
1. ?

Useful references:

[Professor Kazarinoff](https://github.com/ProfessorKazarinoff/Problem-Solving-with-Python-37-Edition/blob/master/notebooks/05-NumPy-and-Arrays/05.03-Python-Lists-and-NumPy-Arrays.ipynb)

[Numpy Documentation](https://numpy.org/doc/stable/reference/generated/numpy.array.html)



## Question 1)

**A) Execute the following cells and describe IN WORDS what is happening in each cell**

```python
lats=np.arange(1,21)
lats=np.arange(10,16)
```

```python
L2 = np.array([lats[2], lats[4]])
```

```python
L3 = np.array([lats[-1], lats[0]])
```

```python
L4 = lats[lats > 13]
```

```python
L5 = lats[lats >= 13]
```

```python
L6 = lats[::-1]
```

```python
L7 = lats[-1]
L7 = lats[4]
L7 = lats[len(lats)-1]
```

## Question 2

**A) We can change the shape of our `lats` array with numpy's built in funciton `reshape()`. What does the following code do?**

```python
newlats = lats.reshape([2,3])
```

**B) What are all the possible shapes we can reassign to `lats`? Why do some work and others not**


your answer here


**C) We can return `lats` to it's original shape using `flatten()`, i.e.**

```python
lats = newlats.flatten()
lats
```

**How else could you accomplish this? Write code in the following cell that outputs the same result starting with any of the `newlats` shapes we used above**

```python
# your code here
```

```python
# andrew's soln
lats = lats.reshape(len(lats))
lats
```

## Question 3

old question 3 from matlab version introduces OO data structure featuring a student 'joe lunchbucket', who's attributes include birthday and grade in EOSC211. Replace with different content and do talk about classes later?


## Question 4

**Along with `+`, `-`, `*`, `/`, python also defines the *floor division operator* `//` and the *modulo operator* `%`. Floor division (`//`) outputs the *quotient* of two integers, and modulo (`%`) outputs the remainder. Example code:**

```python
5 // 2
```

```python
5 % 2
```

**Write a few lines of code that will create the array `B`, which contains only the even valued elements of an array `A`. You don't know the size of `A` but you do know it contains only integers.**

```python
# your code here
```

```python
# andrew's soln
A = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
B = A[A % 2 == 0]
B
```
