# What Else (2)?

Here's another example that will require you to use the `else` statement.

**Task:** Modify this program so that it prints the statement "Don't be so negative!" if `number` is strictly *less* than 0. Also have the program print the statement "Glad to see you're feeling positive!" if `number` is *above* 0.

## Solution
```python
from pylab import *

number = float(input("Give me a number: "))
if number < 0:
    print("Don't be so negative!")
else:
	print("Glad to see you're feeling positive!")
```