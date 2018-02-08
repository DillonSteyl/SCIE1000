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

Using these operators, you can now construct complex mathematical expressions just like you would on paper or your calculator. The order of operations you learned in school (BOMDAS, PODMAS, etc) is followed in Python, and you can use brackets as much as you like. Here is an example of all these concepts used together:



```
#starting amount
money = 1000
#amount in your bank account after 8 years,
#given an annual interest rate of 3%, compounding monthly
new_money = money*(1 + (0.03/12))**(12*8)
#interest earned
interest = new_money - money
```

Now it's your go. For this exercise, you must write code that will find the two possible values of x that satisfy the following equation given a, b, and c:

``` 0 = a*x**2 + b*x + c ```

Your formulas should look like this, but using Python's operators.

x1 = (-b + (b<sup>2</sup> - 4ac)<sup>0.5</sup>)/2a

x2 = (-b - (b<sup>2</sup> - 4ac)<sup>0.5</sup>)/2a

Hint: you must use an asterisk (\*) between the variables you are multiplying, you can't leave it out like you can on paper!

Note, we will not be testing any values of a, b, and c that result in imaginary numbers, so don't worry about that. 

## Solution
```python
from pylab import *

#you will learn how this bit of code works in another exercise
a = eval(input("The value of a: "))
b = eval(input("The value of b: "))
c = eval(input("The value of c: "))
#but for now, do not change it

x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print("The value of x1 is", x1, ", and the value of x2 is", x2)

```
