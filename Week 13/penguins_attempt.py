from pylab import *
#put your highest(A) function here

# initialise the arrays
F = zeros(16)
P = # your code here

# put in the initial values
F[0] = 50
P[0] = # your code here

# start the while loop at 1, because the 0th element has already been filled in
i = 1

#fill in the arrays
while i<16:
    F[i] = max(-2*i*(i-8) + 50, 0) #fish formula, do not edit
    P[i] = # your code here
    i = i + 1
    
maxIndex = # your code here for the quarter with the most amount of fish
penguinsAtMax = # your code here for the number of penguins for that quarter

print("The quarter with the highest number of fish is", maxIndex, "with", penguinsAtMax, "penguins on the island at the time.")
