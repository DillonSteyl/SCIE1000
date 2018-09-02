# Introduction to Graphs (1)


Often times we want to draw whole lines on a graph, rather than just a single point. To do this, we need a list of x and y points to make up the line and draw them on a graph:

```
from pylab import *

x = array([0, 1, 2, 3, 4, 5])
y = x**2

plot(x, y)
show()
 
```

Plotting a line works the same way as plotting a line using the plot function. Notice in this example we have not included a third argument in the plot function. This means that Python will use the default graph style, which is a solid blue line with no marker. 

It does not matter how the arrays are made, so long as they are the same length. If your arrays have different lengths, you will receive an error similar to this in Jupyter: `ValueError: x and y must have same first dimension, but have shapes (A,) and (B,)`, where A is the length of your x data, and B is the length of your Y data. This error message will come at the end of a very long error, so don't be scared by it.


**Task:** 

Write a program that plots 







