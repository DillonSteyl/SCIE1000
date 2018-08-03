# Introduction to Loops (4)
**Task:** Use a while loop to write a program which will print the sum of all the whole numbers from 1 to 100. The final sum is the only thing that needs to be printed, with no accompanying message.

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
