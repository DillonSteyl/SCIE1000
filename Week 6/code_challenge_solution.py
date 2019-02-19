from pylab import *

def primes(n):
    P = array([2,3,5,7,11,13,17,19,23,29])
    i = 0
    while i < len(P):
        j = 0
        while j< len(P):
            if P[i]*P[j]==n:
                return(P[i],P[j])
            j = j + 1
        i = i + 1
    return(-1,-1)
