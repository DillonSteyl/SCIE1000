# Modulo Operator (1)

Consider for a moment how you would write a program that can tell you if a number is even or odd. You could accomplish it by using some python functions (that you probably haven't learnt about yet), or maybe a while loop, but there is an easier way.

The modulo operator should be familiar to students who have taken some programming or discrete mathematics courses, but most likely it will be new to you. Simply put, it finds the remainder when two numbers are divided. It looks like this: `a%b`, and is often pronounced 'a mod b' or 'a modulo b'. This means, 'the remainder of a divided by b'.

Here are some examples to get you used to the concept:

````
13%10 = 3 # the remainder of 13 divided by 10 is 3
5%2 = 1 # the remainder of 5 divided by 2 is 1
15%5 = 0 # the remainder of 15 divided by 5 is 0
132127%2 = 1 # the remainder of 132127 divided by 2 is 1
124%5000 = 124 # the remainder of 124 divided by 5000 is 124
0%3 = 0 # the remainder of 0 divided by 3 is 0
````

(This works for negative numbers as well, but it's a bit hard to understand and it is not important for these exercises.)

Like with anything in Python, you can use an expression instead of a single variable or number, using brackets.

```
(3+8)%6 = 5 # because 3+8 = 11, and 11%6 is 5. 

```

This can be a very handy tool. Let's see how it solves our even/odd number problem.

````
number = float(input("Enter the number: "))

if number%2 == 0:
    print (number, "is even")
else:
    print(number, "is odd")

````
First, Python evaluates `number%2`. Then, it checks if the result is equal to 0, just like how any other conditional statement would work. If the condition is true (the remainder is 0), it prints the first statement. Otherwise it prints the second statement. This works because when a number is even, its remainder when divided by 2 should be 0. When it is odd, its remainder should be 1. 

Any number `a` that can be evenly divided by another number `b`, will have `a%b` equal to 0.

**Task:** Write a program that takes a single number as input from the user, and prints ("This is a happy number.") if divisible by 7, ("Close enough.") if its remainder when divided by 7 is 6, and prints ("This is a sad number.") otherwise.

