# Introduction to Functions (4) - Conditionals

**Task:** Write a function called `my_sign` which takes a number as input, and returns the following:
* 1 if the number is positive
* 0 if the number is zero
* -1 if the number is negative

To do this, you will need to nest a conditional in the function. You can have multiple return statements in a function (for example, in each conditional).

Here is an example:

```
from pylab import *

#Returns 1 if the number is 7, 0 otherwise
def isSeven(n):
    if n==7:
        return(1)
    else:
        return(0)

```
