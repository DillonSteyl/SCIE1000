from pylab import *

#calculating 2 to the power of x (input)
x = eval(input("Input the number to calculate 2 to the power of "))

power = 2

if x > 0:
    
    while i < x:
        power = power * 2
        i = i + 1

    print("2 to the power of", x, "is", power)
