# Styling (3) - Grids and Legends

It is very important when making graphs that the information is clear to the reader. When drawing multiple lines on a graph, it is helpful to indicate which line corresponds with which set of data. For this we can use a legend. An example program is as follows:

```
from pylab import *

x = arange(0, 8.1, 0.5)
squares = x**2
cubes = x**3

integers = arange(0, 8.1,1)
perfect_squares = integers**2
perfect_cubes = integers**3

plot(x, squares, "r-", label="y = x**2")
plot(x, cubes, "k-", label="y = x**3")
plot(integers, perfect_squares, "ro", label="Perfect Squares")
plot(integers, perfect_cubes, "ko", label="Perfect Cubes")
title("Squares and Cubes")
xlabel("x")
ylabel("y")
legend()
grid(True)

show()
```

There are three things to notice with this program. First, there is a `label` argument in each of the plot functions. This tells Python what the names are for each line, to be displayed to the user. When the legend is displayed, it will have a picture of what the line style looks like (for example, a solid red line for the first line), next to the label that you have chosen, for each line. 

Second, there is the `legend` function, which tells Python that you want to legend displayed to the user on the graph. If you do not use this function, the legend will not be displayed even if you write labels. The legend function does not need an argument, and Python will try to place it somewhere on the graph where it isn't a bother by default. However, as with any graphing function, there are a lot of customisation options if you are willing to search for it.

Third, there is the `grid` function. By default, your graphs will not have any grid lines (vertical and horizontal lines), but you may want to add them to your graph. By calling `grid(True)`, it tells Python that you want grid lines. It's really that simple! But as always, you can customise it.
