# Array Functions

Now that you are proficient in using arrays, here are some python functions that work with arrays:

```python
total = sum(A) # the sum function adds up all the elements of array A
length = len(A) # the len function returns the number of elements in array A
maximum = max(A) # the max function finds the highest value in array A
minimum = min(A) # the min function finds the lowest value in array A
```

Now use them!

**Task:** An excited student wrote some code that creates a large array filled with lots of values for an experiment. They want to make sure that the array's values are okay. Given an array `A`, find the mean, minimum, and maximum of the array and use the provided print statements to print them.

**Note:** Do not change the array creation code, otherwise you will not pass the exercise. The array creation code is beyond what we do in SCIE1000, so don't worry if you don't understand it.

## Solution
```
from pylab import *

# array creation code
A = array([i*3+j**4+i*j-k*20+32 for i in range(10) for j in range(10) for k in range(10)])
# do not edit the code above

mean = sum(A)/len(A)
maximum = max(A)
minimum = min(A)

print("Mean:",mean,", Max:",maximum,", Min:",minimum)
```
