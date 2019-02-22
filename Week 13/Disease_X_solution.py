from pylab import *

def highest(A):
    highestIndex = 0
    i = 1
    while i < len(A):
        if A[i]> A[highestIndex]:
            highestIndex = i
        i = i + 1
    return(highestIndex)

weeks = 20
N = 25000000
a = 2.5
b = 0.5
d = 0.0001
stepSize = 0.1
time = arange(0, weeks+0.1, stepSize)
numSteps = size(time)
S = zeros(numSteps)
I = zeros(numSteps)
R = zeros(numSteps)
D = zeros(numSteps)

S[0] = N - 1
I[0] = 1
R[0] = 0
D[0] = 0

i = 0
while i<numSteps-1:
    S[i+1] = S[i] + stepSize*(-a*S[i]*I[i]/N)
    I[i+1] = I[i] + stepSize*(a*S[i]*I[i]/N - b*I[i] - d*I[i])
    R[i+1] = R[i] + stepSize*(b*I[i])
    D[i+1] = D[i] + stepSize*(d*I[i])
    i = i+ 1

maxIndex = highest(I)

print("The total number of deaths is", D[numSteps-1])
print("The maximum number of people infected at once is", I[maxIndex], "which occurred at step", maxIndex)
