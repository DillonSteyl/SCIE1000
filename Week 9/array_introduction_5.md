# Introduction to Arrays(5) - Array functions

When we create arrays, it can be tedius to type out every individual element of an array. Imagine if you wanted an array of values 0 to 1000. No one wants to type that! Luckily, for particular number patterns, there are python functions that will create the arrays for us.

This first is `arange(start, stop, step)`, that will make an array with numbers starting from `start`, ending at `stop` (but not including `stop`), with a step size of `step`. Here's how it works:

```python
A = arange(0,10,0.5)
print(A)
```
The output is:

```
[0. 0.5 1. 1.5 2. 2.5 3. 3.5 4. 4.5 5. 5.5 6. 6.5 7. 7.5 8. 8.5 9. 9.5]
```

Notice how the array starts at 0, goes all the way up to 10 (but doesn't include it), with a step size of 0.5. (Arange sometimes likes to put periods at the end of integers when it prints them. Don't worry about it!)

If your step size is 1, you can leave out the step size value altogether:

```python
A = arange(2,10)
print(A)
```
The output is:

```
[2 3 4 5 6 7 8 9]
```
Again, the array starts at 2, goes all the way up to 10, but doesn't include it. You can also make an array full of zeroes! To do this use the functions: `zeros(int(length))`, where length is how many elements you want in your array. Pay attention to two things here. Firstly, the spelling of `zeros`; there is only one `e`. And secondly, the `int` function. The `int` function will make sure that the `zeros` function behaves properly, otherwise it will sometimes cause errors. Here's how it works:

```python
z = zeros(int(5))
print(z)
```
The output is:

```
[0 0 0 0 0]
```

It may not seem useful at first to have an array full of zeroes, but in future tutorials and exercises, we will want to create an array and then fill in the values later. For this, we will use the zeros function.


**Task:** Make three arrays. First, make an array that goes from 3 to 8 (including 8), with a step size of 0.1. Second, make an array from -3 to 3 (including 3) with a step size of 1. And lastly, ask for input from the user and make an array full of zeroes of that length.

Finally, print all three arrays with just one print statement and no other text. Make sure to name the arrays as array1, array2, array3, respectively.

## Solution
```python
from pylab import *

array1 = arange(3,8.1,0.1)
array2 = arange(-3,3.1)

length = float(input("Number of zeroes: "))

array3 = zeros(int(length))

print(array1, array2, array3)

```

