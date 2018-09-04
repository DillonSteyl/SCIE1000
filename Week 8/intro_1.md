# Introduction to Graphs (1)

In Python, we are not limited to just print statements when we want to show output to users. We are also able to create graphs, which can be very important when communicating in science.

There are two important functions we use to create graphs. There is the `plot` function, which we use to define the data for our graph, and there is the `show` function, which tells python to display the graph that we have defined. In some IDEs (Integrated Development Environments), such as Jupyter, the show function isn't always necessary (although it usually is). But as it is necessary in most IDEs, it's best to get into the habit of using it every time. 

Here is an example program that will plot a single point on a graph and display it for the user:

```

from pylab import *

plot(2,3, '*')
show()

```

This program will plot a single point in the shape of an asterisk (`*`) with its x coordinate as 2 and its y coordinate as 3. 

The plot function can take different amounts of input, depending on what you want to do. For the most part, the first two arguments (inputs) for the plot function are the x and y values, respectively. All arguments after this are to do with the appearance of the graph. If we just want to specify what marker we want to use, then a third argument specifying the marker type in quotations will work, which is what we have done here. The show function takes no input. 

You'll notice that the output of these functions are not assigned to any variables. They are just called on lines by themselves. This is how they are expected to be used, but if you decide to make complex graphs later on in your studies (not in this course), know that the plot function will produce output if you want it to.

**Task:**

Write a program that plots an asterisk with x and y coordinates (4, 2.5), and displays the graph for the user. 


**Note:** Once you have passed the exercise, observe the appearance of the graph. The x and y axis have no labels. There is no title. The x and y scales have been generated automatically to fit the point you made. 
