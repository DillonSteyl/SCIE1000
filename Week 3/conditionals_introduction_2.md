# Introduction to Conditionals (2)

To get you more familiar with basic conditionals, here's another simple exercise for you!

**Task:** Write a program which takes a number as input from the user, and prints out the message "Don't be so negative!" if the number is strictly *less* than 0.

**Hint:** If you can't remember how to take a number as input, go back to week 2!

## Solution
```python
from pylab import *

number = float(input("Give me a number: "))
if number < 0:
    print("Don't be so negative!")
```
