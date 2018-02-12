#program to model the change in the population of Queensland over the next 10 years based on a growth rate of 1.6%

from pylab import *

#Variables:
growth_rate = 0.0016
X = arange(0,10,1)
population = zeros(10)
population[0] = 5000000

#Loop to calculate population
while i<10:
    population[i] = population[i-1] * (1+growth_rate)
    i = i+1

#Using -1 will point to the last element in the array
print("The population after 10 years in Queensland is", round(population[-1]))

# Plot:
title("Population of Queensland over 10 years")
xlabel("Year")
ylabel("Population")
plot(X,population)
show()

# do not modify (this code is necessary for MyPyTutor to Show Output):
savefig("output.png")
