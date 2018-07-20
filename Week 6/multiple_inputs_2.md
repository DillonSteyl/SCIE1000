# Multiple Inputs (2)

**Task:** Modify this program so that the `cylVolume` function correctly returns the volume of a cylinder with radius `r` and height `h`. Also, modify the code after the function - use the `cylVolume` function to print the volume of the cylinder with the `radius` and `height` entered by the user.

# Solution
```python
from pylab import *

def cylVolume(r,h):
    # calculate the volume of the cylinder:
    return( pi*r**2 * h )

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
# print cylinder volume:
print( cylVolume(radius, height) )
```
