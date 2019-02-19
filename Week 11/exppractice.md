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
