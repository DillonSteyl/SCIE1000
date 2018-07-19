from pylab import *

#This is a program to calculate the hypotenuse of a triangle

a = float(input("Enter the first side length of the triangle: ")
b = float(input("Enter the second side length of the triangle: ")

h_squared = a**2 + b**2
h = h_squared**(1/2)

print("The third side length of the triangle is", h)
