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

# Logic

## EOSC 211

**Week 5 Day 1**

**Learning Objectives:**  
1. ?

**Write either Python or pseudo code to solve the following problems (change cells to 'markdown' if writing pseudo code)**


## Question 1

**Assume you have two variables `X` and `Y`, which each hold a single number. Assign the smallest of the two numbers to the variable `sml`.**

```python
# your code here
```

```python
# andrew's soln
x = 1
y = 2

if x < y:
    sml = x
else:
    sml = y
```

## Question 2
**Modify your code, so that SML contains `None` if the values `X` and `Y` are the same.**

```python
# your code here
```

```python
# andrew's soln
if x < y:
    sml = x
elif x == y:
    sml = None
else:
    sml = y
```

## Question 3

**Modify your code to put the smallest of the numbers in a 3-element list `X=[a, b, c]` into the variable SML.**

```python
# your code here
```

```python
# andrew's soln
x = [14, 21, 1]
sml = min(x)
```

## Question 4

**Longitudes “wrap around” the earth, so that any longitude may be given as a positive value between 0 and 360 degrees (going eastward), or a negative value between 0 and -360 degrees (going westward). The location of the “0” degree line is the same in both cases. But this means that a longitude of 355 and a longitude of -5 refer to the same place!
Given two arbitrary values LON1 and LON2 in the range -360 to +360, write a selection that decides whether these two values refer to the same point. Create a variable same that has a value of `True` if they refer to the same point and a value `False` if they refer to different points.**

**Does it work? - Test your code with pairs of numbers like (5,5), (5,-355), (5,355),(-5,355),(0,0),(360,360),(0,360), etc**

```python
# your code here
```

```python
# andrew's soln
lon1 = 355
lon2 = -5

lons = (lon1, lon2)

# use the sml function from q3
sml = min(lons)
big = max(lons)

if big - sml == 360:
    same = True
# catch the case where lon1 = lon2
elif big - sml == 0:
    same = True
else:
    same = False
    
print(same)
```
