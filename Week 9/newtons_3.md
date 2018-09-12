# Newtons Method (3)

**Task:** Write a function called `newtons_nsteps(x, n)` that applies newtons method `n` times given an initial guess `x`, and returns the guess after `n` steps. Remember to copy paste and use your code from previous exercises. You are already rounding numbers in the outputs of other functions, so you do not need to do any more rounding.

You should have four functions: `f(x)`, `fdash(x)`, `onestep(x)`, and `newtons_nsteps(x, n)`. 


# Solution


```
def f(x):
    y = round(exp(0.05*x)*(0.05*x)-5,5)
    return(y)
    
def fdash(x):
    d = round(exp(0.05*x)*(0.0025*x+0.05),5)
    return(d)
    
def onestep(x):
    newguess = round(x - f(x)/fdash(x),5)
    return(newguess)
    
def newtons_nsteps(x, n):
    currentStep = 1
    while currentStep <= n:
        x = onestep(x)
        currentStep = currentStep + 1
    return(x)
```
