from pylab import *

def getLinearEquation(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    c = y2 - m*x2
    return(m, c)
    
def getExponentialEquation(x1, y1, x2, y2):
    k = log(y1/y2)/(x1-x2)
    A0 = y2/(exp(k*x2))
    return(A0, k)
    
    
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
