# Introduction to Functions (2)

**Task:** Modify this program so that the `double` function doubles any input passed into it. Also, modify the code after the function - use the `double` function to print *double* the number that the user inputs.

## Program
```python

def double(x):
    # doubles the input
    

number = eval(input("Give me a number: "))
```

## Solution
```python

def double(x):
    # doubles the input
    ans = 2*x
    return(ans)
    
number = eval(input("Give me a number: "))
print(double(number))

```
