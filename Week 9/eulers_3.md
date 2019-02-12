# Euler's Method (3)

Recall that after one step of Euler's function is calculated and the new `y` value is found, the new `x` value is also updated to `x+h`. Note that it happens in that order. First the next `y` value is found, *then* the corresponding `x` value is updated.

**Task:** Write a function called `eulers(x, y, h, n)` that uses euler’s method `n` times with the given `x`, `y` and `h` values. It will return the final `y` value. Remember to copy paste your `onestep` and `fdash` functions. You are encouraged to call them in your `eulers` function, but it is up to you. 

The `fdash` and `onestep` functions already round their output, so you will not need to do any rounding inside the `eulers` function.

**Hint:** One way of implementing this function is to use a while loop. 

**If you need help with Euler's method:**

The following example of Euler’s method is given in case you do not understand how it works with multiple steps:

F dash: 2x + 2

Initial x: 1

Initial y: 4

Step size (h): 0.5

Number of steps (n): 3

**Step 1:**

`Fdash = 2*1 + 2 = 2 + 2 = 4`

`Value of y at step 1: new y = 4 + 4*0.5 = 4 + 2 = 6`

`New x value = 1 + 0.5 = 1.5`

**Step 2:**

`Fdash = 2*1.5 + 2 = 3 + 2 = 5`

`Value of y at step 2: new y = 6 + 5*0.5 = 6 + 2.5 = 8.5`

`New x value = 1.5 + 0.5 = 2`

**Step 3:**

`Fdash = 2*2 + 2 = 4 + 2 = 6`

`Value of y at step 3: new y = 8.5 + 6*0.5 = 8.5 + 3 = 11.5`

`New x value = 2 + 0.5 = 2.5`



So our final value for y is 11.5 after 3 steps (at x = 2.5). For interest, one function with this derivative is `y = x**2+2*x+1`. At x = 1, y is equal to 4, like in this example. At x = 2.5 (which is our final x value), the value of y is 12.25. This is pretty close to our approximated value of 11.5. 



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
       y = onestep(x, y, h)
       x = x + h
       currentStep = currentStep + 1
    return(y)

```
