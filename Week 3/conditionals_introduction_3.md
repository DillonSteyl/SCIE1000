# Introduction to Conditionals (3)

**Task:** Modify this program so that it prints the line "This is the unit circle!" if the radius is exactly 1. Ensure the program prints this line *after* the area of the circle has been calculated and printed.

## Program
```python
from pylab import *

radius = eval(input("Enter radius of the circle: "))
area = pi*radius**2
print("Area:", area)

```

## Solution
```python
from pylab import *

radius = eval(input("Enter radius of the circle: "))
area = pi*radius**2
print("Area:", area)
if radius == 1:
    print("This is the unit circle!")
```
