# Introduction to Arrays (6) - Looping Through Arrays

Because of the convenient way that arrays are indexed, we can perform many useful functions by combining loops and arrays. For instance, we can use a loop to access each element of the array individually, and change each entry's value as we please. 

The following is a simple example that could be replaced by code you learned in the past couple exercises, but it is important to understand this first before moving on to more complex examples:

```python
even_numbers = zeros(int(50))
i = 0
while i < 50:
    even_numbers[i] = i*2
    i = i + 1
print(even_numbers)
```

The aim of the program is to create an array filled with even numbers from 0 to 98. This works because `i` will start at 0 and go to 49. By multiplying `i` by 2, we get the even numbers from 0 to 98. Then, we use `i` to edit the correct element of the array. So first it changes the first element of the array to `0*2 = 0`. Then it changes the second element of the array to `1*2=2`, then the third element to `2*2=4`, and so on.

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
