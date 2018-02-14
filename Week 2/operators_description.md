# Operators

Now that you know how to create, access, and modify variables, it is time to learn some of the basic arithmetic operators we can use on these variables. You've seen subtraction and multiplication already in the previous exercise. Here are all the basic arithmetic operators you should learn for SCIE1000:

```
addition = a+b 
subtraction = a-b 
multiplication = a*b 
division = a/b 
exponent = a**b 
```
Fun fact: there are actually over 30 operators in Python ( = is also an operator)! You will come across a few more in this course, but for now this will do.

Using these operators, you can now construct complex mathematical expressions just like you would on paper or your calculator. The order of operations you learned in school (BOMDAS, PODMAS, etc) is followed in Python, and you can use brackets as much as you like.

However, one important difference is that in Python you need an operator between each number/variable. That may not seem different at all, but recall that on paper we often omit multiplication signs (Writing 2pi instead of 2xpi). You cannot do this in Python, you must specify that the numbers are multiplied. So if you have strange errors come up in your expressions, check that there is an operator between each number and variable.

**Task:** Below are some mathematical expressions written in different ways, with a corresponding variable name. Use Python's operators to assign the expressions to the variables. You do not need to print anything.

Example: giraffes = one thousand plus (38 times 11)

In Python: ```` giraffes = 1000 + (38*11) ````

Here are the five expressions you need to write:

seconds_in_a_year = 60 times 60 times 24 times 365

rabbits = 2 to the power of 6

accuracy = (45 plus 38) divided by (45 plus 5 plus 12 plus 38)

money = 100 times (1 plus 0.05)<sup>12</sup>

interest = money minus 100

## Solution

````
from pylab import *

giraffes = 1000+(38*11)
seconds_in_a_year = 60*60*24*365
rabbits = 2**6
accuracy = (45+38)/(45+5+12+38)
money = 100*(1+0.05)**12
interest = money - 100

````




