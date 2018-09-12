# Modelling an Alien Invasion (2)

In the previous exercise, we wrote a program to model the population before a devastating alien invasion. Now, we will modify the program to model the population after the alien invasion.

The particular aliens which have invaded earth are extremely methodical. They have a particular "elimination quota" which they must meet every day. After invasion, the human population decreases by exactly 2,000,000 each day (for a total of 730,000,000 per year). Hence, the population after invasion can be described as follows:

```P(t) = invasionPop - 730000000*(t-tInvasion)```

Where `invasionPop` is the human population on the day of invasion. Note that `invasionPop` can be calculated by using `tInvasion` and the formula for population from the previous exercise:

```P(t) = P0 * exp(k*t)```

**Task:** Write a program to model the population before and after an alien invasion.

In this version of the program, we take the following as input:
* Initial population (`initPop`)
* Population growth rate (`growthRate`)
* The year on which the aliens invade (`tInvasion`) 
* The number of years to model for (`tFinal`)

You may find it useful to copy code from the previous exercise. Once again, you will need to create the `Pop` array. You will also need to calculate the population at the point of invasion, `invasionPop`.

Your task is to fill the `Pop` array with the correct population values using the same while loop as before. You should only use *one* while loop and *one* `Pop` array - the `Pop` array contains population values for both before and after the alien invasion.

**Hint:** In the while loop, you should determine which model to use to calculate `Pop[t]` by using a *conditional*.

Once again, plot `Pop` against `timeArray`, with the same title and labels as before (copy your plot code from the previous exercise if you wish!).

Finally, plot a single red star (*) at the point of invasion `(tInvasion, invasionPop)` (see exercises from last week / google)!

## Solution
```python
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
```