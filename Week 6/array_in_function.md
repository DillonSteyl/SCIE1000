# Functions and Arrays (1) - Arrays as Input

The input to functions does not always have to be a number. You can also take arrays as input. Here is an example:


```
from pylab import *

def multiply(A):
    #this function multiplies all the elements of an array together
    product = 1
    i = 0
    while i<len(A):
        product = product * A[i]
        i = i + 1
    return(product)
    
 ```
 
 **Task:** Write a function that returns how many times the number n occurs in array A. Name the function `how_many`. 
 
 **Hint:** For this you will need a conditional, inside a while loop, inside a function! And that function needs to take multiple inputs!


```
from pylab import *

def how_many(A, n):
    count = 0
    i = 0
    while i<len(A):
        if A[i]==n:
            count = count + 1
        i = i + 1
    return(count)


```
