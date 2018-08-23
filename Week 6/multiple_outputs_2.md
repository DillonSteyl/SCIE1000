Multiple Outputs (2)

A program has been written but the functions have gone missing. Define and write the functions so that the program passes all the tests. 


```
from pylab import *

def getLinearEquation(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    c = y2 - m*x2
    return(m, c)
    
def getExponentialEquation(x1, y1, x2, y2):
    if x1 = 0:
        A0 = y1
        k = ln(y2/A0)/x2
    else:
        k = ln(y1/y2)/(x1-x2)
        A0 = y2/(exp(k*x2)
    return(round(A0), round(k,5))
    
    
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


```
