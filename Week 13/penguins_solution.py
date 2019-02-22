from pylab import *

def highest(A):
    highestIndex = 0
    i = 1
    while i < len(A):
        if A[i]> A[highestIndex]:
            highestIndex = i
        i = i + 1
    return(highestIndex)


F = zeros(16)
P = zeros(16)


F[0] = 50
P[0] = 600


i = 1


while i<16:
    F[i] = max(-2*i*(i-8) + 50, 0)
    P[i] = P[i-1]*0.90 + (P[i-1]/6) * (F[i-1]/100)
    i = i + 1
    
maxIndex = highest(F)
penguinsAtMax = P[maxIndex]

print("The quarter with the highest number of fish is", maxIndex, "with", penguinsAtMax, "penguins on the island at the time.")
