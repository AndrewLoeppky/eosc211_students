---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
---

<!-- #region -->

# Slide 0
```

Concepts for Today’s Class:
steps in problem solving
MATLAB syntax: underlying structure
syntax versus semantics
Reading:
See course web site for details, we’ll cover material in:
pgs 6-40			(in class)
pgs 3-6, 75-80, 89-101	(labs)
pgs 557-564		(general reference, will show up in classes)
Lab:
bring text
Labs due at 4pm on Fridays
TA hours, EOS-Main 203 – make sure to note which weeks these carefully!
Friday (wks 3,4,5,6,8,9,10,11):    9:30 am – 10:30 am
Monday (wks 7,10 only):          11:00 am – noon.
United Launch Alliance Atlas V 411 with NASA OSIRIS-REx mission lifts off from Cape Canaveral, Sept 2016

```





<img src="media\week02_Class1_SyntaxOverview_postclass-slide_0-000.png">

<!-- #endregion -->

<!-- #region -->

# Slide 1
```

Good Problem Solving Techniques
Work in pairs and write down the steps in algorithm design (problem solving using MATLAB) mentioned in the text book (or if you didn’t get that far in the reading just write down what you think are reasonable steps)

```





<img src="media\week02_Class1_SyntaxOverview_postclass-slide_1-001.png">

<!-- #endregion -->


# Slide 2
```

Good Problem Solving Techniques
We will adopt the 5-step program  (NOTE: this is more complete than the approach in the text book on page 76)
State the problem clearly
Describe your input and output info / data
Write down the problem-solving procedure IN WORDS
- pay special attention to the logic
- if possible work the problem “by hand” for a simple set of data
Develop a MATLAB code to do (3)
Test your code with a variety of data or different cases
Example:  What was the largest earthquake in the Vancouver / Vancouver Island region in the past year?

```


<!-- #region -->

# Slide 3
```

http://www.iris.edu/hq/audience/public/earthquakes
http://earthquake.usgs.gov/regional/neic/
http://earthquakescanada.nrcan.gc.ca/index-eng.php
Goal:  find the largest earthquake in the Pacific Northwest during 08/30/2017– 08/31/2018. I have only printed out eqs w/ magnitudes larger than 4.0
Write down input and output in words
Give numeric value for the actual output
3.	Write down the procedure you used to get your answer

```





<img src="media\week02_Class1_SyntaxOverview_postclass-slide_3-002.png">

<!-- #endregion -->


# Slide 4
```

Finding the Largest Earthquake
My procedure or algorithm:
read magnitude on first line, and remember
read magnitude on second line
compare with first, and
remember only the largest of the 2
read magnitude on the next line
compare with largest, and
remember the largest of these two
repeat steps 5-7, until reach end of list
tell you my largest magnitude

```




# Slide 5
```

Finding the Largest Earthquake
My procedure or algorithm:
read mag1
read mag2
Is mag2 > mag1  ?
YES:  biggest = mag2
NO:   biggest = mag1
read next_mag
Is next_mag > biggest  ?
YES:  biggest = next_mag
NO:    don’t need to update biggest
write out biggest
how do we turn this into matlab code?

```




# Slide 6
```

MATLAB:  Programming elements (overview)
The structure of MATLAB
Lexical Elements
- building blocks
Syntax
- set of rules to combine lexical elements into legitimate constructs
Programming language
names, operators, special characters
Programming language
how to build expressions, statements,
functions & programs
Human Language
words, symbols, punctuation
Human Language
how to build sentences & paragraphs

```




# Slide 7
```

Lexical Elements (Building Blocks)
Names
Variable names:
Reserved words:
Function names:
2.	Operators
Logical:
Arithmetic:
Relational:
sequences of code; e.g. sin
have a special meaning, cannot be redefined; e.g. for
store data: e.g., our user-defined variable: mag1
e.g.,   &&			text p. 20
e.g.,   +, -, *, /		text p. 12-13
e.g.,   >, >=, <, <=		text p. 19
Special characters:	keyboard characters with special meaning in MATLAB.
e.g.,  ;    {}    ()

```




# Slide 8
```

Lexical Elements (Building Blocks)
Names:		variable names, reserved words, function names
2.	Operators:		logical, arithmetic, relational
Special characters:	keyboard characters with special meaning in MATLAB.
mag1 =4.9;
mag2 =5.3;
if (mag1 > mag2)
max_mag = mag1;
else
max_mag = mag2;
end
Worksheet Part D

```




# Slide 9
```

Lexical Elements (Building Blocks)
How are variables assigned in MATLAB?
>> mag1 = 4.9
What does this do?
Creates a space in memory
Gives the space the name “mag1”.  We call mag1 a VARIABLE
Stores the value 4.9 in that space (variable)
Echoes back this information
The prompt reappears
>> mag1 = 3.7 		overwrites “4.9” with “3.7”
Note
“=“ does not mean = in the mathematical sense.  Instead, it means “assign the number on the RHS to the variable on the LHS”
We can do math on the RHS, mixing numbers and variables

```




# Slide 10
```

Syntax
Lexical elements are combined using the set of rules known as “syntax”
I cdnuolt blveiee that I cluod aulacity uesdnatnrd what I was rdgnieg.
Important difference between human and programming languages is tolerance to syntax errors versus tolerance to spelling/grammar errors

```




# Slide 11
```

Examples of Syntax Errors
Usually / often your code will not run if you make a syntax error:
>> x=10;				defined my variable x and assigned it a value of 10
>> y=cos(x			trying to compute cos(x) and assign it to variable y
??? y=cos(x			Correct: y = cos(x)
|
Error: Expression or statement is incorrect--possibly unbalanced (, {, or [.
>> y=2x				trying to compute “2 times x” and assign it to “y”
??? y=2x				Correct: y = 2*x (spaces around = don’t matter)
|
Error: Unexpected MATLAB expression.

```




# Slide 12
```

Syntax versus Semantics
When a program doesn’t work this can happen because:
SYNTAX is incorrect - e.g.,
>> distance = speed *
- multiplication (*) needs numbers or variables on both sides of *
b)	SEMANTICS are incorrect
>> distance = speed / time
- may or may not run but will certainly give you the wrong answer!!
The program you wrote is not the program you meant to write!

```




# Slide 13
```

Example of Semantics Error
mag1 =4.9;
mag2 =5.3;
if (mag1 < mag2)
max_mag = mag1;
else
max_mag = mag2;
end
Here’s a code snippet for finding the largest of 2 earthquakes.
What is wrong?

```




# Slide 14
```

Wrap Up
Steps in problem solving
1. state problem clearly
2. define the input/output
3. write down algorithm by hand: ie., think the problem through
4. code in MATLAB
5. test, test, test…
Underlying structure of MATLAB syntax
- building blocks: names, operators, special characters
Syntax versus semantics
- syntax errors are about bugs in step 4 above
- semantics errors usually result from skipping step 3

```


<!-- #region -->

# Slide 15
```

Lab Overview
become familiar with MATLAB environment
load, plot and save data
try some simple operations
write MATLAB scripts
a) pair programming
b) need either an account, or your own version of MATLAB
c) turn in requested file on Canvas (not graded but will use later in term)

```





<img src="media\week02_Class1_SyntaxOverview_postclass-slide_15-003.png">


<img src="media\week02_Class1_SyntaxOverview_postclass-slide_15-004.png">

<!-- #endregion -->
