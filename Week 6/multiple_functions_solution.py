from pylab import *

def toKilograms(pounds):
    kilos = pounds / 2.2
    return(kilos)
    
def weightOnMars(pounds):
    return(toKilograms(pounds)*0.38)
    
def weightOnMoon(pounds):
    return(toKilograms(pounds)*0.16)
