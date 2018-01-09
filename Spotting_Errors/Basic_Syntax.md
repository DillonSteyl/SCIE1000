# Spotting Errors

**Task:** Find the errors in the following code, and fix them. Try running the program and reading the error message if you are stuck!

## Program
```python
from pylab import *

def grade(mark)
    if mark >= 85:
        return(7)
    elif mark >= 75:
        return(6)
    elif mark >= 65:
        return(5)
    elif mark >= 50
        return(4)
    elif mark >= 45:
        return(3)
    elif mark >= 20
        return(2)
    else:
        return(1)

user_mark = eval(input("What mark did you receive? ")
print("Your grade is", grade(user_mark)
```

## Solution
```python
from pylab import *

def grade(mark):
    # missing colon above
    if mark >= 85:
        return(7)
    elif mark >= 75:
        return(6)
    elif mark >= 65:
        return(5)
    elif mark >= 50:
        # missing colon above
        return(4)
    elif mark >= 45:
        return(3)
    elif mark >= 20:
        # missing colon above
        return(2)
    else:
        return(1)

user_mark = eval(input("What mark did you receive? "))
print("Your grade is", grade(user_mark))
# missing brackets above
```
