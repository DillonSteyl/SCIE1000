from pylab import *

# Since we are randomly generating the questions, we need to use the random library
import random

# this function will randomly generate an m value between -0.2 and 0.2 (but not too small)
def generate_k():
    k = round(random.random()*0.4-0.2, 3)
    if abs(k)<0.04:
        return generate_k()    
    return(k)

# this function will randomly generate an A0 value between 0 and 20 (but not too small)
def generate_A0():
    A0 = round(random.random()*20)
    if abs(A0) <= 0.05:
        return generate_A0()
    return(A0)

# this function will generate a data set using the A0 and k values provided
def generate_data(k, A0):
    # the x values will be randomly chosen from 0 to 25
    x = array([random.randrange(25) for i in range(25)])
    
    # the y values will be calculated using y = A0*exp(k*x) * a random number to scatter
    y = array([A0*exp(k*i)*(0.9+random.random()*0.2) for i in x])
    return x, y
    
# the k and A0 values are randomly generated
k = generate_k()
A0 = generate_A0()

# the x and y arrays are randomly generated using k and A0
x, y = generate_data(k , A0)

# YOUR CODE HERE
