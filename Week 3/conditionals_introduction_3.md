# Introduction to Conditionals (3)
This program calculates the area of a circle with a radius given by the user.

**Task:** Modify this program so that it prints the line "This is the unit circle!" if the `radius` is exactly 1. Ensure the program prints this line *after* the area of the circle has been calculated and printed.

## Solution
```python
from pylab import *

# Do not modify:
input_radius = float(input("Enter radius of the circle: "))
# Convert radius to a positive value, in case the input is negative:
radius = abs(input_radius)
area = pi*radius**2
print("Area:", area)

# Your code here:
if radius == 1:
    print("This is the unit circle!")
```
