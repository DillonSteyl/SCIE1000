# Introduction to Graphs (1)

In Python, we are not limited to just print statements when we want to show output to users. We are also able to create graphs, which can be very important when communicating in science.

There are two important functions we use to create graphs. There is the `plot` function, which we use to define the data for our graph, and there is the `show` function, which tells python to display the graph that we have defined. In some IDEs (Integrated Development Environments), such as Jupyter, the show function is usually, but not always, necessary. But as it is necessary in most IDEs and MyPyTutor, it's best to get into the habit of using it every time. 

Here is an example program that will plot a single point on a graph and display it for the user:

```

from pylab import *

plot(2,3, '*')
show()

```

This program will plot a single point in the shape of an asterisk (`*`) with its x coordinate as 2 and its y coordinate as 3. 
