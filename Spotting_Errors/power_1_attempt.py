from pylab import *

def power(a,b):
    # returns a to the power of b
    return(a^b)

a = eval(input("Enter the base: "))
b = eval(input("Enter the power: "))

print("The answer is", power(a,b))
