# Introduction to Graphs 3 - Multiple Lines

Comparing multiple sets of data happens often in science, so it is useful to know how to plot multiple lines on the same graph. Here is a simple example:

```

X = arange(0, 10.1)
Y1 = X**2
Y2 = X**3

plot(X, Y1)
plot(X, Y2)

show()

```

This program plots two lines, one showing the growth of a square function, and the other a cube function. By default, Python will use different colours for the different lines. 

Plotting multiple lines is pretty simple. You just need to use the plot function for each line you want to draw. In this example we used the same X array for both lines, but this is not necessary. If you want to use separate X arrays, they just need to be defined, here is an example:


```

X1 = arange(0, 10.1)
Y1 = X1**2

X2 = arange(-5, 5)
Y2 = X2**3

plot(X1, Y1)
plot(X2, Y2)

show()

```

You are not limited to just two lines. You may plot as many lines (or points) as you want until your computer gives up. 

**Task:**

Plot two lines described by the following equations, with the x data provided:

`y1 = x + 4`
`y2 = -0.5*x + 10`

Plot a point where the two lines intercept (at x = 4, y = 8), using an asterisk as a marker.

**Hint:** That's three times you must use the plot function. Two lines and one point.
