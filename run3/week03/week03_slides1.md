# Week 3 - Storing Information & Data Structures

## Tuesday Class: Outline

* Simple data structures: arrays, string, doubles/floats, characters
* Storing data in memory: variable declaration, colon operator
* Regular indexing into arrays (RC), more complicated indexing
* Distinguish between array indices and stored values
* Complex data structures: cell arrays and structures
* Distinguish between cells/fields

## Quiz \# 1

## In EOAS We Often Work With Many Measurements (i.e. lots of data)

**Example**
* West coast of VI 2013
* Transect: about 70km
* Measurements
    * every 1m vertical
    * every 1km lateral
* Avg depth: 90m
* Temperature, Salinity, Oxygen, Pressure Latitude, Longitude, Depth

<img src="media1/week03_class1_datastructures-slide3_001.png">

90 x 70 = 6300 measurements per variable per transect

7 variables and 75 transects, so 6300 x 7 x 75 = 3,307,500 measurements!

**How do you organize your data?**

## Primitive Data Structures: **Arrays**

**Example, cont'd:**

 The simplest way to store large amounts of data is in *arrays*. Consider the salinity measurements from the previous example - to plot this data, we require three arrays:

<img src="media1\week03_class1_datastructures-slide4_001.png">

Arrays are like tables that store values, with one value stored in each location, much like a spreadsheet in Excel.

They can be:

* 1 Dimensional (row or column)
* 2 Dimensional (square/rectangle)
* 3 Dimensional (cube)
* N Dimensional (hard to visualize)

**In Matlab**

```matlab
  >> whos
   Name     Size       Bytes     Class     Attributes
   depth    251x1       2008    double
   distance   1x75       600    double
   saln     251x75    150600    double
   temp     251x75    150600    double

  >>
```

## Creating Numeric Arrays

* Arrays are usually denoted using **square brackets** ```[]```
* When creating an array, you usually assign it to a **variable name** using the ```=``` symbol (see last week)
* Use a **semi-colon** (```;```) to separate rows, and a **comma** (```,```) or **white space** to separate columns

**Row Vector**

```matlab
>> x = [5 8 6 9]

x =

     5     8     6     9
```

**Column Vector**

```matlab
>> y = [5; 9; 1; 3]

y =

     5
     9
     1
     3
```

**2x2 Array**

```matlab
>> z = [1, 2; 3, 4]

z =

     1     2
     3     4
```

**This doesn't work, why not?**

```matlab
>> a = [4 9 7; 3 9]
```

Use the **colon** (```:```) operator to create numeric series. This is very useful!

**Integers from 1 to 5**
```matlab
>> x = 1:5

x =

     1     2     3     4     5
```

**From -5 to -4.4, with stepsize 0.2**

```matlab
>> y = [-5:0.2:-4.4]

y =

   -5.0000   -4.8000   -4.6000   -4.4000
```

**From 3 to -6, stepsize -2**

```matlab
>> z = 3:-2:-6

z =

     3     1    -1    -3    -5
```

## Creating Character Arrays

* Character arrays are similar to numeric arrays, but contain characters
* Characters are denoted using single quotes: ```'a' 'E'```  'v'
  * "Space" is a character and has to be explicitly inserted
  * Row vector of characters is known as a "string" of characters
  
```matlab
>> x = 'hello'

x =

    'hello'

>> y = ['h' 'ell' 'o']

y =

    'hello'

>> z = ['hello' ' jello']

z =

    'hello jello'

>> xyz = ['hello'; 'jello']

xyz =

  2×5 char array

    'hello'
    'jello'
```

* ```x``` and ```y``` are identical
* ```x, y``` and ```z``` are all 1D character arrays, or simply "strings"
* ```xyz``` is a 2D character array

## Indexing Into Arrays

* For accessing a subset of an array
* Think **RC** - row, column
* Regular indexing always uses the convention (row, column)
  * i.e. "row-comma-column"

### Example Given that the array ```sal``` looks like this:

<img src="media1\week03_class1_datastructures-slide6_001.png">

Here the colon (```:```) operator means "all", and the reserved word ```end``` refers to the last element

<img src="media1\week03_class1_datastructures-slide6_002.png" height=400>

## Worksheet

Please find your groups

Start on exercises 1 and 2

## Complex Data Structures

Arrays are limiting because they only store one type of data at a time and because they must have regular shapes (i.e. rectangles). There are two types of data structures that cna accommodate more than one type:

### Cell Arrays

Arrays of "cells" where each cell may contain any simple data structure (i.e. a numeric or character array). Use curly braces ```{}``` to denote cell arrays

```matlab
>> Var1 = {'Farmer John'; [5 6; 7 8]; [1:4]}

Var1 =

  3×1 cell array

    {'Farmer John'}
    {2×2 double   }
    {1×4 double   }
```

### Structures

Structures are variables that contain a series of fields, each holding a simple data structure. Use "dot notation" to access

```matlab
>> Client.name = 'Farmer John';
>> Client.age = 39;
>> Client.assets = [326, 254, 784];
>> Client

  struct with fields:

      name: 'Farmer John'
       age: 39
    assets: [326 254 784]

>> Client.name

ans = 

Farmer John
```

## Practice

Practice with structures and cell arrays

Worksheet exercise 3 and this week's lab

## Cell Arrays: A Practical Example

Go back to our example of last year's Vancouver island cruise. Say the cruise consisted of 12 individual legs (leg 3 is the one we looked at earlier), each measuring temperature $T$, salinity $S$, distance $x$ and depth $z$

<img src="media1\week03_class1_datastructures-slide11_001.png">

**Problem:** What is an efficient way to store $T$, $S$, $x$, and $z$ for each leg?

**Solution:** You do NOT need 12 x 4 = 48 variables! Instead, create four cell arrays, each with 12 cells

```matlab
>> whos
  Name        Size      Bytes       Class
  
  depth       1x12      25440       cell
  distance    1x12      8544        cell
  saln        1x12      1808544     cell
  tempr       1x12      1808544     cell
```

*Notice the "class" on the right*

## More Practice To Try On Your Own

### Question 1

Given that the array ```sal``` looks like this:

<img src="media1\week03_class1_datastructures-slide12_001.png">

How could you create *this* array:

<img src="media1\week03_class1_datastructures-slide12_002.png">

...using only one line of code?

### Question 2

Given ```x=1:2:10``` is stored in memory, what do you think the following code will produce?

```matlab
z = sal(1,x)
```
