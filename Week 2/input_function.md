# The Input Function

When writing programs, it is often useful to prompt the user for input from the keyboard - this way, a program can be written so that it solves some general problem, and the user can enter different values each time the program is run. 

To take user input from the keyboard, the `(input("message")` function can be used - Python will display the `message`, and allow the user to enter a value in response. 

To assign this input to a variable, we use the following code:

```python
variable = eval(input("message"))
```

Python will *evaluate* the input, and assign the evaluated value to the `variable`. Let's take a look at a simple example:
```python
number = eval(input("Give me a number: "))
print(number, "squared is", number**2)
```
This program asks the user for numerical input, and squares that number in response. Here is example output from this program:
```
Give me a number: 4
4 squared is 16
```

**Task:** Modify this program so that it will take the `width` and `height` of a rectangle as user input, and store those values in variables called `width` and `height`, respectively.

## Program:
```python
from pylab import *

# Take width as input:

# Take height as input:


area = width*height
print("The area of the rectangle is:", area)

```

## Solution:
```python
from pylab import *

# Take width as input:
width = eval(input("Enter width: "))
# Take height as input:
height = eval(input("Enter height: "))

area = width*height
print("The area of the rectangle is:", area)

```
