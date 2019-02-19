from pylab import *

def fdash(x):
    d = round(0.05 * x * exp(0.05 * x),5)
    return(d)

def onestep(x, y, h):
    nexty = round(y + fdash(x)*h,5)
    return(nexty)
