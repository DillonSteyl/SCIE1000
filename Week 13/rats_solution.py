from pylab import *

def highest(A):
    highestIndex = 0
    i = 1
    while i < len(A):
        if A[i]> A[highestIndex]:
            highestIndex = i
        i = i + 1
    return(highestIndex)
steps = 51
A = zeros(steps)
B = zeros(steps)
C = zeros(steps)
D = zeros(steps)

A[0] = 40
B[0] = 20
C[0] = 30
D[0] = 10

i = 1

while i<steps:
    A[i] = A[i-1]*0.7 + B[i-1]*0.1 + C[i-1]*0.4
    B[i] = B[i-1]*0.65 + A[i-1]*0.2 + C[i-1]*0.1
    C[i] = C[i-1]*0.5 + A[i-1]*0.1 + B[i-1]*0.05
    D[i] = D[i-1]*1 + B[i-1]*0.2
    i = i + 1

    
print("The final number of rats in each cage are:")
print("A -", round(A[-1]))
print("B -", round(B[-1]))
print("C -", round(C[-1]))
print("D -", round(D[-1]))
    
maxIndexA = highest(A)
maxIndexB = highest(B)
maxIndexC = highest(C)
maxIndexD = highest(D)

print("The largest number of rats in a cage A is", round(A[maxIndexA]),"at step", maxIndexA)
print("The largest number of rats in a cage B is", round(B[maxIndexB]),"at step", maxIndexB)
print("The largest number of rats in a cage C is", round(C[maxIndexC]),"at step", maxIndexC)
print("The largest number of rats in a cage D is", round(D[maxIndexD]),"at step", maxIndexD)
