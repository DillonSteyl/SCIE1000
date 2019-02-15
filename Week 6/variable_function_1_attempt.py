from pylab import *


#functions for time dilation
def time_dilation(t, V):
    dilation = t * sqrt(1 - (V**2/299792458**2))
    return(dilation)

#input for time_dilation function
time = float(input("Enter the time: "))
velocity = float(input("Enter the velocity: "))

time_dilation(time, velocity)

print("The time dilation is", round(dilation))
