from pylab import *

# Since we are randomly generating the questions, we need to use the random library
import random

# this function will randomly generate an A value between 1 and 20
def generate_a():
    return(random.randrange(1, 20))

# this function will randomly generate a B value between 8 and 20
def generate_b():
    return(random.randrange(8, 20))

# this function will randomly generate a C value between -20 and 20
def generate_c():
    return(random.randrange(-20, 20))

# this function will randomly generate a D value between 0 and B
def generate_d(b):
    return(random.randrange(0, b))

# this function will generate a data set using a, b, c, d
def generate_data(a, b, c, d):
    # the x values will be randomly chosen from 0 to 25, there will be 100 of them
    x = array([random.random()*25 for i in range(100)])
    # the y values will be calculated 
    # using y = asin(2pi(x-d)/b) + c as mu and a/10 as sigma in a gaussian distribution
    y = array([random.gauss(a*sin(2*pi*(i - d)/b)+c, a/10) for i in x])
    return x, y
    
# the a, b, c, d values are randomly generated
a = generate_a()
b = generate_b()
c = generate_c()
d = generate_d(b)
# the x and y arrays are randomly generated using a, b, c, d
x, y = generate_data(a, b, c, d)

# the data is plotted using black circles
plot(x, y, 'ko')
grid(True)
xlabel("x")
ylabel("y")
title("Sine Wave")
show()

# the user guesses the a, b, c, d values
a_guess = float(input("Enter your a value: "))
b_guess = float(input("Enter your b value: "))
c_guess = float(input("Enter your c value: "))
d_guess = float(input("Enter your d value: "))


# let the user know if their guesses are close enough
if a-3<=a_guess<= a+3:
    print("The a value is close enough.")
else:
    print("The a value is incorrect.")

if b-3<=b_guess<= b+3:
    print("The b value is close enough.")
else:
    print("The b value is incorrect.")

if c-3<=c_guess<= c+3:
    print("The c value is close enough.")
else:
    print("The c value is incorrect.")
    
if d-2<=d_guess<= d+2:
    print("The d value is close enough.")
else:
    print("The d value is incorrect.")
        
# tell the user the actual values
print("Actual values -- a:", a, "-- b:", b,"-- c:", c, "-- d:",d)
