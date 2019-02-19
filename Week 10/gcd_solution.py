from pylab import *

def gcd(a,b):
    while a%b!=0:
        remainder = a%b
        a = b
        b = remainder
    return(b)
