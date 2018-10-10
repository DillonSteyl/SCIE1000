# Exponential Modelling

Exponential functions have the following basic structure:

` y = A0 * e^(k*x)`

Exponential functions can be more complex (for example, including c and d values), but for this exercise we will only be using the basic exponential structure (where k will be positive or negative, and A0 will only be positive).

**Task:** You will write a program that helps the user practice modelling with exponential equations. The aim is to have a program that will generate a different data set each time for the user to model with an exponential equation. The user enters their values for the exponential model, and the program will check if they are close enough to the real values.

The functions to generate the random dataset are already written and used in the program. You do not need to understand how these work. All you need to do is complete the rest of the program as follows:

**Step 1:** Display a graph for the user with the given x and y arrays. Name the x axis "x", and the y axis "y". Give the graph the title "Exponential Model". Use black, circle markers ('o'), and no line. Use grid lines.

**Step 2:** Allow the user to input their guesses for the A0 and k values, respectively.

**Step 3:** Check to see if the A0 value is in the appropriate range: actual_value-3 <= entered_value <= actual_value+3

**Step 4:** If the user got the A0 value close enough, print the message ("The A0 value is close enough."). Otherwise, print the message ("The A0 value is incorrect.")

**Step 5:** Check to see if the k value is in the appropriate range: actual_value-0.03 <= entered_value <= actual_value+0.03

**Step 6:** If the user got the k value close enough, print the message ("The k value is close enough.") Otherwise, print the message ("The k value is incorrect.")

**Step 7:** Finally, print the message ("The actual A0 value is", actual_A0, "and the actual k value is", actual_k)


# Solution
```
from pylab import *

# Since we are randomly generating the questions, we need to use the random library
import random

# this function will randomly generate an m value between -0.15 and 0.15 (but not too small)
def generate_k():
    k = round(random.random()*0.3-0.15, 3)
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
x, y = generate_data(k, A0)

# the data is plotted using black circles
plot(x, y, 'ko')
grid(True)
xlabel("x")
ylabel("y")
title("Exponential Model")
show()

# the user guesses the A0 and k values
A0_guess = float(input("Enter your A0 value: "))
k_guess = float(input("Enter your k value: "))


# let the user know if their guesses are close enough  
if A0-3<=A0_guess<= A0+3:
    print("The A0 value is close enough.")
else:
    print("The A0 value is incorrect.")

if k-0.03<=k_guess<= k+0.03:
    print("The k value is close enough.")
else:
    print("The k value is incorrect.")



        
# tell the user the actual values
print("The actual A0 value is", A0, "and the actual k value is", k)
```
