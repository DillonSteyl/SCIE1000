# Multiple Inputs (2)

**Task:** Modify this program so that the `cylVolume` function correctly returns the volume of a cylinder with radius `r` and height `h`.

# Program
```python
from pylab import *

def cylVolume(r,h):
    # calculate the volume of the cylinder:


# do not modify:
radius = eval(input("Enter radius: "))
height = eval(input("Enter height: "))
print( cylVolume(radius, height) )
```

# Solution
```python
from pylab import *

def cylVolume(r,h):
    # calculate the volume of the cylinder:
    return( pi*r**2 * h )

# do not modify:
radius = eval(input("Enter radius: "))
height = eval(input("Enter height: "))
print( cylVolume(radius, height) )
```
