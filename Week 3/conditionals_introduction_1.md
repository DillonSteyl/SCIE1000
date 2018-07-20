# Introduction to Conditionals

It is often necessary to have a program behave differently depending on whether a certain condition is true or false. This can be done using *conditionals*. They can allow the program to do more complicated things by performing different actions depending on the value of a variable. Conditionals can also allow a program to "respond" to user input. This is incredibly useful!

The most simple form of conditional has the following structure:
```python
if condition:
    # do a thing if condition is true
    # do another thing if condition is true
# this code will execute regardless of whether the condition is true or false.
```
Some important notes:
* The `condition` must be able to be resolved as true or false (for example, `3<5` is true)
* After the first line (`if condition:`), any code that is **indented by four spaces (or one tab)** will only run if the condition is true. 'Indented' means that there is a space between the left side, and where code actually starts on the line.
* Lines of the program that occur after the first line but are **not** indented by four spaces will run regardless of the conditional.

Here is an example of a program that uses a simple conditional:

```python
marks = float(input("What mark did you receive? "))
if marks >= 50:
    print("Congratulations. You passed!")

print("Finished!")
```

Here are two examples of what can happen when this program is run. Take note of the input!
```
What mark did you recieve? 52
Congratulations. You passed!
Finished!

What mark did you receive? 38
Finished!
```

## Conditions
Here are some examples of operators in Python that resolve to either true or false. Great for conditionals!

| Operation                  | Python |
|:---------------------------|:------:|
| 'Greater than'             | a > b  |
| 'Less than'                | a < b  |
| 'Greater than or equal to' | a >= b |
| 'Less than or equal to'    | a <= b |
| 'Equal to'                 | a == b |
| 'Not equal to'             | a != b |

**Note:** the operation for checking equality is `==`, NOT `=`. This because `=` is reserved for variable assignment!

**Task:** Modify this program so that it prints the message "You are not tall enough to ride!" if the value of the `height` variable is less than 130.

## Solution
```python
from pylab import *

height = float(input("Enter your height: "))
if height < 130:
    print("You are not tall enough to ride!")
```
