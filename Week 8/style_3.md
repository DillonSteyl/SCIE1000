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

# Task

The University of Queensland St. Lucia campus is home to a large variety of wildlife, including student favourites such as the families of ducks seen at UQ Lakes. The university is also home to a range of reptiles, insects and plant species, many of which are Australian fauna and flora. 

You may remember the species area curve discussed earlier in the semester, which can be used to predict the number of species present in a given area of land, dependent on certain geographical factors.

The UQ St. Lucia campus covers 114 hectares of land. Note that 1 hectare is equivalent to 10,000 metres squared. Recall that the species area curve is modelled using the form

```python
S(a) = M*a**p
```
where a is the area of a given sample of land, and M and p are constants. 

You anticipate that the number of different species at UQ is lower during the months of Autumn and Winter than it is in Summer and Spring. You predict that during the cooler months, the variety is 32.5% lower. After consulting with a peer, you believe the species area curve for Spring/Summer can be modelled using

```python
SS = 3*a**0.5
```

Write a program that plots the species area curve for both Autumn/Winter and Spring/Summer, where the x-axis represents the number of 1,000m square cells of UQ land being considered. Label each of the individual plots as 'Spring/Summer' and 'Autumn/Winter', and give your graph the title 'Species Area Curve'. Label the axes as 'Area (1000m square cells)' and 'Number of Species'. Make sure you include a legend. Also ensure your graph displays a grid. 

Use the following variable names:

a = area array

SS = Spring/Summer model

AW = Autumn/Winter model


# Solution
```python
from pylab import *

# Some variables to use
M = 3
p = 0.5

# Write your program below:
a = arange(0,1141,1)
SS = M*a**p
AW = 0.675*SS

plot(a,SS,label="Spring/Summer")
plot(a,AW,label="Autumn/Winter")
title("Species Area Curve")
xlabel("Area (1000m square cells)")
ylabel("Number of Species")
grid()
legend()
show()

# Do Not Modify Below This Line
savefig("output.png")
```
