from pylab import *

# Input:
initPop = float(input("Enter the initial population: >"))
growthRate = float(input("Enter the population growth rate: >"))
tFinal = float(input("How many years? >"))

# Initialize Arrays
timeArray = arange(tFinal+1)
Pop = zeros(int(tFinal+1))

# Fill the Population Array
t = 0
while t <= tFinal:
    Pop[t] = initPop*exp(growthRate*t)
    t = t + 1

# Plot the graph
plot(timeArray, Pop)
title("Alien Invasion!")
xlabel("Years")
ylabel("Population")
show()
