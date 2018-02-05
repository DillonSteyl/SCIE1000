# Spot the Error

**Task:** Find and fix the error in the following code

**Hint:** Take a closer look at the input statements

## Program
```python

print("this is a program to calculate the hypotenuse of a triangle")

a = eval(input("Enter the first side length of the triange: ")
b = eval(input("Enter the second side length of the triange: ")

h_squared = a**2 + b**2
h = h_squared**(1/2)

print("The third side length of the triangle is", h)

```

## Solution
```python

print("this is a program to calculate the hypotenuse of a triangle")

#missing brackets to end both input statements
a = eval(input("Enter the first side length of the triange: "))
b = eval(input("Enter the second side length of the triange: "))

h_squared = a**2 + b**2
h = h_squared**(1/2)

print("The third side length of the triangle is", h)

```
