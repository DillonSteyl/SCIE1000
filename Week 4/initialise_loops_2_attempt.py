from pylab import *

#calculating 2 to the power of x (input)
x = float(input("Input the number to calculate 2 to the power of: "))

power = 2

if x > 0:
    
    while i < x:
        power = power * 2.0
        i = i + 1

    print("2.0 to the power of", x, "is", power)
