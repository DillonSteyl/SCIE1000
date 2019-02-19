from pylab import *

# Input:
initPop = float(input("Enter the initial population: >"))
growthRate = float(input("Enter the population growth rate: >"))
tInvasion = float(input("At what year do aliens invade? >"))
tFinal = float(input("Total years to model? >"))

# Initialize Arrays and Variables
timeArray = arange(tFinal+1)
Pop = zeros(int(tFinal+1))
invasionPop = initPop*exp(growthRate*tInvasion)

# Fill the Population Array
t = 0
while t <= tFinal:
    if t <= tInvasion:
        Pop[t] = initPop*exp(growthRate*t)
    else:
        Pop[t] = invasionPop - 730000000*(t-tInvasion)
    t = t + 1

# Plot the graph
plot(timeArray, Pop)
plot(tInvasion, invasionPop, 'r*')
title("Alien Invasion!")
xlabel("Years")
ylabel("Population")
show()
