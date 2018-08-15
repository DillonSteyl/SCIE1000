## Arrays and Loops

Loops can also be used to fill in arrays based on values already in the array. This can be useful when you can only calculate the next value, unlike some equations where you can calculate any value (linear, exponential, quadratic, etc). Here is a simple example:


```
A = zeros(int(12))
A[0] = 10


i = 1
while i<12:
    A[i] = (A[i-1]-4)*2
    i = i + 1

print(A)
```
The output is:

```
[  10.   12.   16.   24.   40.   72.  136.  264.  520. 1032. 2056. 4104.]

```

So the array starts off with its first value as 10, and the rest of its values as 0. For the first iteration of the while loop, it uses the previous array value (10) to calculate the next array value (12). For the second iteration, it uses the value 12 to calculate the value 16. It continues this for the rest of the loop. 

It does this by using `A[i-1]`, which refers to the previous value calculated. Also note that the loop will only iterate 11 times. It starts at 1, and ends at 11. This is because the first value has already been filled in. 

**Task:**

You want to calculate the height of your plant throughout the year. The person who sold you the plant said the plant's growth will follow this equation, with `H(i)` being the height (cm) of the plant at month `i`:

`H(i+1) = H(i)*(1.2+0.4*sin(2*pi*i/4))`, rounded to 0 decimal places. 

Given that the plant will start at a height of 10cm (H(0) = 10), write a program that will calculate the plant's height for 12 months. Store it in an array `Height`. Do not print anything.

**Hint:** Recall, to access and edit elements in an array, you must use square brackets `[]`.

## Solution

```
from pylab import *

A = zeros(int(12))
A[0] = 10

i = 1
while i<12:
    A[i] = round(A[i-1]*(1.2+0.4*sin(2*pi*i/4)))
    i = i + 1
```


