from pylab import *

#Program to print how many times an inputted number appears in the array

my_array = array([1,3,0,0,6,5,5,5,0,6])

number = float(input("Enter a number: "))

count = 0
i = 0
while i < 10:
    if my_array[i] == number:
        count = count + 1
    i = i + 1

print("The number", number, "appears in the array", count, "times")
