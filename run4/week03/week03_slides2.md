# Review - Storing Information and Data Structures

## Last Class: Regular Indexing

### 1) Row - Comma - Column (RC Cola!)

```matlab
>> A = [101 102 103; 104 105 106]

A =

   101   102   103
   104   105   106

>> B = A(:,2)

B =

   102
   105
```

### 2) Linear Indexing
   
```matlab
>> C = A(1:4)

C =

   101   104   102   105
```

## Logical Indexing

It's also possible to index into an array using a **logical array** of the same size $\rightarrow$ *array of **logical** 1's and 0's*

```matlab
>> mag = [7.2 3.1 2.8 6.2];
>> ii = logical([1 1 0 0]);
>> mag(ii)

ans =

    7.2000    3.1000
```

Three ways to create a logical array:

### 1) Convert an array of ones and zeroes using the function ```logical()```

```matlab
>> logical([1 0 0 1])

ans =

  1×4 logical array

   1   0   0   1
```

### 2) Use a logical comparison (```==```, ```>```, ```<```, etc.) *more on this next week*

```matlab
>> mag = [7.2 3.1 2.8 6.2];
>> mask = mag > 5

mask =

  1×4 logical array

   1   0   0   1

>> mag(mask)

ans =

    7.2000    6.2000
```

Note, you can do all this on one line:

```matlab
>> mag(mag > 5)

ans =

    7.2000    6.2000
```

### 3) Use a function that produces a logical array, ex. ```isnan()```, ```isfinite()```, ```isequal()```, etc...

```matlab
>>> Data = [3, 5, NaN, 9, 8, Inf];

>> isfinite(Data)

ans =

  1×6 logical array

   1   1   0   1   1   0
```

```{note}
```NaN``` means "not a number" i.e. a missing value

```Inf``` means "infinity"
```

Logical indexing is very useful for choosing specific subsets of a large array.
