# Introduction to Functions (3)

**Task:** Write a function called `circleArea` which takes a radius as input, and returns the area of the circle with that radius.

## Solution
```python
from pylab import *
# Write your function here:
def circleArea(r):
    area = pi*r**2
    return(area)

# do not modify:
radius = eval(input("Enter radius: "))
print( circleArea(radius) )

```
