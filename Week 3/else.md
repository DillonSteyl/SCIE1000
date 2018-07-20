# What Else?

In the simple case for conditionals, we have written a program so that certain lines of code are executed if a condition is true. However, often we would like the program to run some *different* commands only if the condition is false. To do this, we use the `else` keyword as follows:

```python
if condition:
    # do stuff if condition is true
else:
    # do different stuff if condition is not true
    
# this code will be executed regardless of the conditional shown above
```

Here is an example of how this might be used:

```python
from pylab import *

mark = float(input("What mark did you receive? "))
if mark >= 50:
    print("Congratulations! You passed!")
else:
    print("You failed. Better luck next time!")
print("Finished!")
```

Here are two examples of the output when running this program.
```
What mark did you receive? 38
You failed. Better luck next time!
Finished!

What mark did you receive? 75
Congratulations! You passed!
Finished!
```

**Task:** Modify this program so that it prints the message "You are not tall enough to ride!" if the value of the `height` variable is less than 130, and prints the message "You are tall enough to ride." otherwise.

## Solution
```python
from pylab import *

height = float(input("Enter your height. "))
if height < 130:
    print("You are not tall enough to ride!")
else:
    print("You are tall enough to ride.")

```
