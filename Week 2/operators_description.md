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

Now that we know these operators, we can construct complex mathematical expressions just like we would on paper or our calculator. The order of operations you learned in school (BOMDAS, PODMAS, etc) is followed in Python, and you can use brackets as much as you like. Here is an example of all these concepts used together:



```
#starting amount
money = 1000
#amount in your bank account after 8 years given an annual interest rate of 3%, compounding monthly
new_money = money*(1 + (0.03/12))**(12*8)
#interest earned
interest = new_money - money
```

Now it's your go. For this exercise, you must write code that will find the two possible values of x that satisfy the following equation given a, b, and c:

``` 0 = a*x**2 + b*x + c ```

Please assign these two values of x to the variables, x1 and x2. Hint: you can find the square root of a number by putting it to the power of 0.5

Note, we will not be testing any values of a, b, and c that result in anything less than two real values for x, so don't worry about that. 

## Solution
```python
from pylab import *

#you will learn how this bit of code works in another exercise
a = eval(input("The value of a: "))
b = eval(input("The value of b: "))
c = eval(input("The value of c: "))
#but for now, do not change it

x1 = #put your first expression for x here
x2 = #put your second expression for x here, order not important

```
