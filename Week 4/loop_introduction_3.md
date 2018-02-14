# Introduction to Loops (3)

To get you more comfortable with while loops, let's try something different!

**Task:** Use a while loop to write a "Happy New Year!" program, which counts down from 3. Your output should be:
```
3
2
1
Happy New Year!
```

**Hint:** You will need to subtract from `i`, instead of adding to it as you did in the last exercise.

## Solution
```
from pylab import *

i = 3
while i >= 1:
    print(i)
    i = i - 1
    
print("Happy New Year!")
```
