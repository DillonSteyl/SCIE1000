# Challenge: The Species Area Curve

The University of Queensland St. Lucia campus is home to a large variety of wildlife, including student favourites such as the families of ducks seen at UQ Lakes. The university is also home to a range of reptiles, insects and plant species, many of which are Australian fauna and flora. 

You may remember the species area curve discussed earlier in the semester, which can be used to predict the number of species present in a given area of land, dependent on certain geographical factors.

The UQ St. Lucia campus covers 114 hectares of land. Note that 1 hectare is equivalent to 10,000 metres squared. Recall that the species area curve is modelled using the form

```python
S(a) = M*a**p
```
where a is the area of a given sample of land, and M and p are constants. In this exercise, `a` will be in hectares.  

You anticipate that the number of different species at UQ is lower during the months of Autumn and Winter than it is in Summer and Spring. You predict that during Autumn and Winter, the variety is 32.5% lower compared to Spring and Summer. After consulting with a peer, you believe the species area curve for Spring/Summer can be modelled using:

```python
SS = 3*a**0.5
```
Which means the species area curve for Autumn and Winter will be `SS*0.675`. 

You want to see the effects of a reduced land area on the number of species during the different seasons using a graph. On your graph you will have the two species area curves, and two red vertical lines where the number of species drops below 15 for each species area curve. You will ask the user for a number of proposed hectares, and plot a single point on both lines corresponding to the number of hectares they gave as input - with different colours depending on the value at that point in the species area curves.

**Task:** You will write a program that displays a graph with 4 lines and 2 points, given a randomly generated variable `h` (provided for you). The details of the lines and points are as follows:

Line 1: The species area curve for Spring/Summer. The x data will be the hectares, starting with 0 and ending with 114 (inclusive), with a step size of 1. The y data will be the number of species, using the equation given previously. The line will be solid, have no markers, and be coloured with the X11 colour 'green'. This line will be labelled 'Spring/Summer'.

Line 2: The species area curve for Autumn/Winter. The x data will be the hectares, starting with 0 and ending with 114 (inclusive), with a step size of 1. The y data will be the number of species, using the equation given previously. The line will be solid, have no markers, and be coloured with the X11 colour 'orange'. This line will be labelled 'Autumn/Winter'.

Line 3: A vertical line corresponding to the point where the species area curve for Spring/Summer reaches 15. To draw this vertical line, make a line that starts at (25, 0) and ends at (25, 35). This line should have the colour 'r', have a width of 3, and be solid. This line will have no label.

Line 4: A vertical line corresponding to the point where the species area curve for Autumn/Winter reaches 15. To draw this vertical line, make a line that starts at (55, 0) and ends at (55, 35). This line should have the colour 'r', have a width of 3, and be dashed. This line will have no label.

Point 1: Let h be the input from the user. Draw a single point with the marker as a filled in circle ('o') on the Spring/Summer line where `x = h` and `y = 3*h**0.5`. The point should be labelled 'Number of species in S/S'. If this point has a y value below 15, colour it red ('r'). If it is 15 or above, colour it black ('k'). You will need an if statement for this.

Point 2: Let h be the input from the user. Draw a single point with the marker as a filled in square ('s') on the Autumn/Winter line where `x = h` and `y = 3*h**0.5*0.675`. The point should be labelled 'Number of species in A/W'. If this point has a y value below 15, colour it red ('r'). If it is 15 or above, colour it black ('k'). You will need an if statement for this.

The graph should be styled as follows:

Legend: There should be a legend on this graph.

Grid: There should be a grid on this graph.

Title: The title should be 'Species Area Curve in Different Seasons'.

X Axis: The x axis should be labelled 'Area (hectares)'.

Y Axis: The x axis should be labelled 'Number of Species'.

**Note:** Plot the lines in the exact order given, using the exact specifications. The code to generate h is also given.

# Solution
```python
from pylab import *

#These two lines allow h to be random chosen from the range 0 to 114. Do not change these lines. 
import random
h = random.randint(0, 114)

# Write your program below:
a = arange(0,114.1,1)
SS = 3*a**0.5
AW = 0.675*SS

h_SS = 3*h**0.5
h_AW = 3*h**0.5*0.675

SS_vertical_x = array([25, 25])
AW_vertical_x = array([55, 55])
vertical_y = array([0, 35])

plot(a,SS,color='green',label="Spring/Summer")
plot(a,AW,color='orange',label="Autumn/Winter")
plot(SS_vertical_x, vertical_y, 'r', linewidth = 3)
plot(AW_vertical_x, vertical_y, 'r--', linewidth = 3)


if h_SS<15:
    plot(h, h_SS, 'ro', label='Number of Species in S/S')
else:
    plot(h, h_SS, 'ko', label='Number of Species in S/S')
    
if h_AW<15:
    plot(h, h_AW, 'rs', label='Number of Species in A/W')
else:
    plot(h, h_AW, 'ks', label='Number of Species in A/W')




title("Species Area Curve in Different Seasons")
xlabel("Area (hectares)")
ylabel("Number of Species")
grid(True)
legend()
show()

# Do Not Modify Below This Line
savefig("output.png")
```
