# Linear Modelling Pratice

SCIE1000 contains a lot of modelling using linear equations. It's important to be able to quickly find a linear model based on a given data set, which requires practice. Unfortunately there are only so many tutorial questions. Luckily, we can use Python to generate questions for us.


**Task:** You will write a program that helps the user practice modelling with linear equations. The aim is to have a program that will generate a different data set each time for the user to model with a linear equation. The user enters their values for the linear model, and the program will check if they are close enough to the real values. 

Step 1: Display a graph for the user with the given x and y arrays. Name the x axis "x", and the y axis "y". Give the graph the title "Linear Model". Use black, circle markers ('o'), and no line. Use grid lines.

Step 2: Allow the user to input the m and c values, respectively.

Step 3: Check to see if the values are in the appropriate range: `actual_value-3 <= entered_value <= actual_value+3`

Step 4: If the user got both the values correct, print the message ("Both values are close enough!"). If the user only got the m value correct, print the message ("The m value is close enough, but the c value is not."). If the user got only the c value correct, print the message ("The c value is close enough, but the m value is not."). If the user got both values wrong, print the message ("Both values are not close enough.").

Step 5: Print the message ("The actual m value is", actual_m, "and the actual c value is", actual_c)


# Solution
```
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

# the data is plotted using blakc circles
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

```
