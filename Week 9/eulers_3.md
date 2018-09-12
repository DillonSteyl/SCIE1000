# Euler's Method (3)

**Task:** Write a function called eulers(x, y, h, n) that uses euler’s method `n` times with the given x, y and h values. It will return the final y value. Remember to copy paste your `onestep` and `fdash` functions. You are encouraged to use them in your `eulers` function, but it is up to you. 

The `fdash` and `onestep` functions already round their output, so you will not need to do any rounding inside the `eulers` function.

**Hint:** One way of implementing this function is to use a while loop. 

**If you need help with Euler's method:**

The following example of Euler’s method is given in case you do not understand how it works with multiple steps:

F dash: 2x + 2
Initial x: 1
Initial y: 4
Step size (h): 0.5
Number of steps (n): 3

Step 1:

New x value = 1 + 0.5

Fdash = 2*1.5 + 2 = 3 + 2 = 5

Value of y at step 1: new y = 4 + 5*0.5 = 4 + 2.5 = 6.5

Step 2:

New x value = 1.5 + 0.5 = 2

Fdash = 2*2 + 2 = 4 + 2 = 6

Value of y at step 2: new y = 6.5 + 6*0.5 = 6.5 + 3 = 9.5

Step 3:

New x value = 2 + 0.5

Fdash = 2*2.5 + 2 = 5 + 2 = 7

Value of y at step 3: new y = 9.5 + 7*0.5 = 9.5 + 3.5 = 13

So our final value for y is 13 after 3 steps (at x = 2.5). For interest, one function with this derivative is `y = x**2+2*x+1`. At x = 1, y is equal to 4, like in this example. At x = 2.5 (which is our final x value), the value of y is 12.25. This is pretty close to our approximated value of 13. 



# Solution

```
from pylab import *

def fdash(x):
    d = round(0.05 * x * exp(0.05 * x),5)
    return(d)

def onestep(x, y, h):
    nexty = round(y + fdash(x)*h,5)
    return(nexty)
    
def eulers(x, y, h, n):
    currentStep = 1
    while currentStep<=n:
       x = x + h
       y = onestep(x, y, h)
       currentStep = currentStep + 1
    return(y)

```
