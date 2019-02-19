from pylab import *

#This is a program to model the fish population over time in a non-competing environment

#growth value
r = 0.05

#initial number of fish
init = float(input("Input the initial number of fish: "))

#number of years to project for
years = float(input("Input the number of years to be modelled: "))

i=0

while i < years:
    if i==0:
        fish = init
    else:
         fish = (fish*(1+r))
    i = i + 1
    
