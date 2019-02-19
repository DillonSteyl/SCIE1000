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
