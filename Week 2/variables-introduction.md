# Introduction to Variables

Variables are absolutely fundamental to programming. They allow the program to remember a value, which is associated with a certain name. This name is used to access, modify, and use the variable. It is good practice to choose *meaningful* and *simple* names for your variables. Variable names cannot contain spaces or other "special" characters - and it is important to note that variable names are also *case sensitive*.

To assign a value to a variable, we use the following command:

```python
name = expression
```

Where `name` is the name of the variable, and `expression` is a value/expression. Python will evaluate the expression on the right hand side, and then assign that value to the variable with the name given on the left. For example, the following code will assign the value `190` to the variable called `height`, and `18` to the variable called `age`.

```python
height = 190
age = 2018-2000
```

Once you have assigned a value to a variable, Python can remember and use the value associated with that variable name in subsequent calculations. For example:

```python
birth_year = 2000

age = 2018 - birth_year
print("You are", age, "years old!")

```

**Task:** Modify the following program so that it calculates the area of a rectangle with width `13` and height `22` - do this by creating two variables, `width` and `height`, and assigning the appropriate values to them.

## Program:
```python
from pylab import *

# create variables here:


# do not modify:
area = width * height
print("Width:", width)
print("Height:", height)
print("Area:", area)

```
