# Introduction to Functions (2)

**Task:** Modify this program so that the `double` function behaves as expected. Also, modify the code to print double the number that the user inputs, using the `double` function.

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
