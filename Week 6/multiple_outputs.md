#  Multiple Outputs

Sometimes, you might want a function to return multiple outputs. Here is how it works:

```
from pylab import *

def my_function(a, b):
    c = a + b
    d = a * b
    return(c, d)

answer1, answer2 = my_function(2, 3)
print("Answers: ", answer1, answer2)

```

The output of this program is "Answers: 5 6". 

For a multiple output function to work, the returned variables need to be separated by a comma. This means that when you call the function, you need two variables to assign the output to. These also need to be separated by a comma. 

The output will be assigned to the variables in the order they are written in the function. So the number `c` is assigned to answer1, and the number `d` is assigned to answer2. 

You can return any number of things in a function. They just need to be separated by more commas. 

**Task:** Write a function called 'powers' that takes one number as input, and returns the inverse, square, and cube, in that order. Call the function with `2` as input, and the outputs need to be assigned to the variables `inverse`, `square`, and `cube`, respectively.

**Hint:** The inverse of a number is that number to the power of -1. The square is that number to the power of 2. The cube is that number to the power of 3. 

```
from pylab import *

def powers(n):
    return(n**-1, n**2, n**3)
    
inverse, square, cube = powers(2)

```
