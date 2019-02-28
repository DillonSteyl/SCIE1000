from pylab import *

height = float(input("Enter your height: "))
adult = float(input("Enter 1 if you are accompanied by an adult, and 0 otherwise"))

if height<=200 and (height>=130 or (height>100 and adult==1)):
    print("Enjoy your ride!")
else:
    print("Sorry, you cannot ride this rollercoaster.")
