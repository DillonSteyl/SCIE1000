from pylab import *

year = 1

while year!=0:
    year = float(input("Enter the year you want to know about, or enter 0 to exit the program: "))
    if year!=0:
        print("Purchasing power:", 1000*(1.03)**(2018-year), "in year", year)

print("Thanks, and have a good day!")
