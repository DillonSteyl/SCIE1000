# Introduction to Functions (3)

**Task:** Write a function called `circleArea` which takes a radius as input, and returns the area of the circle with that radius. Use the `circleArea` function to print the area of the circle with `radius` specified by the user.

## Program
```python
from pylab import *
# Write your function here:



radius = eval(input("Enter radius: "))

```

## Solution
```python
from pylab import *
# Write your function here:
def circleArea(r):
    area = pi*r**2
    return(area)

radius = eval(input("Enter radius: "))
print( circleArea(radius) )

```
