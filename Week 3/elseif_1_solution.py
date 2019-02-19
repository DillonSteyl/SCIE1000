from pylab import *

age = float(input("Enter your age: "))
if age >= 21:
    print("You can legally drink, even in America!")
elif age >= 18:
    print("You can legally drink in Australia!")
else:
    print("You are under the legal drinking age.")
