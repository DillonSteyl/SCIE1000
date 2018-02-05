# Introduction to Arrays (3) - Looping Through Arrays

Because of the convenient way that arrays are indexed, we can perform many useful functions by combining loops and arrays. For instance, we can use a loop to access each element of the array individually, and change each entry's value as we please. 

Imagine we want to create an array containing the first 1000 even numbers (starting from 0). It would be *very* tedious to do this manually. Instead, we could use a loop to make things easier! The following program shows how this would be done for the first 50 even numbers.

**Note:** we use a new function in the following program, `zeros(n)`. This function simply creates an array of size `n`, filled with zeros.

```python
even_numbers = zeros(50) # array of zeros
i = 0
while i < 50:
    even_numbers[i] = 2*i
    i = i + 1
print(even_numbers)
```

Note that we do this by simply doubling the index, which increases by 1 for each sequential entry. 
The output is:

```
[  0.   2.   4.   6.   8.  10.  12.  14.  16.  18.  20.  22.  24.  26.  28.
  30.  32.  34.  36.  38.  40.  42.  44.  46.  48.  50.  52.  54.  56.  58.
  60.  62.  64.  66.  68.  70.  72.  74.  76.  78.  80.  82.  84.  86.  88.
  90.  92.  94.  96.  98.]
```

**Task:** Write a while loop to fill the array `squares` with the first 10 square numbers (use a similar strategy to above - perform an operation on the index variable `i`)

# Solution
```python
from pylab import *

squares = zeros(10)
i = 0
# while loop here:
while i < 10:
    squares[i] = i**2
    i = i + 1
```
