from pylab import *

a = float(input("The value of a: "))
b = float(input("The value of b: "))
c = float(input("The value of c: "))

x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print("The value of x1 is", x1, ", and the value of x2 is", x2)
