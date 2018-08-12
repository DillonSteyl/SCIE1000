# Introduction to Arrays (1) - Creating Arrays

So far, we have only used Python to store individual values in variables. *Arrays* allow multiple values to be stored in one variable, which can be very useful. You can think of an array as simply a *list* of items. Here's a simple example of how you might use an array in Python:

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
* Create an array using the `array(...)` function as shown above. Separate the entries in the array using commas.
* Printing an array will display all of its contents.
* The *size* of an array is simply how many values it holds, so the `size` of the `fib` array is 7.

**Task:** Create an array which contains the first 5 square numbers (1, 4, 9, 16, 25), and assign it the the variable `squares`.

## Solution
```python
from pylab import *

squares = array([1, 4, 9, 16, 25])
```
