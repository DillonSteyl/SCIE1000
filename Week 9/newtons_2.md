# Newton's Method (2)

Recall that Newton's method is as follows:

blah

**Task:** Write a function called `onestep(x)` that applies one step of Newton's method given an initial guess of `x`, and returns the next guess. The function and its derivative are the same as the previous exercise. Please copy paste and use your previous code in this exercise. You should have three functions defined: `f(x)`, `fdash(x)`, and `onestep(x)`.

Round the answer to 5 decimal places. 



# Solution


```from pylab import *

def f(x):
    y = round(exp(0.05*x)*(0.05*x)+5,5)
    return(y)
    
def fdash(x):
    d = round(exp(0.05*x)*(0.0025*x+0.05),5)
    return(d)
    
def onestep(x):
    newguess = round(x - f(x)/fdash(x),5)
    return(newguess)
    
```
