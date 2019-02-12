# Euler's Method (2)

Recall the formula for Euler's method is:

`next y = current y + f'(x)*h`

**Task:** Write a function called `onestep(x, y, h)` that calculates the next y value using Euler's method with the given `x`, `y` and `h` values. The derivative is the same as used in the previous exercise. Copy paste your function from the previous exercise and call it inside your `onestep` function. 

Round the output to 5 decimal places. Do not print anything, call your onestep function, or ask for any input. You should have two functions defined in your code (`onestep` and `fdash`). 

**Reminder:** Only use `exp`, not `e**`.


# Solution

```
from pylab import *

def fdash(x):
    d = round(0.05 * x * exp(0.05 * x),5)
    return(d)

def onestep(x, y, h):
    nexty = round(y + fdash(x)*h,5)
    return(nexty)

```
