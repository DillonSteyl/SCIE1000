# Practice Plotting! (2)

To get you more comfortable with plotting graphs in Python, let's try plotting 4 functions on one set of axes!

**Task:** Write a program from scratch to plot the following functions between X=0 and X=10, with a spacing of 0.1 - make sure to **include** the final x-coordinate, X=10.

To ensure MyPyTutor evaluates your work correctly, make sure you use the variable name 'X' for the array containing your x-values, and the variable names given below for each function.

* ` Y1 = -0.2*X + 2`
* ` Y2 = 0.2*X - 2`
* ` Y3 = (-0.2*X+2)*(sin(X)) `
* ` Y4 = (0.2*X-2)*(sin(X)) `

Plot Y1 and Y2 as black dotted lines with 'x' as the marker. Plot Y3 and Y4 as cyan solid lines. You should also give the plot the title "Functions of X and Y", and label the axes as "X value" and "Y value" appropriately.

## Solution
```python
from pylab import *

# x-coordinates
X = arange(0, 10.1, 0.1)
# function 1
Y1 = -0.2*X + 2
# function 2
Y2 = 0.2*X - 2
# function 3
Y3 = (-0.2*X+2)*(sin(X))
# function 4
Y4 = (0.2*X-2)*(sin(X))

# Plot:
plot(X, Y1, marker='x', linestyle=':', color='k')
plot(X, Y2, marker='x', linestyle=':', color='k')
plot(X, Y3, color='c')
plot(X, Y4, color='c')
title("Functions of X and Y")
xlabel("X value")
ylabel("Y value")

show()
```
