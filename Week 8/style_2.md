# Graph Styles (2) - Titles and Axis Labels

For good science communication, your graphs should be labelled and titled. This is very easy to do in Python. Here is an example program that labels both axes, and gives the graph a title:

```
from pylab import *

time = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
temp = array([100, 80, 66, 58, 51, 45, 42, 37, 35, 33])

plot(time, temp, 'v:')
title("Cooling of hot water over time")
xlabel("Time (minutes) since start")
ylabel("Temperature (degrees Celcius)")
show()

```

Three new functions are used here. The `title` function displays a message above the graph by default. The `xlabel` function displays a message below the graph, for the x axis. And the `ylabel` function displays a vertical message to the left of the graph, for the y axis. Expect to use these functions in class and possibly for your assignment, every time.

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

X = arange(0, 10.1, 0.1)
Y1 = -0.2*X + 2
Y2 = 0.2*X - 2
Y3 = (-0.2*X+2)*(sin(X))
Y4 = (0.2*X-2)*(sin(X))

plot(X, Y1, marker='x', linestyle=':', color='k')
plot(X, Y2, marker='x', linestyle=':', color='k')
plot(X, Y3, color='c')
plot(X, Y4, color='c')
title("Functions of X and Y")
xlabel("X value")
ylabel("Y value")

show()

# Do not modify (this code is necessary for MyPyTutor to show output):
savefig("output.png")
```

