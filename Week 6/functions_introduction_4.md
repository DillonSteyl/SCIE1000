# Introduction to Functions (4)

**Task:** Write a function called `sign` which takes a number as input, and returns the following:
* 1 if the number is positive
* 0 if the number is zero
* -1 if the number is negative

To do this, you will need to nest a conditional in the function.

## Program
```python
# Write function here:



# Do not modify:
num = eval(input("Enter a number: "))
print( sign(num) )
```

## Solution
```python
# Write function here:
def sign(num):
    if num > 0:
        return(1)
    elif num == 0:
        return(0)
    else:
        return(-1)

# Do not modify:
num = eval(input("Enter a number: "))
print( sign(num) )
```
