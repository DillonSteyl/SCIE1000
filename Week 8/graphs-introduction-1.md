# Introduction to Graphs - Arange

Drawing graphs is very important in any form of computer modelling. It can allow you to easily visualize complex (or simple) behaviour, and provide a form of output for your program that is a lot easier to understand than lines of text. We will only be covering 2D graphs in SCIE1000.

To plot a 2D graph in python, you will need to use two *arrays* - one containing the x-coordinates of the points to plot, and the other containing the y-coordinates. Python plots a graph by placing these points on a grid, and then connecting adjacent points with a straight line (if we choose).
**Note:** Essentially, an *array* is just a way of storing multiple values in one variable name. We wil cover these in more detail next week.

It is common to plot a graph by using x-coordinates that are equally spaced. The closer these points are to each other, the 'smoother' our graph will appear. To create an array of x-values, we can use the `arange` function:

```python
X = arange(a,b,s)
```

This command will create an array of values starting at `a`, increasing with a step size of `s`, and stopping at the last value less than `b`. For example,

```python
X = arange(0, 4, 0.5)
```

will create an array with the name `X` that contains the values 0, 0.5, 1, 1.5, 2, 2.5, 3, and 3.5 - note that 4 is **not** included.

**Task:** Write a program that creates an array (called `X`) which contains all the values from 0 to 10, with a spacing of 0.5.

## (One) Solution:
```python
X = arange(0, 10.1, 0.5)
```
