# Spot the Error

**Task:** Find an fix the error in the following code


## Program
```python

#program to model the change in the population of Queensland over the next 10 years based on a growth rate of 1.6%

from pylab import *

population = 5000000
growth_rate=0.0016

while i<10:
    population = population * (1+growth_rate)
    i=i+1

print("The population after 10 years in Queensland is", round(population))

```

## Solution
```python

#program to model the change in the population of Queensland over the next 10 years based on a growth rate of 1.6%

from pylab import *

population = 5000000
growth_rate=0.0016

i=0
while i<10:
    population = population * (1+growth_rate)
    i=i+1

print("The population after 10 years in Queensland is", round(population))

```
