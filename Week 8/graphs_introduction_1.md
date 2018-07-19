# Introduction to Graphs (1) - Arange

Drawing graphs is very important in any form of computer modelling. It can allow you to easily visualize complex (or simple) behaviour, and provide a form of output for your program that is a lot easier to understand than lines of text. We will only be covering 2D graphs in SCIE1000.

To plot a 2D graph in python, you will need to use two *arrays* - one containing the x-coordinates of the points to plot, and the other containing the y-coordinates. Python plots a graph by placing these points on a grid, and then connecting adjacent points with a straight line (if we choose). To create an array of x-values, we usually use the `arange` function:

```python
X = arange(a,b,s)
```
After we create our x-coordinates, we need to create our y-coordinates in order to plot a graph. It is simple to do this if we are plotting mathematically defined functions.

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

# Plot:
plot(X,Y)
show()
```

The `plot(X,Y)` command plots the points defined by the two arrays, `X` and `Y`. The first array will be used to define the x-coordinates, and the second array will define the y-coordinates. The `show()` command will display the graph. Keep in mind that you don't have to name your arrays X and Y, you can use whatever variable names you like. Just make sure the variable names have meaning. Here's the output from the program: 

![graph1](https://imgur.com/BY7MHEg.png)

We can make this graph look a lot smoother and more accurate by using more points. The lines that Python uses to join the points together will be shorter and less noticeable. Here's the graph we get when we use `X = arange(0, 4.1, 0.1)` instead:

![graph2](https://imgur.com/M7CbTKv.png)

**Task:** Modify this program to plot the function y=sin(x).

## Solution
```python
from pylab import *

# x-coordinates:
X = arange(0,2*pi,0.1)
# y-coordinates:
Y = sin(X)

# Plot:
plot(X,Y)
show()
```

## Output
![8-2 Solution](https://imgur.com/zIJg1QV.png)
