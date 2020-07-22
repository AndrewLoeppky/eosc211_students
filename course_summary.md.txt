# EOSC 211 Summary

## Reading List and Learning Goals By Week

This is a summary of EOSC 211 as taught in 2018, with readings specified from "MATLAB: A Practical Introduction to Programming and Problem Solving" by Stormy Attaway.

## List of Missing or Unclear Course Material

* Week 3: reading list
* Week 4: learning goals, additional reading list(?)
* Week 6: reading list, formal list of learning goals, learning material for day 2
* Week 9: additional reading(?), learning goals, content for day 2
* Week 10: all lecture material, learning goals, reading list
* Week 12: everything (if applicable)
* Week 13: everything (if applicable)

## Week 1 / Syllabus

**Reading:**

* N/A

**Learning Goals:**

* Students will write computer programs to model and analyze data in the solid earth, atmospheric and oceanographic sciences
* Break problems into logical steps using flowcharts and pseudocode to specify algorithms: operation, repetition, decision, I/O, computer math
* Write and debug MATLAB computer programs to correctly implement algorithms; syntax, data structures, debugging strategies
* Modifying existing MATLAB computer programs using the elements of good programming style to make it more efficient, readable and documented for future use. Naming conventions, appropriate syntax, structures, modularization using functions, using built-in functions, code re-use, good documentation practices, vectorization of loop operations.
* Creating scientifically informative and visually appealing plots (scatter, time series, contours, multiple subplots, legends)

## Week 2

### Day 1

**Reading:**

* Pg 3-40, 75-80, 89-101, 557-564

**Learning Goals:**

* Steps in problem solving
* Syntax, underlying structure
* Syntax vs semantics

### Day 2

**Reading:**

* 35-40, 40-60, 266-267, 443-456, 60-69
  
**Learning Goals:**

* Variable assignment
* 6 types of action in algorithms
* preview of arrays
* use built-in functions

### Lab

**Learning Goals:**

* Log on to MATLAB
* Make a folder in a directory, same directory as the_file.m
* Load and save data
* initialize and use variables
* make (x,y) plots of data, play with colours, etc.
* edit, save and run a MATLAB script
* comment your code

**Lab Content Summary:**

* Radius of earth, ```pi``` as a built in function
* Air temperature time series (linear indexing)
* optional arguments for ```plot()``` ie colour, shape, etc
* ```min()``` and ```max()``` functions

## Week 3

### Day 1

**Reading:** ???

**Learning Goals:**

* data structures: arrays, strings, doubles/floats, char
* storing data in memory, declaring variables
* regular indexing into arrays, more complicated indexing
* distinguish between indices and stored values
* complex data structures: cell arrays and structures
* distinguish between cells and cell content

### Day 2

**Reading:** ???

**Learning Goals:**

* Review day 1
* regular indexing (row, column)
* linear indexing
* logical indexing ```A = logical([1 1 0 1])```
* logical indexing using comparison operator ```A = B(B > 5)```

### Lab

**Learning Goals:** 

* Download rasdter image from web and import into MATLAB
* Describe the parent/child structure in handle graphics
* Write short snippets of code that will perform various actions
> * display raw images and change the colormap
> * retrieve subsections of an array
> * perform mathematical operations on a vector
> * display a contour plot
> * use handles to get and set property/value pairs to customize graphics

* Build up a larger program by modifying a "starter" program
* Write a short program that performs specified actions

**Lab Content Summary:**

* ```[A, CMAP] = imread('the_file.png')```
* ```image(A)```
* ...
* Change colormaps, axis labels
* Query the size of an array
* Side note on O.O. programming
* make a colorbar and change its color attribute
* make a contour plot
* follow specific instructions on lab structure, filename

## Week 4

### Day 1

**Reading:** ??

**Learning Goals:**

* do quiz, go over last weeks lab
* talk about computer math (no slides)
* data types: int, double, logical, etc.

### Day 2

**Reading:** ??

**Learning Goals:**

* code is read top to bottom
* input $\rightarrow$ definition $\rightarrow$ calculation $\rightarrow$ output
* debugger

### Lab

**Reading:**

* Ch2, pg 11-28
* Ch3, pg 52-68

**Learning Goals:**

* Write a program with input $\rightarrow$ definition $\rightarrow$ calculation $\rightarrow$ output
* Write a complex program by modifying a simple program
* learn some technical features of matlab

>* built-in functions
>* perform simple math on vectors and scalars

* Evaluate a built in function over a range of values using ```meshgrid```
* plot output of a built-in function with ```legend``` and ```subplot```
* adjust axis limits using ```axis``` and ```xlim```

**Lab Content Summary:**

* Define variables in Clausius-Klapeyron equation
* Tips on programming style

