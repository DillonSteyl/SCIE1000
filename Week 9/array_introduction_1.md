# Introduction to Arrays (1) - Creating Arrays

Last week, we learned how to plot graphs - to do this, we used the `arange` function to create an *array* which stored x-coordinates.  Apart from this, we have only used Python to store individual values in variables. *Arrays* allow multiple values to be stored in one variable.  Here's a simple example of how you might use an array in Python:

```python
# Create an array containing the first 7 numbers in the fibonnaci sequence
fib = array([0,1,1,2,3,5,8])
print("The first 7 numbers in the fibonnaci sequence are:", fib)
```

The output of running this program is given below:
```
The first 7 numbers in the fibonnaci sequence are: [0 1 1 2 3 5 8]
```

Some important notes:
* Just like any other variable, use meaningful names for your arrays.
* Python uses square brackets to distinguish arrays from other variables.
* Create an array using the `array(...)` function as shown above. Seperate the entries in the array by commas.
* Printing an array will display all of its contents.
* The *size* of an array is simply how many values it holds, so the `size` of the `fib` array is 7.

**Task:** Create an array called *squares* which contains the first 5 square numbers (1, 4, 9, 16, 25).

## Solution
```python
from pylab import *

squares = array([1, 4, 9, 16, 25])
```
