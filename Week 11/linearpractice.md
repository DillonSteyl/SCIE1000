# Linear Modelling Pratice

SCIE1000 contains a large amount of modelling using linear, exponential, and sine wave equations. It's important to be able to quickly find the equation for a model based on a given data set, but this requires practice. Unfortunately, there are only so many tutorial questions to practice on. Luckily, we can use Python to generate questions for us.

In the following exercises you will write programs that generate practice questions for linear, exponential, and sine wave models. We have already written the code to randomly generate the data sets, so all you have to do is write the code to interact with the user.

**Task:** You will write a program that helps the user practice modelling with linear equations. The aim is to have a program that will generate a different data set each time for the user to model with a linear equation. The user enters their values for the linear model, and the program will check if they are close enough to the real values. 

The functions to generate the random data set are already written and used in the program. You do not need to understand how these work. All you need to do is complete the rest of the program as follows:

**Step 1:** Display a graph for the user with the given x and y arrays. Name the x axis "x", and the y axis "y". Give the graph the title "Linear Model". Use black, circle markers ('o'), and no line. Use grid lines.

**Step 2:** Allow the user to input their guesses for the m and c values, respectively. (That should be two input statements.)

**Step 3:** Check to see if the values are in the appropriate range: `actual_value-3 <= entered_value <= actual_value+3`

**Step 4:** If the user got both the values correct, print the message ("Both values are close enough!"). If the user only got the m value correct, print the message ("The m value is close enough, but the c value is not."). If the user got only the c value correct, print the message ("The c value is close enough, but the m value is not."). If the user got both values wrong, print the message ("Both values are not close enough.").

Step 5: Print the message ("The actual m value is", actual_m, "and the actual c value is", actual_c)
