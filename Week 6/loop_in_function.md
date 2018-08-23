# Loops in functions

You can also include loops in functions. Here is an example:

```
def mySum(n):
    # adds up all the numbers from 1 to n
    i = 1
    total = 0
    while i<=n:
        total=total+i
        i=i+1
    return(total)

```



**Task:** Write a function that take a number as input, and returns the factorial of that number. Name your function `factorial`.

**Hint:** The factorial of n is all the integers from 1 to n multiplied together. So the factorial of 3 is `1*2*3 = 6`.  

```
def factorial(n):
    i = 1
    total = 1
    while i<=n:
        total=total*i
        i=i+1
    return(total)
    
    
```
