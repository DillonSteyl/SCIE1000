# The Input Function

When writing programs, it is often useful to prompt the user for input from the keyboard - this way, a program can be written so that it solves some general problem, and the user can enter different values each time the program is run. 

To take user input from the keyboard, the `float(input("message")` functions can be used - Python will display the `message`, and allow the user to enter a value in response. 

To assign this input to a variable, we use the following code:

```python
variable = float(input("message"))
```

Python will take the input from the user, turn it into a number, and assign the number to the `variable`. Let's take a look at a simple example:
```python
number = float(input("Give me a number: "))
print(number, "squared is", number**2)
```
This program asks the user for numerical input, and squares that number in response. Here is example output from this program:
```
Give me a number: 4
4 squared is 16
```

**Task:** Modify this program so that it will take the `width` and `height` of a rectangle as user input, and store those values in variables called `width` and `height`, respectively. Use the following *messages*:

* "Enter width: " for width
* "Enter height: " for height

Do not forget the space after the colon!

## Solution:
```python
from pylab import *

# Take width as input:
width = float(input("Enter width: "))
# Take height as input:
height = float(input("Enter height: "))

area = width*height
print("The area of the rectangle is:", area)
```
