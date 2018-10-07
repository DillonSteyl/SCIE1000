# Sine Wave Modelling












# Solution

```
from pylab import *

# Since we are randomly generating the questions, we need to use the random library
import random

# this function will randomly generate an m value between -10 and 10
def generate_a():
    return(random.randrange(0, 20))

# this function will randomly generate a c value that is between m/2 and 3m/2
def generate_b():
    return(random.randrange(8, 20))

# this function will randomly generate an m value between -10 and 10
def generate_c():
    return(random.randrange(-20, 20))

# this function will randomly generate a c value that is between m/2 and 3m/2
def generate_d(b):
    return(random.randrange(0, b))

# this function will generate a data set using the m and c values provided
def generate_data(a, b, c, d):
    # the x values will be randomly chosen from 0 to 25
    x = array([random.randrange(25) for i in range(60)])
    # the y values will be calculated using y = mx+c + a random number scaled using m
    y = array([random.gauss(a*sin(2*pi*(i - d)/b)+c, a/10) for i in x])
    return x, y
    
# the m and c values are randomly generated
a = generate_a()
b = generate_b()
c = generate_a()
d = generate_d(b)
# the x and y arrays are randomly generated using a, b, c, d
x, y = generate_data(a, b, c, d)
# the data is plotted using black circles
plot(x, y, 'ko')
grid(True)
xlabel("x")
ylabel("y")
title("Linear Model")
show()
print("Actual values -- a:", a, "-- b:", b,"-- c:", c, "-- d:",d)
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
    
if d-3<=d_guess<= d+3:
    print("The d value is close enough.")
else:
    print("The d value is incorrect.")
        
# tell the user the actual values
print("Actual values -- a:", a, "-- b:", b,"-- c:", c, "-- d:",d)


```
