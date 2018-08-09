from pylab import *

#A program to output whether a number is a perfect square number

number = float(input("Enter a number: "))

if number = 0:
    print("Zero is a special case")

elif number = 1:
    print("One is a special case")
    
else:

    i = 1.0
    while i <= number/2:
        if number / i = i: 
            print("The number", number, "is a perfect square of", i)
        i = i + 1
            
