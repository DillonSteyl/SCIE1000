from pylab import *

def cylVolume(r,h):
    # calculate the volume of the cylinder:
    return( pi*r**2 * h )

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
# print cylinder volume:
print( cylVolume(radius, height) )
