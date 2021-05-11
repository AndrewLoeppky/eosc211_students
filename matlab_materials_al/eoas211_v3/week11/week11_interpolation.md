---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.1-dev
---


# Slide 0
```

Week 11:  What and When
Today (Tues): code / background for this week’s lab:  Interpolating data sets.
Thurs: background and worksheet for assignment 2.  I will post assignment 2 on Tuesday.  It is due Wednesday November 28, 4pm.
No new MATLAB this week with exception of using built-in interpolation functions.  Lots of review / practice.
This week (week 11) is the last week with a lab that must be turned in.  During weeks 12 and 13 you can use the lab times to work on assignment 2.  There will be TAs in the lab but no additional TA hours those weeks.

```




# Slide 1
```

Common problems in data analysis are
Missing data:  want to fill in gaps
Unevenly-spaced data:  would like evenly spaced data
Differently spaced data in two data sets:  want to compare data from same time, place
Week 11:  Interpolating Data
x1
x2
x3
x4
x5
x1
x2
x4
x3
x5
x6
x1
x2
x4
x3
x5
x6
X’1
X’2
X’4
X’3
X’5
X’6
This requires estimating data at locations or times where we don’t have a measurement

```




# Slide 2
```

Same underlying issue: want to fill in the gaps or re-grid onto an even sampling interval!
One way to handle this is  BINNING your data and then taking the mean / median / mode in each bin.
This is not always practical since don’t always have many repeat or nearby measurements
Week 11:  Interpolating Data
INTERPOLATION:  		Estimating data between some known measurement points
Done all the time, care needed
EXTRAPOLATION:  	Estimating data beyond the end of your measurement set
This is VERY dangerous, and should be avoided
Why interpolate or re-grid data?
Comparing / overlaying multiple data sets (maps especially)
Create evenly spaced data so we can use our running-mean code for example
If we have lots of observations in one time interval and few in another any statistics will be biased toward the time period w/ more observations - want evenly gridded data
Doing spectral analysis (fourier transforms etc)

```




# Slide 3
```

x
xnew
x1
x2
x4
x3
x5
x6
xnew1
xnew2
xnew3
xnew4
xnew5
xnew6
Our new x-axis has an even spacing:   = xnew(j+1) - xnew(j)
Our original x-axis has a uneven spacing of data points
How to do this?  The first thing is to define a new, evenly spaced x-axis:
Next, we want to estimate our quantity of interest, y, (e.g. temperature) at our new points, xnew.
There are many ways to do this………..

```




# Slide 4
```

worksheet

```




# Slide 5
```

x
xnew
x1, T1
X2, T2
x4 ,T4
X3, T3
x5 ,T5
x6 ,T6
xnew1
xnew2
xnew3
xnew4
xnew5
xnew6
Let’s say our original measurements are temperature, T, versus distance, x
We could estimate the temperature at each of our new points, xnew(j) by assigning
The value of temp at the nearest point x(i) in the original time series,
e.g., x3 is closest to xnew3, so we could put     Temperature(xnew3) = T3
Name:	nearest neighbor interpolation
Advantage:	fast
Disadvantage:	produces a “step-like” function, i.e., discontinuous
Temp

```




# Slide 6
```

x
xnew
x1, T1
X2, T2
x4 ,T4
X3, T3
x5 ,T5
x6 ,T6
xnew1
xnew2
xnew3
xnew4
xnew5
xnew6
Temp
We could average the values of temperature at the two points x3 and x4
Not so great, but …..
We could add a percentage of the difference T4-T3 to the value T3, and the % would be based on the fractional distance xnew3 is toward x4 from x3
Name:	linear interpolation
Advantage:	(1) still pretty fast, (2) produces continuous function
Disadvantage:	“corners” at data points, discontinuous first derivative

```




# Slide 7
```

x
xnew
x1, T1
X2, T2
x4 ,T4
X3, T3
x5 ,T5
x6 ,T6
xnew1
xnew2
xnew3
xnew4
xnew5
xnew6
Let’s say our original measurements are temperature, T, versus distance, x
Temp
We might want our estimates to be more smoothly varying and fit a polynomial.
A better version of this approach involves the use of functions called splines.
Name:  	cubic splines
Advantage:	smooth function, continuous second derivative
Disadvantage: 	slower (not big deal), can produce “overshoots” in large data gaps

```




# Slide 8
```

Run demoweek11_tues

```

