# Functions and Loops

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



**Task:** Write a function that takes a number as input, and returns the factorial of that number. Name your function `factorial`.

**Hint 1:** The factorial of n is all the integers from 1 to n multiplied together. So the factorial of 3 is `1*2*3 = 6`.  
**Hint 2:** The factorial of 0 is 1. Make sure your function returns 1 if the input is 0. 
