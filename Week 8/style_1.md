# Styling (1) - Colours, Lines, and Markers

So far you have mostly used the default styles that Python uses. There are a lot of customization options on offer for graphs, and this exercise will introduce a few of them to you. 

**Note:** At this point in your programming, you should have tried to use google to help you solve problems, whether that is figuring out what an error means, or learning how a bit of syntax works. It is an important skill for a programmer to have to know how to google things efficiently, using relevant keywords. Typically, you want to specify the programming language (Python3), sometimes the IDE (Jupyter), any relevant libraries (pylab), and your problem using technical words. However, when searching information on graphing, you will get better results if you use the term 'matplotlib' instead of 'pylab'. Matplotlib is the library you have been using to plot graphs, and is included in the pylab library (along with other helpful libraries). For example, googling 'matplotlib markers' will help you find the matplotlib documentation about markers. Give it a go now and see if you can find "*" on the list. 

## Line Style

The line style refers to how the line is drawn on the graph.  You can change the line style in a graph as follows:


```
from pylab import *

x = arange(10)
y = x**2

plot(x, y, linestyle='-.')
show()
```

So the third argument in the plot function is `linestyle='-.'`. This tells Python that the linestyle variable should be set to '-.', which represents a dash-dot line. There are four main line style options:

`Solid: '-' (default)`

`Dash: '--'`

`Dash-Dot: '-.'`

`Dot: ':'`


Do not forget the quotations. Technically, 'no line' is also an option. You can do this using `linestyle='None'`.

## Marker Style

The marker style determines the shape of the points on the line, if there are any. There are many marker styles, and you should already be familiar with the asterisk '*'. The following program gives an example of how to change the asterisk in a graph:

```
from pylab import *

x = arange(10)
y = x**2

plot(x, y, marker='o', linestyle="--')
show()
```

This program draws a dashed line with a filled in circle on each point. It doesn't matter what order you put the style options in, so long as the x and y data come first.

## Colours

There are various ways to ask Python to colour your lines. The keyword to use is 'color', and there are 10 default colours that python uses: 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', which refer to blue, green, red, cyan, magenta, yellow, black, and white. They can be used as follows:



```
from pylab import *

x = arange(10)
y = x**2

plot(x, y, marker='o', linestyle="--', color='r')
show()
```

This program draws a red dashed line with red circles on each point. Note the American spelling of colour (unfortunately this is pretty standard for most programming languages). 

There are more colour options available, which you can find by googling 'matplotlib colors api' and finding a list of acceptable colour formats. One popular format uses a set of popular colour names, which can be found by googling `wikipedia X11 color names`. Here is an example of that format being used:


```
from pylab import *

x = arange(10)
y = x**2

plot(x, y, marker='o', linestyle="--', color='salmon')
show()
```

In this format, just the full colour name is needed in quotations. There are many colours available, including 'salmon'. Many colour names you can think of will be accepted for that format, but not all.

## Line Width

You can also specify the width of the line. The default line width is `1`. The following program draws two lines, one thick and one thin:

```
from pylab import *

x = arange(10)
y = x**2
z = x**3

plot(x, y, linestyle='-', linewidth=4)
plot(x, z, color='red', linewidth=0.5)
show()
```


## Shorthand

If the customisation of your line is fairly simple, you can use shorthand. If you want to style your line with a default colour and some types of popular markers and line styles, you can style your line as follows:


```
from pylab import *

x = arange(10)
y = x**2

plot(x, y, 'ro--')
show()
```

This program draws a red ('r'), dashed ('--') line with circles ('o') as markers. These can be in any order. `'--or'`, for example, is also acceptable. You do not need to specify all the style options either. Simply using `'r--'` will draw a red dashed line with no markers, or `'o'` will draw a set of markers in the default colour, with no line. Using just `'r'` will create a solid red line with no markers.

**Task:** 

Draw 5 lines with the provided data, with the following styling:

1. A green dashed line with no markers.
2. A solid line with the X11 colour 'purple', with square markers and line width 0.5.
3. Black octagon markers with no line. 
4. A solid line with width 5 and no markers
5. A dash-dot line with width 2, markers in the shape of 'points', and with the xkcd colour 'blood orange'. (Hint: the matplotlib format for xkcd colours is `'xkcd:colour name'`.


**Hint:** You are welcome to search the internet to see how to achieve the specified styles, including using the matplotlib documentation. 
