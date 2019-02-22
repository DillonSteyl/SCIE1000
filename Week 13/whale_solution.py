from pylab import *

def highest(A):
    highestIndex = 0
    i = 1
    while i < len(A):
        if A[i]> A[highestIndex]:
            highestIndex = i
        i = i + 1
    return(highestIndex)

steps = 201
W = zeros(steps)
Z = zeros(steps)

W[0] = 12
Z[0] = 40

i = 1

while i<steps:
    dZ = 0.4*Z[i-1] - 0.025*Z[i-1]*W[i-1]
    dW = -1*W[i-1] + 0.03*Z[i-1]*W[i-1]
    Z[i] = Z[i-1] + 0.1*dZ
    W[i] = W[i-1] + 0.1*dW
    i = i + 1
    
    
maxIndexW = highest(W)
maxIndexZ = highest(Z)

print("The whale population reaches its peak of", round(W[maxIndexW]),"whales during step", maxIndexW)
print("The zooplankton population reaches its peak of", round(Z[maxIndexZ]),"thousand tonnes during step", maxIndexZ)

print("The number of steps between these peaks is", abs(maxIndexZ-maxIndexW))
