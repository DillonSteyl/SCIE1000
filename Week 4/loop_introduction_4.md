# Introduction to Loops (4)
**Task:** Use a while loop to write a program which will print the sum of all the whole numbers from 1 to 100, inclusive. The final sum is the only thing that needs to be printed, with no accompanying message. 

**Hint:** You will need a variable to count through the loop, and another variable to keep track of the total sum. 

## Solution:
```python
from pylab import *

sum = 0
i = 1

while i <= 100:
    sum = sum + i
    i = i + 1
    
print(sum)
```
