---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
---

# Week 2:  Steps In Problem Solving & Some MATLAB Basics

## Concepts:

* Review variable assignment, structural elements of MATLAB
* Identify 6 types of action involved in algorithm
* Rreview of arrays (link to lab 1)
* Use built-in functions (link to lab 1)

### Reading for next week:
>For Tues: pg. 35-40 (review), 40-60, 266-267 <br>
>There will be a quiz on the material on pages 35-60. <br>
>For lab:pg. 443-456 <br>
For Thurs: pg. 60-69

### TA hours, EOS-Main 203 
>Make sure to note these carefully! <br>
>Thurs (wks 3,4,5,6,8,9,10,11): 9:30am – 10:30am <br>
>Mon (wks 7,10 only): 11:00am – noon <br>

**Lab due on Canvas by 4pm Friday**

## Types of Action in Algorithm
Use example from last time, maximum earthquake magnitude

Types of Actions:

* Input
* Operation
* Selection
* Repetition
* Output
* Stop

```
1.  read mag1
2.  read mag2
3.  Is mag2 > mag1  ?
3a.	YES:  biggest = mag2
3b.	NO:   biggest = mag1
4.  read mag3
5.  Is mag3 > biggest  ?
5a.	YES:  biggest = mag3
5b.	NO:    don’t need to update biggest

Loop over 4-5b until reach end of list
write out biggest
```

## Case Sensitivity

Question: what happens when…

```matlab
>> IF = 2;
>> if = 2;
??? if = 2;
       |
Error: The expression to the left of the equals sign is not a valid target for an assignment.
```

What went wrong?  I tried to use ```if``` as a variable name, BUT
```if``` is a reserved word so I cannot redefine it.
Because MATLAB is case sensitive I AM allowed to do this.
However, it is very bad programming practice

## Review from Lab

Variable Assignment <br>
Worksheet A: What is the output of this code snipped?
Worksheet B:  Identify variables etc

```matlab
% radius of Earth in km
radius = 6371;
area = 4*pi*radius*radius;
% radius of Moon in km
radius = 1739;
area = 4*pi*radius*radius
```

```pi``` in MATLAB returns the value of $\pi$ (3.1415...) <br>

```matlab
pi =  4*atan(1) and imag(log(-1))
```

## Review from Lab cont'd

Worksheet C & D:
Arrays in MATLAB (see next week)

```matlab
>> load lab1
>> whos
Name                 Size            Bytes  Class     Attributes
temperature      12213x1             97704  double
time             12213x1             97704  double

Temperature 12213 measurements
```

This is an array, dimensions 12213 by 1 <br>
A big advantage of MATLAB is the ease of dealing with vectors and matrices
>Recall:  In lab 1 you loaded a file lab1.mat that contained 2 variables:

**Analogy: Think of a table / EXCEL file:** <br>

* Each VALUE in the table is defined by its POSITION (row #, col #) <br>
* Conversely each POSITION in the table (row #, col #) has associated with it a VALUE

## Arrays in MATLAB

Worksheet E <br>
Let’s look at e.g.,10 entries in a list of eq magnitudes:

```matlab
>> clear
>> mags = [4.2; 4.1; 4.1; 4.1; 4.3; 4.2; 4.3; 4.5; 4.0; 4.7];
>> whos
Name         Size            Bytes  Class     Attributes
mags         10x1                80  double
>> mags
mags =
4.2000
4.1000
4.1000
4.1000
4.3000
4.2000
4.3000
4.5000
4.0000
4.7000
```

<!-- #region -->

## Arrays and Plotting

```matlab
load lab1;
figure(1)
plot(time,temperature)
datetick('x',3)
```
What has happened to make the plot? <br>
\# of points in time and temperature MUST be the same

<img src="media\week02_Class2_AlgorithmSteps-slide_6-000.png" height=300>

<!-- #endregion -->

<!-- #region -->

## Arrays and Plotting cont'd

What does this do?

```matlab
>> plot(time,temperature,time(5149:7308),temperature(5149:7308),....,time(9493:11700),temperature(9493:11700))

```

<img src="media\week02_Class2_AlgorithmSteps-slide_7-001.png" height=300>

<!-- #endregion -->

<!-- #region -->

## Defining new arrays

```matlab
>> plot(time,temperature,time(5149:7308),temperature(5149:7308),....
time(9493:11700),temperature(9493:11700)
```

This is error prone if there are many commands involving the winter or summer parts of the time and temperature arrays.  So we defined new arrays:

```matlab
wtime = time(5149:7308);
wtemp = temperature(5149:7308);
stime = time(9493:11700);
stemp = temperature(9493:11700);
```

Programming Style Hint:
Use variable names that are easy to understand and try to keep them short
e.g. wtemp vs. winter_temperature
See text p. 28-29 for Programming style guidelines & common pitfalls

<img src="media\week02_Class2_AlgorithmSteps-slide_8-002.png" height=300>

<!-- #endregion -->

## Using Built-In Functions

Worksheet F:

```matlab
y3 = max(mags(3:8))
```

Steps:

* Select a subset of mag that includes the 3rd thru 8th values
* Calculate the maximum of these using the built-in function ```max```
* Assign the output to a variable called ```y3```
* No semi-colon so echo the value of ```y3``` to the screen

```{note}
Advantage of MATLAB:
many built-in functions
```

## Why Arrays and Built-In Functions are Slick:

### Finding the Largest Earthquake <br>

My algorithm that we could code up explicitly (i.e. write code that looks pretty much like this set of instructions):

```
0.  load data file with magnitudes
1.  read mag1
2.  read mag2
3.  Is mag2 > mag1  ?
3a.	YES:  biggest = mag2
3b.	NO:   biggest = mag1
4.  read mag3
5.  Is mag3 > biggest  ?
5a.	YES:  biggest = mag3
5b.	NO:    don’t need to update biggest
6. Loop over 4-5b until reach end of list
7. Write out biggest
```

BUT we’ve learned we can load arrays and use them as the input to built-in functions in MATLAB: <br>
So this can be coded in 2 lines! <br>

```matlab
% load array of earthquake magnitudes
load mags;
% find biggest and echo to screen
biggest = max(mags)

