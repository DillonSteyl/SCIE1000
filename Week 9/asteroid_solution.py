from pylab import *

def fdash(x):
    d = round( (-0.05*x+5)*exp(0.002*x)*0.05,5)
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
    
def will_it_hit(h):
    prediction = eulers(0, 160.195, h, 215/h)
    if abs(prediction - 150)<0.01:
        return(1, prediction)
    else:
        return(0, prediction)
