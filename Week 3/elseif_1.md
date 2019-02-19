# Else If (1)

Sometimes, we would like to check *more* than one condition. We can do this using the `elif` keyword, which means "else if". This way, we can check for multiple values. The `else` keyword can be included at the *end*, to 'catch' any values we have not explicitly compared against. Study the following example carefully:

```python
from pylab import *

mark = float(input("What mark did you receive? "))
if mark >= 85:
    print("Congratulations! You got a 7!")
elif mark >= 75:
    print("Congratulations! You got a 6!")
elif mark >= 65:
    print("Congratulations! You got a 5!")
elif mark >= 50:
    print("Congratulations! You passed!")
else:
    print("You failed. Better luck next time!")

print("Finished!")
```

Here are some examples of what happens when the program is run:
```
What mark did you receive? 92
Congratulations! You got a 7!
Finished!

What mark did you receive? 32
You failed. Better luck next time!
Finished!

What mark did you receive? 73
Congratulations! You got a 5!
Finished!

```

**Task:** Modify this program so that it prints out the following messages:
* "You can legally drink, even in America!" if the age is over or equal to 21.
* "You can legally drink in Australia!" if the age is over or equal to 18.
* "You are under the legal drinking age." if the age is under 18.

## Solution
```python
from pylab import *

age = float(input("Enter your age: "))
if age >= 21:
    print("You can legally drink, even in America!")
elif age >= 18:
    print("You can legally drink in Australia!")
else:
    print("You are under the legal drinking age.")

```
