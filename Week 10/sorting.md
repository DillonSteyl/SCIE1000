# Challenge problem: Sorting

For this challenge problem, you will need to write a function called `mySort` that sorts an array from lowest to highest.

**Note:** There already exists a python function for sorting arrays (`sort(A)`). We will check to make sure you don't use it. 

**Hint 1:** A quick way to find the length of an array is the `len` function. Used like: `length = len(A)`, if `A` is the array.

**Hint 2:** One way to solve this problem is to put a while loop inside a while loop.

**Hint 3:** If you are struggling to come up with a way to solve this problem, search 'bubble sort'. A big part of programming is checking to see if anyone has already solved your problem. But for learning purposes, try to write this algorithm yourself.



## Solution

```python
from pylab import *

def mySort(A):
    i = 0
    while i<len(A):
        j = 0
        while j<len(A)-1:
            if A[j]>A[j+1]:
                temp = A[j+1]
                A[j+1] = A[j]
                A[j] = temp
            j+=1
        i+=1
    return A
