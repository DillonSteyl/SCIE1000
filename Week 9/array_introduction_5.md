# Introduction to Arrays(5) - Array functions

When we create arrays, it can be tedius to type out every individual element of an array. Imagine if you wanted an array of values 0 to 1000. No one wants to type that! Luckily, for particular number patterns, there are python functions that will create the arrays for us.

This first is 'arange(start, stop, step)', that will make an array with numbers starting from 'start', endign at 'stop' (but not including 'stop'), with a step size of 'step'. Here's how it works:

```python
A = arange(0,10,0.5)
print(primes)
```
The output is:

```
[0. 0.5 1. 1.5 2. 2.5 3. 3.5 4. 4.5 5. 5.5 6. 6.5 7. 7.5 8. 8.5
 9. 9.5]
```


Notice how the array starts at 0, goes all the way up to 10 but doesn't include it, with a step size of 0.5. **Note:** Arange likes to put periods at the end of integers when it prints them. Don't worry about it!

Now that we can access individual elements in an array, we can learn how to change them. It works the same way variables are changed, except instead of the variable name you need to write the array name and the index in square brackets. Take a look at the following example:

```python
primes = array([354,3,5,7,11])
primes[0] = 2
print(primes)
```
The output is:

```
[2 3 5 7 11]
```

So the format is `arrayname[index] = new value`. Recall, array indexing starts at 0, so primes[0] refers to the first element in the primes array, primes[1] refers to the second element in the array, and so on.


**Task:** Modify this program so that it correctly prints the first 10 squares after it prints the squares incorrectly. 

## Solution
```python
from pylab import *

squares = array([0, 4, 9, 15, 25, 36, 49, 64, 81, 121])
print(squares)
squares[0] = 1
squares[3] = 16
squares[9] = 100
print(squares)
```

