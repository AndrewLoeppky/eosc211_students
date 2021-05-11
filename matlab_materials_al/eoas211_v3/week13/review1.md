# Instructions

This review sheet is intended to help you prepare for the exam. The best
way to study is to work the examples through by hand, and then check
your answers by writing code snippets in MATLAB.

## Dimensions and element-wise versus matrix algebra

Given a = `[1 2; 3 -1; 0 1]`, `b = [3: -2: -2]'`, `c = ones(3)`

What are the dimensions of

1.  `a`

2.  `b`

3.  `c`

4.  `b'*a`

5.  `a.^2`

6.  `a*a'`

7.  `a^2`

Check by entering `  a, b, c `  into MATLAB.

## More math

Given

    A=[1 5 3 0 1]; 
    B=[0 5 6 0 1];
    C=A./B + 4

What is the result contained in C?

## Function practice

Write a function `transp` that will take as input a 2-D array \(A\), and
return the array \(B\) where \(B(i,j)\) = \(A(j,i)\). Do not use a
built-in MATLAB function.

Add a check to the function code that will exit the function with an
error message if \(A\) is not a 2-D array.

## Code-writing practice

The Fibonacci sequence goes 0,1,1,2,3,5,... where each number is the sum
of the previous 2 numbers. How many terms in the sequence are less than
5000? (write code, pseudo-code, or a flowchart)

## Precedence

Given `  a = 3 `. What is

1.  `  x= [2^a `+`a*2`+`1, a^sum([2:-1:0,-4])]`

2.  `  x= a^3-2^a `

## Writing to a string (also practice with repetition)

You want to set up a series of \(N\) data files with names `file01.dat`,
`file02.dat`, `fileN.dat`. Write a code snippet that will generate these
file names and write them to an array. Note that filenames for integers
less than 10 need an extra zero – i.e., make a string `file02.dat` not
`file 2.dat`. Assume you have less than 99 filenames. You can check your
code by adding a printf statement – do this to practice more with
fprintf. e.g., I wrote an fprintf statement that produces the following
output for N=11

    Filename 1 is file01.dat
    Filename 2 is file02.dat
    Filename 3 is file03.dat
    Filename 4 is file04.dat
    Filename 5 is file05.dat
    Filename 6 is file06.dat
    Filename 7 is file07.dat
    Filename 8 is file08.dat
    Filename 9 is file09.dat
    Filename 10 is file10.dat
    Filename 11 is file11.dat

## Opening and closing files

I have a file called `myfile.dat` and want to open it such that I can
write to it. Which, if any, of these statements works? (Why not, if they
don’t work).

1.  `fid1 = fopen(myfile.dat, 'r')`

2.  `fid2 = fopen(myfile.dat)`

3.  `fid3 = fopen(myfile.dat, 'w')`

Which if, any, could be fixed with one change? What is the change if so?

## Debugging

This code is supposed to sum all the values in y, stopping when the sum
is more than 12. It should print the last value of the sum (before the
sum reached a number greater than 12) to the screen. There are three
problems here, and one possible additional problem for general choices
of y – what are they?

    x=1:10;  
    y=2*x;
    sum=0;
    while (sum1 + y(i) < 12)
        sum1=sum1+y(i);
        i=i+1;
    end
    fprintf('Sum = %3.1f, i=%3d\n',sum1,i-1);

We want compute the vector `d=(a*b)/c` using element-wise arithmetic so
that length(d)=length(a). Fix the problems.

    a=1:3:30;
    b=sin(a);
    c=tan(a);
    d=a*b/c;
    plot(a,d);

## Bits ’n’ Bobs

If `r` is a row vector, length N, write code snippets to

1.  count the number of elements in `r` whose value is above the median
    value
    
    1.  using a loop
    
    2.  using logical indexing

2.  form an N by 2 matrix whose first column contains the circumference
    of circles with radii given by `r`, and whose second column contains
    the area of circles with radii given by `r`,
