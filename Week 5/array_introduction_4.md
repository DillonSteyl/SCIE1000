# Introduction to Arrays(4) - Editing Arrays

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

