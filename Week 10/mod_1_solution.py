from pylab import *

number = float(input("Enter the number: "))

if number%7==0:
    print("This is a happy number.")
elif number%7==6:
    print("Close enough.")
else:
    print("This is a sad number.")
