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
