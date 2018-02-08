# Spotting Errors

**Task:** Find the errors in the following code, and fix them. Try running the program and reading the error message and output if you are stuck!

## Solution
```python
from pylab import *

def power(a,b):
    # returns a to the power of b
    return(a**b)
    # ** is the correct syntax for power, ^ is a different operator in Python

a = eval(input("Enter the base: "))
b = eval(input("Enter the power: "))

print("The answer is", power(a,b))


```
