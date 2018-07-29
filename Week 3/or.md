### The 'or' operator

Much like the `and` operator, the `or` operator joins two conditions to be evaluated as true or false together. The `and` operator only runs the code if BOTH conditions are true. The `or` operator runs the code if **either** or **both** conditions are true. Here is how it works:

````
if condition1 or condition2:
    #do a thing if EITHER condition is true
````

Just like `and` operators, you can have many `or` operators, like this:

````
if condition1 or condition2 or condition3:
    #do a thing if ANY of the conditions are true.
````
 
We can have even more fun with this. You can make if statements using `and` and `or`, with the help of brackets to make order clear (just like you would in mathematical expressions). Here is an example:

````
if condition1 and (condition2 or condition3):
    #do a thing if condition1 is true and either condition2 or condition3 is true.
````    
These can be very helpful! Consider a more complex version of our driving problem. Recall, you are only allowed to drive if your BAC is below 0.05% and you hold an open license. But now we will consider provisional licenses (P1 (red) and P2 (green) in Queensland). While holding a provisional license, you may only drive if your BAC is 0%. 

To summarise, you may only drive if you either hold an open license **and** your BAC is below 0.05%, **or** if you hold a provisional license **and** your BAC is 0%. 

So using brackets, the condition would be: (open license and BAC<0.05) or (provisional license and BAC==0). 

Here's how it would be implemented in python:
 
````
BAC = float(input("Enter your BAC (%): "))
license = float(input("Type 2 if you have an open license, 1 if you have a provisional license, and 0 otherwise: "))

if (BAC<0.05 and license==2) or (BAC==0 and license==1):
    print("You are allowed to drive!")
else:
    print("Sorry, you are not allowed to drive.")
````

We solved the problem with just one if statement and an else statement! Now it's your turn.

**Task:** Edit the program so that it checks to see if a student is allowed to take the imaginary course HELP3000. Here are the rules:


1. Student must have completed either HELP2000 or HELP2001.
2. Student must have completed HELP2500.
3. Student must not have completed HELP3001.


The student is asked using input statements to enter 1 if they have taken these courses, and 0 otherwise: HELP2000, HELP2001, HELP2500, HELP3001.

Print the message "You can take this course." if they are allowed to take the course, and "You cannot take this course, sorry!" otherwise.

**Hint:** Challenge yourself! You should be able to solve this problem with just ONE if statement (and an else statement).

## Solution

````
from pylab import *

HELP2000 = float(input("Type 1 if you have taken HELP2000, and 0 otherwise: "))
HELP2001 = float(input("Type 1 if you have taken HELP2001, and 0 otherwise: "))
HELP2500 = float(input("Type 1 if you have taken HELP2500, and 0 otherwise: "))
HELP3001 = float(input("Type 1 if you have taken HELP3001, and 0 otherwise: "))

if (HELP2000 == 1 or HELP2001 == 1) and HELP2500 == 1 and HELP3001==0:
    print("You can take this course.")
else:
    print("You cannot take this course, sorry!")
````
