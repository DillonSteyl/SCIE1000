When programming, it is important to know at least a bit about what is going on in the computer's brain. Specifically, how things are stored on computers, and how computers move things around and make operations. This is a very complex topic, and fortunately we will only scrape the surface in SCIE1000. 

Python (and many other programming languages for that matter) have various different ways to store numbers, for all kinds of situations. In this course we will look at two: int and float. 

Int should be familiar to you, as it stands for 'Integer'. Integers are numbers that do not have any decimal places. For example: 0, 5, 38, -100, 49, -12. The number 38.5 is not an integer, because it has one decimal place (nor is 18.214212, -0.00001, 132.052, pi, 8.0, e, sqrt(2)).

A 'float' (known as a floating point number), is a number that **can** have decimal places. For example: 0.0, -5.0, 5.5, 38.2, 12.2432, -42.001, sqrt(2). Remember that Python can store whole numbers as floats (like 0.0, 2.0, -3.0, etc), but these are stored differently to their integer counterparts (0, 2, -3, etc). 

When writing numbers in your programs, Python will try to figure out if it should store the number as an integer or a float. The rule is simple: if it has a '.' in it, it's a float. Otherwise, it is an integer. There is one exception: if you are using the division operator, then your answer will be a float even if the numbers divide evenly. 

Here are some examples:

1 #int
1.0 #float
0 #int
0.0 #float
0.001 #float
-1.234 #float
-15 #int
6/3 #float equal to 2.0
5/2 #float equal to 2.5

It is important to remember this difference because some functions in python will only work with integers, and in other cases you have no choice but to use float. Most mathematical functions (sqrt, log, exp, etc) will only return floats (but you can give them either integers or floats to use). 

So what happens if we are given a float, but we actually need an int? There's a function for that! Here is how it works:

a = 5.0
b = int(a)

This will make b equal to the integer 5. Great! But what if the number already has decimal places? When you use the int() function, Python will give you the integer before the decimal, and discard all numbers after the decimal. For example:

a = 3.8
b = int(a)

This will make b equal to the integer 3. Not 4. The int() function does not round. 

We can also do this in reverse, and turn an int into a float:

a = 5
b = float(a)

This will make b equal to the float 5.0. Float won't add anything but 0 for the decimal place, so that's easy. 

**Task:** We will give you a set of numbers, and you must print them in the correct section: int or float.

For example, given the numbers 5, 5.0, -2.38, -12, int(12.5), 10/2, sqrt(2), float(8):

print("These are the integers:")
print(5)
print(-12)
print(int(12.5))
print("These are the floats:")
print(5.0)
print(-2.38)
print(10/2)
print(sqrt(2))
print(float(8))

Here are your numbers:

3, 4/4, -13.2, sqrt(16), int(15.9), 100.0, float(7), -6, int(1), float(1.0)

Make sure to keep the numbers in the order given (within their sections), like in the example. 

## Solution

print("These are the integers:")
print(3)
print(int(15.9))
print(-6)
print(int(1))
print("These are the floats:")
print(4/4)
print(-13.2)
print(sqrt(16))
print(100.0)
print(float(7))
print(float(1.0))
