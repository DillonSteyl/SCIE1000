from pylab import *

def highest(A):
    highestIndex = 0
    i = 1
    while i < len(A):
        if A[i]> A[highestIndex]:
            highestIndex = i
        i = i + 1
    return(highestIndex)
