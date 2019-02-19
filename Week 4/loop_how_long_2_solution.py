from pylab import *

number = 1
usersNumber = 1
while usersNumber!=0:
    usersNumber = float(input("Give me a number, or enter 0 to exit the program: "))
    if usersNumber!=0:
        number = number*usersNumber


print("The final answer is", number)
