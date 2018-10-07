from pylab import *

# Since we are randomly generating the questions, we need to use the random library
import random

# this function will randomly generate an m value between -10 and 10
def generate_m():
    return(round(random.random()*20-10))

# this function will randomly generate a c value that is between m/2 and 3m/2
def generate_c(m):
    return(round(random.random()*m+m/2))

# this function will generate a data set using the m and c values provided
def generate_data(m, c):
    # the x values will be randomly chosen from 0 to 25
    x = array([random.randrange(25) for i in range(25)])
    # the y values will be calculated using y = mx+c + a random number scaled using m
    y = array([((m*i+c+(random.random()-0.5)*5*m)) for i in x])
    return x, y
    
# the m and c values are randomly generated
m = generate_m()
c = generate_c(m)
# the x and y arrays are randomly generated using m and c
x, y = generate_data(m , c)

# YOUR CODE HERE
