# Array Functions (2) - Array Statistics

Now that you know how to make arrays using functions, here are some python functions that work *with* arrays:

```python
total = sum(A) # the sum function adds up all the elements of array A
length = len(A) # the len function returns the number of elements in array A
maximum = max(A) # the max function finds the highest value in array A
minimum = min(A) # the min function finds the lowest value in array A
average = mean(A) # the mean function finds the mean of all values in array A
```

Now use them!

**Task:** An excited student wrote some code that creates a large array filled with lots of values for an experiment. They want to make sure that the array's values are okay. Given an array `A`, find the mean, minimum, maximum, sum and length of the array and store them in the variables provided. 

Additionally, find the difference between the maximum and minimum (the difference should be positive). and store it in the variable provided.  

**Note:** Do not change the array creation code, otherwise you will not pass the exercise. The array creation code is beyond what we do in SCIE1000, so don't worry if you don't understand it.

## Solution
```
from pylab import *

# array creation code
bigArray = array([i*3+j**4+i*j-k*20+32 for i in range(10) for j in range(10) for k in range(10)])
# do not edit the code above

average = mean(bigArray)
maximum = max(bigArray)
minimum = min(bigArray)
total = sum(bigArray)
length = len(bigArray)
difference = maximum - minimum




```
