# Introduction to Graphs (2) - Plotting Lines


We often want to draw whole lines on a graph, rather than just a single point. To do this, we need a list of x and y points to make up the line and draw them on a graph:

```
from pylab import *

x = array([0, 1, 2, 3, 4, 5])
y = x**2

plot(x, y)
show()
 
```

The example above will plot an approximation of the equation `y=x^2`. It does this by plotting the point `x^2` for `x=0,1,2,3,4,5` and then joining these points together with straight lines. 

Plotting a line works the same way as plotting a single point using the plot function. Notice in this example we have not included a third argument in the plot function. This means that Python will use the default line style, which is a solid blue line with no marker. 

It does not matter how the arrays are made, so long as they are the same length. If your arrays have different lengths, you will receive an error similar to this in Jupyter: `ValueError: x and y must have same first dimension, but have shapes (A,) and (B,)`, where A is the length of your x data, and B is the length of your y data. This error message will come at the end of a very long error, so don't be scared by it, but you won't see it in MyPyTutor.


**Task:** 

Write a program that plots the first 6 powers of 2, starting from 2 to the power of 0 and finishing with 2 to the power of 5. The variable x should be used to represent the powers, and y should be used to determine the power of 2.

# Solution


```
from pylab import *

x = array([0, 1, 2, 3, 4, 5])
y = 2**x

plot(x, y)
show()

```







