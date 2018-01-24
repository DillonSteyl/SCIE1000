from pylab import *

''' calc function, used to implement the trapezoidal rule for one trapezoid
in a data set. '''
def calc(x1, x2, y1, y2):
	w = x2 – x1
	h = (y2 + y1)/2
	a = w * h
	return(a)

# Arrays containing dye dilution method data
t = array([0, 1, 2, 3, 4, 6, 10])
c = array([0, 34, 48, 19, 8, 1.2, 0])

# Define extra variables here as necessary: (You will need to do this!)

# While loop to implement the trapezoidal rule for all the data
while i <= 6:
    # Your code here:
