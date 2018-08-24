# Multiple Outputs (2)

A program has been written but the functions have gone missing. Define and write the functions so that the program passes all the tests. 

**Hint:** The returned values for the Exponential Equation need to be rounded. Please round the value of A0 (or P0, or whatever you name it) to 0 decimal places, and round the value of k to 5 decimal places. Use the round function! (`round(num, places)`, where num is the number you want to round and places is the number of decimal places).

To solve this you may want to try finding the formulas on paper first. Try it yourself before reading the hint below:

**Hint:**

For Linear equations: 

Find m first by using the formula for m. Then, use m and one of the points to find c by rearranging `y = m*x + c`.

For Exponential equations:

You can't guarantee that one of the x values is 0 (which would mean the corresponding y value is A0). But, it will be guaranteed that neither of the y values will be 0. 

So, if both sets of values are subbed into the Exponential equation you get:

`y1 = A0 * exp(k*x1)`
`y2 = A0 * exp(k*x2)`

If you divide these two equations you get:

`y1/y2 = A0*exp(k*x1)/(A0*exp(k*x2))`

Which simplifies to:

`y1/y2 = exp(k*(x1-x2))`

Rearranged to find k:

`k = log(y1/y2)/(x1-x2)` (log here being the natural log). 

Once k is found, one of the equations can be rearranged to find A0:

`A0 = y/(exp(k*x)`

So that's only two lines of calculations you need. First to find k, and then to find A0.

```
from pylab import *

def getLinearEquation(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    c = y2 - m*x2
    return(m, c)
    
def getExponentialEquation(x1, y1, x2, y2):
    k = log(y1/y2)/(x1-x2)
    A0 = y2/(exp(k*x2)
    return(round(A0), round(k,5))
    
    
x1 = float(input("What is the first x value: "))
y1 = float(input("What is the first y value: "))
x2 = float(input("What is the second x value: "))
y2 = float(input("What is the second y value: "))
choice = float(input("Enter 1 if you want to calculate a linear model, and 0 for exponential."))

if choice==1:
    m, c = getLinearEquation(x1, y1, x2, y2)
    print("The value of m is", m, "and the value of c is", c)
else:
    A0, k = getExponentialEquation(x1, y1, x2, y2)
    print("The value of A0 is", A0,"and the value of k is", k)
    
print("Thanks for using this program!")


```
