# Linear Modelling Pratice

SCIE1000 contains a lot of modelling using linear equations. It's important to be able to quickly find a linear model based on a given data set, which requires practice. Unfortunately there are only so many tutorial questions. Luckily, we have the power to use Python to generate questions for us.

For this exercise you will write a program that helps the user practice modelling data with linear equations. The aim is to have a program that will generate a different data set each time for the user to model with a linear equation. Then, the user enters their values for the linear model, and the program will check if they are close enough to the real values. 

**Task:** 

Step 1: Display a graph for the user with the given x and y arrays. Name the x axis "x", and the y axis "y". Give the graph the title "Linear Model". Use black, circle markers ('o'), and no line. 

Step 2: Allow the user to input the m and c values, respectively.

Step 3: Check to see if the values are in the appropriate range: `0.8*actual_value <= entered_value <= 1.20*actual_value`

Step 4: If the user got both the values correct, print the message ("Both values are correct!"). If the user only got the m value correct, print the message ("The m value is correct, but the c value is not."). If the user got only the c value correct, print the message ("The c value is correct, but the m value is not."). If the user got both values wrong, print the message ("Both values are incorrect").

Step 5: Print the message ("The actual m value is", actual_m, "and the actual c value is", actual_c)



