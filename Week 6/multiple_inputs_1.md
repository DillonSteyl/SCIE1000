# Multiple Inputs (1)

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
    
a = float(input("Give me one number: "))
b = float(input("Give me another number: "))
print("The sum of the two numbers is:", sum(a,b) )
```

**Task:** Modify this program so that it uses the `prod` function to return the product of the two numbers that are input by the user.
