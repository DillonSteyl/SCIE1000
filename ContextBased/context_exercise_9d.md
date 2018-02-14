The government was unhappy with the amount of deaths that would occur despite the large amount of vaccinations. It is expensive to vaccinate the population at a rate of 1000000 people per week, but they are willing to provide more funding if it will have a big impact. They want you to investigate the effect of vaccination rate on deaths, so they will know how many people to vaccinate per week.

**Task:** Plot a graph of the number of deaths for different vaccination rates. Start with 1000000, increasing by 50000 until 2000000 (inclusive).

The title of your graph should be "Effect of vaccinations p/w on Deaths". The x-axis should be labelled "Vaccinations per week", and the y-axis should be labelled "Deaths". There should be no legend or print statements. 

**Hint:** Now would be a good time to use the function you wrote in the previous exercise (you will have to copy paste it if you want to use it).


**Solution:**
````
from pylab import *

def runSimulation(weeks, N, a, b, d, v, stepSize):
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
        if S[i+1]<v*stepSize:
            R[i+1] = R[i+1] + S[i+1]
            S[i+1] = 0
        else:
            S[i+1] = S[i+1] - v*stepSize
            R[i+1] = R[i+1] + v*stepSize
        i = i+ 1
  
    return D[numSteps-1]


weeks = 20
N = 25000000
a = 2.5
b = 0.5
d = 0.0001
stepSize = 0.1
V = arange(1000000, 2000001, 50000)
D = zeros(size(V))


i = 0
while i<size(V):
    D[i] = runSimulation(weeks, N, a, b, d, V[i], stepSize)
    i = i + 1

plot(V, D)
xlabel("Vaccinations per week")
ylabel("Deaths")
title("Effect of Vaccinations p/w on Deaths")
show()




# do not modify (this code is necessary for MyPyTutor to show output):
savefig("output.png")
````