>* watch your units
>* choose judicious variable names
>* input, variables, calc, output
>* comment your code!

* Do vector calculations with ```./``` and ```.*```
* Follow specific instructions ie "hand in a file called "lab4.m"

## Week 5

### Day 1

**Reading:**

* First 10 pages of chapter 11

**Learning Goals:**

* Go over last weeks lab
* DRY (dont repeat yourself)
* Do "selection exercise" (selectionExercise.pdf)

### Day 2

**Reading:** ???

**Learning Goals:**

* Convert from lat-lon to (x,y) (spherical to cartesian)

### Lab

**Learning Goals:**

* Create a large program by modifying a small one
* Create algorithms using selections (if/else)
* Implement if/else statements
* Begin using formal debugging procedures
* Learn about argument checking for input data
* Understand latitude and longitude conversion to cartesian

**Lab Content Summary:**

* Write a program to anaalyze topographic slopes
* pick a point on a digital elevation model and output the slope (east facing, west facing, or flat)
* Break problem into parts. Solve one special case then generalize
* Modify/fix existing code, then add your own
* Handle "bad" input data
* Implement an equation do calculate the slope between two discrete points
* Output results to screen
* Handle (literal) edge cases, finding the slope at $x=0$

## Week 6

### Day 1

**Reading:** ???

**Learning Goals:** ??

### Day 2

[DNE]

### Lab

**Learning Goals:**

* Develop algorithms involving loops
* Carry out a top-down design process
* modularize code separating the algorithm from input/output statements

**Lab Content Summary:**

* Preamble - smoothing a timeseries using a running mean
* Math for running mean of window size $L$ where $L$ is *odd*

$$
z_i = \frac{1}{L}\sum_{k=-W}^W x_{i+k}
$$
where
$$
W=\frac{L-1}{2}
$$

* First, create a function that loops through the time series and performs some arbitrary operation
* Then, develop the running mean function inside the loop
* Finally, write code to handle special cases (NaN's, edges, etc)
* Repeat with *running median*
  >why? mean averages over bad data and thus includes it, median will usually only select good data
* Write code that will pass a *test*

## Week 7

(This week consists of midterm practice and the midterm. No reading or learning material other than the practice MT)

## Week 8

### Day 1

**Reading:**

* Pg 101-113, 193-207, 341-346

**Learning Goals:**

* Defining a function
* Using a function -- calling, returning, ```help```
* Pass-by-value vs. pass-by-reference (positional vs keyword args)

### Day 2

**Reading:** None?

**Learning Goals:**

* Hand back midterms
* Review day 1
* Logical indexing review
* Introduce assignment 2 (check? should be assignment 1?)

### Lab

**Learning Goals:**

* Turn previous running mean code into a cunction, implement checks
* CODE: function definition and help lines
* CODE: subfunctions
* CODE: function calls from main script
* CODE: useful matlabl functions: ```error```, ```rem```, ```size```

**Lab Content Summary:**

* Re-write lab 6 code as a function
* Screen bad inputs with a subfunction

## Week 9

### Day 1

**Reading:**

* URL posted in week09_formatting.pdf

**Learning Goals:**

* Formatted output
* Opening/closing files

### Day 2

(DNE)

### Lab

**Learning Goals:**

* Output numbers and text using formatted ```printf```
* Open and close files for writing
* Practice with logical indexing, loops

**Lab Content Summary:**

* Convert float/int to string so you can print it to the screen or on a plot or something
* Print ```pi``` using different formatting tags, variable precision
* Load the file about student commute statistics
* Use formatted text to label plots and make them pretty
* Output statistics into a table and display it
* Note: This lab and future ones are marked on *coding style*

## Week 10

### Day 1

(DNE)

### Day 2

(DNE)

### Lab

**Learning Goals:**

* Read and understand someone else's code
* Use the 5 methods of finding errors
* Use the debugger to step through code
* Solve a useful problem in earth sciences

**Lab Content Summary:**

* ```set``` (breakpoint), ```run```, ```continue```
* Debug existing code
* Use skills from lab 5 (lat/lon to cartesian)
* Plot ocean currents

## Week 11

### Day 1

**Reading:** none

**Learning Goals:**

* Interpolate data a number of ways
>* Nearest neighbour
>* Linear
>* Cubic splines

### Day 2

**Reading:** none

**Learning Goals:**

* Brief assignment 2

### Lab

**Learning Goals:**

* Understand and use different interpolation algorithms
* Gain more familiarity with loops and vectorization
* Use MATLAB built in functions like ```interp2```
* Gain experience with complex data sets
* Learn to scavenge code from other code

**Lab Content Summary:** N/A

## Week 12

The only content I have here is two worksheets. Presumably this is meant for review and/or class time to work on assignment 2

## Week 13

Review for exam, several practice worksheets provided.