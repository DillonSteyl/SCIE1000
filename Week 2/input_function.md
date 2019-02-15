# The Input Function

When writing programs, it is often useful to prompt the user for input from the keyboard - this way, a program can be written so that it solves some general problem, and the user can enter different values each time the program is run. 

To take user input from the keyboard, the `float(input("message"))` functions can be used. Python will display the `message`, and allow the user to enter a value in response. 

To assign this input to a variable, we use the following code:

```python
variable = float(input("message"))
```

This line of code contains four important parts: `variable`, `float`, `input`, and `message`. First, `input` tells Python to display the `message` to the user - essentially whatever is written between the quotation marks, like a print statement. The user will enter something into the box or line provided, and press enter. Then, `float` tells Python that this input should be a number. And finally, the number is stored using the `variable` name provided.

That can be a bit confusing at first, but it's actually super easy to use. Let's take a look at a simple example:


```python
number = float(input("Give me a number: "))
print(number, "squared is", number**2)
```

This program asks the user for numerical input, and squares that number in response. Here is example output from this program, where the user typed the number 4 and pressed enter:

```
Give me a number: 4
4 squared is 16
```

**Important Note:** Due to the quirkiness of the Python language, sometimes you will have to use `int` instead of `float`. The reasons for this are beyond the scope of this course, but we will make sure to tell you when you must use `int`. Luckily it wont happen often, so you should be using `float` every time, unless stated otherwise.

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
