### The 'or' operator

Much like the 'and' operator, the 'or' operator joins two conditions to be evaluated as true or false together. The 'and' operator only runs the code if BOTH conditions are true. The 'or' operator runs the code if EITHER or BOTH conditions are true. Here is how it works:

````
if condition1 or condition2:
    #do a thing if EITHER condition is true
````

Just like 'and' operators, you can have many 'or' operators, like this:

````
if condition1 or condition2 or condition3:
    #do a thing if ANY of the conditions are true.
````
 
We can have even more fun with this. You can make if statements using 'and' and 'or', with the help of brackets to make order clear (just like you would in mathematical expressions). Here is an example:

````
if condition1 and (condition2 or condition3):
    #do a thing if condition1 is true and either condition2 or condition3 is true.
````    
These can be very helpful! See how this makes the rollercoaster problem even easier:
 
````
height = eval(input("What is the height (cm) of the rider: "))
adult = eval(input("Type 1 if accompanied by an adult, 0 otherwise: "))

if height<=200 and (height>=130 or (height>=110 and adult==1)):
    print("You may ride. Have fun!")
else:
    print("Sorry, you cannot ride.")
````

**Task:** Write a program that checks to see if a student is allowed to take the imaginary course HELP3000. Here are the rules:


1. Student must have completed either HELP2000 or HELP2001.
2. Student must have completed HELP2500.
3. Student must not have completed HELP3001.
4. Student may take the course and override all other rules if given permission by the Head of School.



Ask the student to enter 1 if they have taken these courses, and 0 otherwise: HELP2000, HELP2001, HELP2500, HELP3001. Then ask the student to enter 1 if they have permission from the Head of School, and 0 otherwise. 

Make sure you ask for these input in order: HELP2000, HELP2001, HELP2500, HELP3001, permission. That should be 5 input statements. Assign these inputs to variables. 

Print the message "You can take this course." if they are allowed to take the course, and "You cannot take this course." otherwise.

**Hint:** Challenge yourself: you should be able to solve this problem with just ONE if statement (and an else statement).

## Solution

````
from pylab import *

HELP2000 = eval(input("Type 1 if you have taken HELP2000, and 0 otherwise: "))
HELP2001 = eval(input("Type 1 if you have taken HELP2001, and 0 otherwise: "))
HELP2500 = eval(input("Type 1 if you have taken HELP2500, and 0 otherwise: "))
HELP3001 = eval(input("Type 1 if you have taken HELP3001, and 0 otherwise: "))
permission = eval(input("Type 1 if you have permission from the Head of School, and 0 otherwise: "))

if permission==1 or ((HELP2000 == 1 or HELP2001 == 1) and HELP2500 == 1 and HELP3001==0):
    print("You can take this course.")
else:
    print("You cannot take this course.")
````
