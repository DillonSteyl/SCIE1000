from pylab import *

def displacement(v0, a, t):
    x = (v0 * t) + (0.5 * a * t**2)
    return(x)
    
init_velocity = float(input("Initial velocity: "))
acceleration = float(input("Acceleration: "))
time = float(input("Time: "))
x = displacement(init_velocity, acceleration, time)
print("The displacement of this object at", time, "seconds is:", x, "metres.")
