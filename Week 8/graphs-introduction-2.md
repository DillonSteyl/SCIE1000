# Introduction to Graphs - Array Operations and Plotting

Now that we know how to create an array of x-coordinates (using `arange`), we need to create our y-coordinates in order to plot a graph. It is simple to do this when plotting mathematically defined functions. We can perform calculations with arrays the same way as we do with numbers - Python will simply perform the calculation on each element in the array. For example,

```python
from pylab import *

# x-coordinates:
X = arange(0,4.1,1)
# y-coordinates:
Y = X**2
```

The program above will create two arrays - the `X` array contains the whole numbers between 0 and 4, and the `Y` array contains all the squares of those numbers (0,1,4,9,16). Now, we can (approximately) plot the function y=x<sup>2</sup> by plotting these points against each other. To do this, we use the following program:

```python
from pylab import *

# x-coordinates:
X = arange(0,4.1,1)
# y-coordinates:
Y = X**2

plot(X,Y)
show()
```

The `plot(X,Y)` command plots the points defined by the two arrays, `X` and `Y`. The first array will be used to define the x-coordinates, and the second array will define the y-coordinates. The `show()` command will display the graph. Here's the output from the program: 

![graph1](graph1.png)

We can make this graph look a lot smoother by introducing more x-coordinates. The lines that Python uses to join points together will be shorter and less noticeable. Here's the graph we get when we use `X = arange(0, 4.1, 0.1)`:

![graph2](graph2.png)
