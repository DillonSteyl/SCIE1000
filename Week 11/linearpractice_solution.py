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

# the data is plotted using black circles
plot(x, y, 'ko')
grid(True)
xlabel("x")
ylabel("y")
title("Linear Model")
show()

# the user guesses the m and c values
m_guess = float(input("Enter your m value: "))
c_guess = float(input("Enter your c value: "))


# let the user know if their guesses are close enough
if m-3<=m_guess<= m+3:
    if c-3<=c_guess<= c+3:
        print("Both values are close enough!")
    else:
        print("The m value is close enough, but the c value is not.")
else:
    if c-3<=c_guess<= c+3:
        print("The c value is close enough, but the m value is not.")
    else:
        print("Both values are not close enough.")
        
# tell the user the actual values
print("The actual m value is", m, "and the actual c value is", c)
