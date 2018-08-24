from pylab import *

#define the functions here
#def getLinearEquation
#def getExponentialEquation
    
    
x1 = float(input("What is the first x value: "))
y1 = float(input("What is the first y value: "))
x2 = float(input("What is the second x value: "))
y2 = float(input("What is the second y value: "))
choice = float(input("Enter 1 if you want to calculate a linear model, and 0 for exponential."))

if choice==1:
    m, c = getLinearEquation(x1, y1, x2, y2)
    print("The value of m is", m, "and the value of c is", c)
else:
    A0, k = getExponentialEquation(x1, y1, x2, y2)
    print("The value of A0 is", A0,"and the value of k is", k)
    
print("Thanks for using this program!")
