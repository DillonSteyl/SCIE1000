# Spot the Error

**Task:** Find and fix the error in the following code

**Hint:** Take a closer look at the while loop contents

## Program
```python

from pylab import *

print("This is a program to model the population of fish over time, with a growth rate of 0.05.")

#growth value
r = 0.05

#initial number of fish
init = float(input("Input the initial number of fish: "))

#carrying capacity
capacity = float(input("Input the carrying capacity of the fish population: "))

#number of years to project for
years = float(input("Input the number of years to be modelled: "))

print("Year - Number of Fish")

fish = init
i=1
while i <= years:
    fish = init + r*init*(1-(init/capacity))
    print(i, "  -  ", round(fish))
    i = i + 1
    
print("The fish population changed by", round(abs(fish-init)), "fish in", years, "years.")

```

## Solution
```python
from pylab import *

print("This is a program to model the population of fish over time, with a growth rate of 0.05.")

#growth value
r = 0.05

#initial number of fish
init = float(input("Input the initial number of fish: "))

#carrying capacity
capacity = float(input("Input the carrying capacity of the fish population: "))

#number of years to project for
years = float(input("Input the number of years to be modelled: "))

print("Year - Number of Fish")

fish = init
i=1
while i <= years:
    # use the NEW fish value, not the initial fish value
    fish = fish + r*fish*(1-(fish/capacity))
    print(i, "  -  ", round(fish))
    i = i + 1
    
print("The fish population changed by", round(abs(fish-init)), "fish in", years, "years.")

```
