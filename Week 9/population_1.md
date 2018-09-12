# Modelling an Alien Invasion (1)

In the following exercises, you will combine your knowledge of arrays and loops to track the effects of a devestating alien invasion.

Recall that we can often model a normal, peaceful population as follows:

``` P(t) = P0 * exp(k*t) ```

Where `P(t)` represents the population at time `t`, `P0` is the initial population and `k` is the growth rate of the population. Remember: using this model, the rate at which the population grows is proportional to the size of the population.

Assuming that the outbreak has not yet occured (and the world is not running out of space or resources) the world population will closely follow this model.

**Task:** Write a program which models the world population for each year *leading up to* the invasion. 

This program takes the following as input:
* Initial population (`initPop`)
* Growth rate (`growthRate`)
* Number of years to calculate the population for (`tFinal`). You may assume that this will be a whole number.

You should create an array that will hold the population values for each year from `t=0` to `t=tFinal`.

To make this code easier to adapt for the next exercise, you should use the `zeros` function to create the empty `Pop` array. Then, use a `while` loop to go through the array and fill it with the correct population values for `t=0` to `t=tFinal`.

After the while loop is done, plot `Pop` against `timeArray`. Give the plot the following attributes:

* Title: `Alien Invasion!`
* X-label: `Years`
* Y-label: `Population`

To test your code, MyPyTutor will use specific values for the input, so make sure you don't remove the input calls!

## Solution
```python
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
```