# Arrays and Loops (1) - Looping Through Arrays

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

The aim of the program is to create an array filled with even numbers from 0 to 98. This works because `i` will start at 0 and go to 49. By multiplying `i` by 2, we get the even numbers from 0 to 98. Then, we use `i` to edit the correct element of the array. So first it changes the first element of the array to `0*2 = 0`, then it changes the second element of the array to `1*2=2`, then the third element to `2*2=4`, and so on.

The output is:

```
[  0.   2.   4.   6.   8.  10.  12.  14.  16.  18.  20.  22.  24.  26.  28.
  30.  32.  34.  36.  38.  40.  42.  44.  46.  48.  50.  52.  54.  56.  58.
  60.  62.  64.  66.  68.  70.  72.  74.  76.  78.  80.  82.  84.  86.  88.
  90.  92.  94.  96.  98.]
```

The reason we may want to use a loop instead of a python function is because the value that is being updated might be too complex to represent with just an equation. For example, the following program will make an array where the ith element is equal to 1 if sin(i) is greater than 0, and -1 otherwise:

```python
values = zeros(int(20))
i = 0
while i < 20:
    if sin(i)>0:
        values[i] = 1
    else:
        values[i] = -1
    i = i + 1
print(values)
```
The output is:
```
[-1.  1.  1.  1. -1. -1. -1.  1.  1.  1. -1. -1. -1.  1.  1.  1. -1. -1. -1.  1.]
```

**Task:** You are given two arrays, and we want to compare them. You must create a new array such that the element at index `i` is equal to 3 if the ith index in the first array has a larger value than element `i` of the second array, 1 if the ith index of the second array has a larger value, and 2 if both the values are equal. Name the array `win_loss_draw`. 

To recap, the value is 3 if array1's element is bigger, 1 is array2's element is bigger, and 2 if they are equal. For example, consider the following case:

```python
array1 = array([45,63,27])
array2 = array([100,2,27])
```

Here, we would want `win_loss_draw` to store the following values: `[1,3,2]`.

**Hint:** Both arrays have a length of 30.

# Solution
```python
from pylab import *

array1 = array([1,43,7,12,3,9,2,23,4,5,6,2,3,65,7,43,2,3,4,5,67,8,3,2,345,456,8,2,21,34])
array2 = array([123,43,6467,12,234,68,2,4,5,5,5,23,543,4576,8678,4,2,3,4,34,53,4,4,4,68,8,8,21,5,67])
win_loss_draw = zeros(int(30))

i = 0
while i<30:
    if array1[i]>array2[i]:
        win_loss_draw[i] = 3
    elif array1[i]<array2[i]:
        win_loss_draw[i] = 1
    else:
        win_loss_draw[i] = 2

    i = i + 1
    
```
