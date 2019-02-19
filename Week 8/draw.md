# Introduction to Graphs (4) - Draw a Shape

Lines don't just have to go from left to right. You can draw whatever lines you like, in whatever direction you like, so long as you specify the coordinates of the points. 

Here is a program that draws a triangle by specifying the three corners:

```
from pylab import *

x = array([0, 1, 0.5, 0])
y = array([0, 0, 1, 0])
print("It's a triangle!")

plot(x, y)

show()


```

So the line starts at the origin (0, 0), then goes to (1, 0) which draws the base of the triangle. Next it goes to (0.5, 1) to draw the right side of the triangle, then back down to the origin again to draw the left side of the triangle. And it works! 

Notice that despite having three points, a triangle needs four points to be drawn correctly using the plot function. Take a second to think about that. Even if you are drawing one line, you still need two points to signify the start and end. If your shape has `n` sides, you will need `n+1` points on your graph to draw it. 


**Task:**

Draw a square where the top left corner has coordinates (3, 3), and the square has height and width equal to 2. Start from the top left corner and go **clockwise**. You do not need to print anything.
