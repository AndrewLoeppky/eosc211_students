---
jupyter:
  jupytext:
    main_language: matlab
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---


# Week 2 Day 1

## Concepts for Today’s Class:
* Steps in problem solving
* MATLAB syntax: underlying structure
* Syntax versus semantics

**Reading:**
See course web site for details, we’ll cover material in:

* pgs 6-40 (in class)
* pgs 3-6, 75-80, 89-101 (labs)
* pgs 557-564 (general reference, will show up in classes)

**Lab:**
Bring text

* Labs due at 4pm on Fridays
* TA hours, EOS-Main 203 – make sure to note which weeks these carefully! <br>
>**Friday** (wks 3,4,5,6,8,9,10,11): 9:30 am – 10:30 am <br> 
 **Monday** (wks 7,10 only): 11:00 am – noon* <br>
    
United Launch Alliance Atlas V 411 with NASA OSIRIS-REx mission lifts off from Cape Canaveral, Sept 2016

<img src="media\week02_Class1_SyntaxOverview_postclass-slide_0-000.png">



## Good Problem Solving Techniques

<img src="media\week02_Class1_SyntaxOverview_postclass-slide_1-001.png" height="500">



## Good Problem Solving Techniques 2
We will adopt the 5-step program  (NOTE: this is more complete than the approach in the text book on page 76)

> 1) State the problem clearly <br>
> 2) Describe your input and output info / data <br>
> 3) Write down the problem-solving procedure IN WORDS (*pay special attention to the logic. If possible work the problem “by hand” for a simple set of data)* <br>
> 4) Develop a MATLAB code to do (3) <br>
> 5) Test your code with a variety of data or different cases

*Example:  What was the largest earthquake in the Vancouver / Vancouver Island region in the past year?*



## Example

http://www.iris.edu/hq/audience/public/earthquakes
http://earthquake.usgs.gov/regional/neic/
http://earthquakescanada.nrcan.gc.ca/index-eng.php

Goal:  Find the largest earthquake in the Pacific Northwest during 08/30/2017– 08/31/2018. I have only printed out eqs w/ magnitudes larger than 4.0

Write down input and output in words
Give numeric value for the actual output. Write down the procedure you used to get your answer

<img src="media\week02_Class1_SyntaxOverview_postclass-slide_3-002.png">



## Finding the Largest Earthquake

My procedure or algorithm:
1) Read magnitude on first line, and remember
2) Read magnitude on second line
3) Compare with first, and
remember only the largest of the 2
4) Read magnitude on the next line
5) Compare with largest, and
remember the largest of these two
6) Repeat steps 4-5, until reach end of list
7) Tell you my largest magnitude

## Finding the Largest Earthquake (Cont'd)

My procedure or algorithm:

```matlab
read mag1
read mag2

Is mag2 > mag1 ?
    YES:  biggest = mag2
    NO:   biggest = mag1

read next_mag

Is next_mag > biggest  ?
    YES: biggest = next_mag
    NO: don’t need to update biggest

write out biggest
```

How do we turn this into *matlab* code?

## MATLAB:  Programming Elements (Overview)

**The structure of MATLAB** <br>

**Lexical Elements:** building blocks <br>
> Programming Language: *names, operators, special characters*<br>
> Human Language: *words, symbols, punctuation*


**Syntax**: a set of rules to combine lexical elements into legitimate constructs

> Programming language: *how to build expressions, statements,
functions & programs* <br>
> Human Language: *how to build sentences & paragraphs*

## Lexical Elements (Building Blocks)

### Names

**Variable names:** store data (e.g. our user defined variable ```mag1```)<br>
**Reserved words:** have a special meaning, cannot be redefined (e.g. ```for```) <br>
**Function names:** sequences of code (e.g. ```sin()```)<br>

### Operators

**Logical:** e.g. ```&&``` (text p. 20) <br>
**Arithmetic:** e.g.   ```+, -, *, /```	(text p. 12-13) <br>
**Relational:** e.g. ```>, >=, <, <=``` (text p. 19) <br>
**Special characters:** keyboard characters with special meaning in MATLAB.
e.g.```;    {}    ()```

## Lexical Elements II

How are variables assigned in MATLAB?

```matlab
>> mag1 = 4.9
```

What does this do?

* Creates a space in memory
* Gives the space the name ```mag1```.  We call ```mag1``` a *variable*.
* Stores the value ```4.9``` in that space (variable)
* Echoes back this information

The prompt reappears:

```matlab
>> mag1 = 3.7
```

<!-- #region -->
overwrites ```4.9``` with ```3.7```


Note: ```"="``` does not mean = in the mathematical sense.  Instead, it means *“assign the number on the RHS to the variable on the LHS”*.
We can do math on the RHS, mixing numbers and variables

## Syntax

Lexical elements are combined using the set of rules known as “syntax”

>"I cdnuolt blveiee that I cluod aulacity uesdnatnrd what I was rdgnieg."

Important difference between human and programming languages is tolerance to syntax errors versus tolerance to spelling/grammar errors

## Examples of Syntax Errors

Usually / often your code will not run if you make a syntax error:
<!-- #endregion -->

```matlab
>> x=10;
```

defined my variable x and assigned it a value of 10

```matlab
>> y=cos(x
         ↑
Error: Invalid expression. When calling a function or indexing a variable, use parentheses. Otherwise, check for mismatched
delimiters.
```

trying to compute cos(x) and assign it to variable y
??? y=cos(x <br> 
Correct: ```y = cos(x)```

```matlab
>> y=2x
      ↑
Error: Invalid expression. Check for missing multiplication operator, missing or unbalanced delimiters, or other syntax error. To
construct matrices, use brackets instead of parentheses.
```

trying to compute “2 times x” and assign it to “y”
??? y=2x				Correct: y = 2*x (spaces around = don’t matter)

## Syntax versus Semantics
When a program doesn’t work this can happen because: <br>
SYNTAX is incorrect -- e.g.

```matlab
>> distance = speed *
```

multiplication (```*```) needs numbers or variables on both sides of ```*``` 

SEMANTICS are incorrect -- e.g.

```matlab
>> distance = speed / time
```

may or may not run but will certainly give you the wrong answer!!
The program you wrote is not the program you meant to write!

## Example of Semantics Error

```matlab
mag1 =4.9;
mag2 =5.3;
if (mag1 < mag2)
    max_mag = mag1;
else
    max_mag = mag2;
end
```

Here’s a code snippet for finding the largest of 2 earthquakes.
What is wrong?

## Wrap Up

**Steps in problem solving**

1. State problem clearly
2. Define the input/output
3. Write down algorithm by hand: ie., think the problem through
4. Code in MATLAB
5. Test, test, test…

**Underlying structure of MATLAB syntax**

* building blocks: names, operators, special characters

**Syntax versus semantics**

* syntax errors are about bugs in step 4 above
* semantics errors usually result from skipping step 3

<!-- #region -->

## Lab Overview

**Learning Goals:**

* Become familiar with MATLAB environment
* Load, plot and save data
* Try some simple operations
* Write MATLAB scripts

<img src="media\week02_Class1_SyntaxOverview_postclass-slide_15-004.png" height="300">

a) pair programming <br>
b) need either an account, or your own version of MATLAB <br>
c) turn in requested file on Canvas (not graded but will use later in term)






<img src="media\week02_Class1_SyntaxOverview_postclass-slide_15-003.png" height="400">



<!-- #endregion -->
