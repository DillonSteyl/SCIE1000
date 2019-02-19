# Sine Wave Modelling

Sine waves have the following structure:

` y = A*sin(2*pi*(x - D)/B) + C`

Where A is the amplitude, B is the period, C is the vertical shift, and D is the phase (horizontal) shift. While D can be negative, only positive D values will be used for this program. 

**Task:** You will write a program that helps the user practice modelling with sine waves. The aim is to have a program that will generate a different data set each time for the user to model with a sine wave. The user enters their values for the sine wave, and the program will check if they are close enough to the real values.

The functions to generate the random dataset are already written and used in the program. You do not need to understand how these work. All you need to do is complete the rest of the program as follows:

**Step 1**: Display a graph for the user with the given x and y arrays. Name the x axis "x", and the y axis "y". Give the graph the title "Sine Wave". Use black, circle markers ('o'), and no line. Use grid lines.

**Step 2**: Allow the user to input the A, B, C, and D values, respectively.

**Step 3**: Check to see if the A value is in the appropriate range: actual_value-3 <= entered_value <= actual_value+3

**Step 4**: If the user got the A value close enough, print the message ("The A value is close enough."). Otherwise, print the message ("The A value is incorrect.")

**Step 5**: Check to see if the B value is in the appropriate range: actual_value-3 <= entered_value <= actual_value+3

**Step 6**: If the user got the B value close enough, print the message ("The B value is close enough."). Otherwise, print the message ("The B value is incorrect.")

**Step 7**: Check to see if the C value is in the appropriate range: actual_value-3 <= entered_value <= actual_value+3

**Step 8**: If the user got the C value close enough, print the message ("The C value is close enough."). Otherwise, print the message ("The C value is incorrect.")

**Step 9**: Check to see if the D value is in the appropriate range: actual_value-2 <= entered_value <= actual_value+2

**Step 10**: If the user got the D value close enough, print the message ("The D value is close enough."). Otherwise, print the message ("The D value is incorrect.")

**Step 11**: Finally, print the message ("Actual values -- a:", a, "-- b:", b,"-- c:", c, "-- d:", d)
