# Styling - Titles Axis Labels

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

**Task:** WRITE A GRAPH or sOMETHING 
