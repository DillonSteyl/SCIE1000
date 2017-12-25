# Functions with Multiple Inputs

It is often useful to write a function which can take *multiple* inputs. These functions are written with a very similar format to single-input functions; the only difference is that multiple variables can be passed into these functions. The structure of a function with 3 inputs is given below.

```python
def functionName(input1, input2, input3):
    # function commands here
    
# other code here
```

Inside the function code, we can refer to each variable (`input1`, `input2`, `input3`) seperately. Here's a simple example of a function with two inputs:

```python
def sum(a,b):
    return(a+b)
    
a = eval(input("Give me one number: "))
b = eval(input("Give me another number: "))
print("The sum of the two numbers is:", sum(a,b) )
```

**Task:** Modify this program so that it uses the `prod` function to return the product of the two numbers that are input by the user.

## Program
```python
def prod(x,y):
    return(x*y)
    
a = eval(input("Give me the first number: "))
b = eval(input("Give me the second number: "))
# print product:

```

## Solution
```python
def prod(x,y):
    return(x*y)
    
a = eval(input("Give me the first number: "))
b = eval(input("Give me the second number: "))
# print product:
print( prod(a,b) )
```
