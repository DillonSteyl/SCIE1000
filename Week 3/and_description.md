## The 'and' operator

Being able to check conditions in sequence is useful, but there are some situations where it just isn't efficient. Consider a situation where you must check to see if someone is allowed to drive. To drive, the person must hold a valid license, and their BAC must be below 0.05% at the time of driving. The rules can be more complex depending on the license type and other conditions, but we will assume for now that only open licenses exist. 

This is a situation where multiple conditions need to be true at the same time. We could try putting multiple if/elif/else statements in sequence, or we could use the `and` operator and make our if statements feel more natural. Here is the usual structure of an if statement that includes the `and` operator:

```
if condition1 and condition2:
    #do a thing if BOTH conditions are true.
    
```

Note that you aren't limited to just two conditions, you can have many conditions separated by 'and'. You can keep adding conditions for as long as you like. Here is an example with three conditions:

```
if condition1 and condition2 and condition3:
    #do a thing if ALL conditions are true.
```

We can use this for our driving problem:

```python
BAC = float(input("Enter your BAC (%): "))
license = float(input("Type 1 if you hold an open license, 0 otherwise: "))

if BAC<0.05 and license==1:
    print("You can drive!")
else:
    print("You are not allowed to drive.")
```

So, our program prints "You can drive!" only if their BAC is below 0.05 and they hold an open license. Easy!

**Task:** Write a program to determine if a student is allowed to take the imaginary course HELP2000. A student may only take HELP2000 if they have completed HELP1000 and HELP1500 but haven't completed HELP2001. 

Ask the student using three input functions which courses of the three they have taken, and store their response in the variables HELP1000, HELP1500, and HELP2001. The student will say '1' if they have taken the course, and '0' if they haven't (like the license variable in the driving problem).

Print the message "You can take this course." if they are allowed to take the course, and "You cannot take this course, sorry!" otherwise. 

You should be able to do this with just one if statement (and an else statement), using 'and' operators.

## Solution

````
from pylab import *

HELP1000 = float(input("Type 1 if you have taken the course HELP1000, 0 otherwise"))
HELP1500 = float(input("Type 1 if you have taken the course HELP1500, 0 otherwise"))
HELP2001 = float(input("Type 1 if you have taken the course HELP2001, 0 otherwise"))

if HELP1000 == 1 and HELP1500 == 1 and HELP2001 != 1:
    print("You can take this course.")
else:
    print("You cannot take this course, sorry!")
````
