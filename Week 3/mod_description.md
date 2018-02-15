## Modulo Operator

Consider for a moment how you would write a program that can tell you if a number is even or odd. You could accomplish it by using some python functions (that you probably haven't learnt about yet), but there is an easier way.

The modulo operator should be familiar to students who have taken some programming or discrete mathematics courses, but most likely it will be new to you. Simply put, it finds the remainder when two numbers are divided. It looks like this: a%b, and is often pronounced 'a mod b'. 

Here are some examples to get you used to the concept:

````
13%10 = 3
5%2 = 1
15%5 = 0
132127%2 = 1
124%5000 = 124
0%3 = 0
````
This can be a very handy tool. Let's see how it solves our even/odd number problem.

````
number = eval(input("Enter the number: "))

if number%2==0:
    print (number, "is even")
else:
    print(number, "is odd")

````
First, Python evaluates 'number%2'. Then, it checks if the result is equal to 0. This works because when a number is even, its remainder when divided by 2 should be 0. When it is odd, its remainder should be 0. 

**Task:** Write a program that takes a single number as input, and prints "This is a happy number." if divisible by 7, "Close enough." if its remainder when divided by 7 is 6, and prints "This is a sad number." otherwise.


## Solution
````
from pylab import *

number = eval(input(("Enter the number: "))

if number%7==0:
    print("This is a happy number.")
elif number%7==6:
    print("Close enough.")
else:
    print("This is a sad number.")


````


