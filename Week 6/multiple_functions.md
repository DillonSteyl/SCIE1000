# Multiple Functions

You aren't limited to just one function per program. You can define many functions in your program and use them wherever you like (so long as you have defined them at the top of your program). Take a look at this example program:

```
from pylab import *

def sineDegrees(degrees):
    answer = sin(toRadians(degrees))
    return(answer)

def toRadians(degrees):
    radians = degrees * pi / 180
    return(radians)


degrees = float(input("Enter the degrees: ))

sineValue = sineDegrees(degrees)

print("The sine value is", sineValue)

```

There are two interesting things happening in this program. Firstly, there are two functions defined in the program. Secondly, the toRadians function is used in the sineDegrees function! It is no issue at all to use a function you wrote inside another function. In fact, you can actually call a function inside itself! This is called recursion, which you can learn about in other courses or online. 

When you begin to write longer and more complex programs, it is good practice to break the problem down into smaller problems using lots of functions. In fact, some styles of programming demand that almost the entire program is in different functions! Functions are great!

**Task:** Write three functions to calculate the weight of a person on different planets.

The first function will be called `toKilograms`, and will take a single number as input, and convert it from pounds to kilograms, and return it. 

The second function will be called `weightOnMars`, and will take the weight of a person on Earth in pounds as input, and return the weight of that person in kilograms if that person was on Mars. 

The third function will be called `weightOnMoon`, and will take the weight of a person on Earth in pounds as input, and return the weight of that person in kilograms if that person was on the Moon.

To calculate the weight of a person on a different planet, first you must convert that weight to kilograms, then multiply it by a coefficient. The coefficient for Mars is 0.38, and for the Moon it is 0.16. 

You should not have anything else in your program besides the import pylab statement and the three functions. 

