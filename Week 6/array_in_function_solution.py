from pylab import *

def how_many(A, n):
    count = 0
    i = 0
    while i<len(A):
        if A[i]==n:
            count = count + 1
        i = i + 1
    return(count)
