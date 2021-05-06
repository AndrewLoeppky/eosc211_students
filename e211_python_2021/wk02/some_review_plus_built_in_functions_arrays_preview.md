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

# Some Review Plus Built-In Functions, Arrays Preview

## EOSC 211

**Week 2 Day 2**

**Learning Objectives:**  
1.	Review variable assignment, structural elements of PYTHON
2.	Introduce the idea of arrays[lists?] (from lab)
3.	Using built-in functions




### Question 1

**The code snippet below was intended to calculate the surface area of the Earth and print the answer to the screen.**

```python
# radius of earth
radius = 6371  # km
area = 4 * 3.14 * radius * radius

# radius of moon
radius = 1739  # km
area = 4 * 3.14 * radius * radius

print(area)
```

**A) What is the actual output (describe the quantity in words) of the code snippet?**


your answer here


**B) Identify the following:** 


A) Variable names:

B) Operators:

C) Reserved words:

D) Special characters:


**C) Next to each line of the code snippet write down what the line of code does**


    radius = 6371  # km
    area = 4 * 3.14 * radius * radius

    radius = 1739  # km
    area = 4 * 3.14 * radius * radius

    print(area)


### Question 2

**Let's create a *list* variable called `mags` containing 10 earthquake magnitudes**

```python
mags = [4.2000, 4.1000, 4.1000, 4.1000, 4.3000, 4.2000, 4.4000, 4.1000, 4.0000, 4.7000]
```

**A) In the cell below, write a line of code to access the 3rd item in `mags`:**

```python
# your code here
```

```python
# andrew's solution
mags[2]
```

**B) Define a new variable called `mags2` containing the last magnitude in the list:**

```python
# your code here
```

```python
# andrews solution
mags2 = mags[9]
# or
mags2 = mags[-1]

mags2
```

### Question 3

**A) Built-In Functions: Assume you have variable mags defined above.  What is the output to the screen of the following command?**

```python
y3 = max(mags[3:8])
```

your answer


**B) Write down in words the steps involved in getting the output.**


your answer
