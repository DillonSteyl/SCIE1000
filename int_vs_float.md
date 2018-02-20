When you define or modify a variable, that variable will have a 'type'. There a different variable types for different uses: such as for numbers, or for words. In this exercise, we will introduce to you ints and floats, which are two types of numbers in Python.

Int should be familiar to you, as it stands for 'Integer'. Integers are numbers that do not have any decimal places. For example: 0, 5, 38, -100, 49, -12. The number 38.5 is not an integer, because it has one decimal place.

A float (known as a floating point number), is a number that **can** have decimal places. For example: 0.0, -5.0, 5.5, 38.2, 12.2432, -42.001. 

Python stores floats and ints differently on your computer, even when they are mathematically the same thing. For example, 3 vs 3.0. The first is an int, the second is a float. Even though they mean the same to us, they mean different things to the computer.

When writing numbers in your programs, Python will try to figure out if it should store the number as an int or a float. The rule is simple: if it has a '.' in it, it's a float. Otherwise, it is an integer.

Here are some examples:

1 #int
1.0 #float
0 #int
0.0 #float
0.001 #float
-1.234 #float
-15 #int
.2 #float equal to 0.2
2. #float equal to 2.0

It is important to remember this difference because some functions in python will only work with integers, and in other cases you have no choice but to use floats. Most mathematical functions (sqrt, log, exp, etc) will only return floats (but you can give them either integers or floats to use). When you divide two numbers, even if they are ints, the answer will always be a float.

So what happens if we are given a float, but we actually need an int? There's a function for that! Here is how it works:

a = 5.0
b = int(a)

This will make b equal to the integer 5. Great! But what it isn't a whole number? When you use the int() function, Python will give you the integer before the decimal, and discard all numbers after the decimal. For example:

a = 3.8
b = int(a)

This will make b equal to the integer 3. Not 4. **The int() function does not round properly.** There is a function specifically for rounding numbers (round()), which you will learn about in a different exercise. 

We can also convert an int into a float:

a = 5
b = float(a)

This will make b equal to the float 5.0. Float won't add anything but 0 for the decimal place, so that's easy. 

**Task:** We will give you a set of numbers, and you must print them in the correct section: int or float.

For example, given the numbers 5, 5.0, -2.38, -12, int(12.5), 10/2, 3., sqrt(2), float(8):

print("These are the integers:")
print(5)
print(-12)
print(int(12.5))
print("These are the floats:")
print(5.0)
print(-2.38)
print(10/2)
print(3.)
print(sqrt(2))
print(float(8))

Here are the numbers for you to print:

3, 4/4, -13.2, sqrt(16), int(15.9),  8., .8, 100.0, float(7), -6, int(1), float(1.0);

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
print(8.)
print(.8)
print(100.0)
print(float(7))
print(float(1.0))
