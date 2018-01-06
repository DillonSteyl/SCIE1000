# Arrays and Conditionals

**Task:** Write a program which loops through the `numbers` array, and counts the number of positive elements. 

**Hint:** Use a variable `positive_sum`. Use a conditional to increment it when an entry of the array is positive.

## Program
```python
from pylab import *

numbers = array([0, 2, -12, 3, -34, -20, 36, -23, 453, -2302, -1, -2, 34, 8, 32, -90, -23])



print("Number of positive numbers:", positive_sum)
```

## Solution
```python
from pylab import *

numbers = array([0, 2, -12, 3, -34, -20, 36, -23, 453, -2302, -1, -2, 34, 8, 32, -90, -23])
positive_sum = 0
i = 0
while i < size(numbers):
    if numbers[i] > 0:
        positive_sum = positive_sum + 1
    i = i + 1

print(positive_sum)
```
