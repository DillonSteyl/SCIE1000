# Practice Plotting!

Time for you to try writing program to plot functions from scratch!

**Task:** Write a program which plots the function `Y = X**3` from `X=-3` to `X=3`. Use a spacing of 0.1, and make sure to include the final x-coordinate... remember how the `arange` function works!

## Solution
```python
from pylab import *

# x-coordinates
X = arange(-3, 3.1, 0.1)
# function
Y = X**3

plot(X,Y)
show()
```
