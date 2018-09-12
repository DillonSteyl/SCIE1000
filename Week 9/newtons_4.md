# Newton's Method (4)

It can be difficult to tell how many steps of Newton's method should be used to approximate 0 values in a function. Generally, we want to get pretty close to the zero value, but we also do not want to waste too much time if we are already pretty close. One way to handle this is to stop calculating new guesses if your current guess hasn't changed much compared to your previous guess. For this, we can use percentage change, and stop calculating new guesses if our percentage change is too small, or if there have been too many guesses. 

Recall that percentage change is calculated using the following formula:

`percentage change = |old value - new value| / old value   * 100`

In this formula, the vertical lines indicate absolute value (that is, the value is made positive no matter its value). You can use the abs(x) function to do this. 

**Task:** Write a function called `newtons(x, n, p)` that uses Newton's method to guess the `x` value that corresponds to a zero value for the function. For the input, `n` is the maximum number of steps, and `p` is the minimum percentage change before the program stops making guesses. For the output, return the guess and the number of steps. Copy paste your code from the previous exercises, however you will not need to use the `newtons_nsteps` function anymore. 

**Hint:** Your while loop will stop when either the current step is greater than the maximum number of steps, or the percentage change is lower than the minimum percentage change. You will need to keep track of the previous guess. There are multiple ways to implement this function, so do whatever is most comfortable for you. 

**Note:** You can assume that you will never be given an initial `x` value of 0.


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
    
def newtons(x, n, p):
    currentStep = 1
    stop = 0
    while stop==0 and currentStep <= n:
        previous = x
        x = onestep(x)
        if 100*abs(previous - x)/previous < p:
            stop = 1
        currentStep = currentStep + 1
    return(x, currentStep-1)
```
