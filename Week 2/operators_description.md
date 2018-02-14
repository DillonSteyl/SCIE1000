

Now it's your go. For this exercise, you must write code that will find the two possible values of x that satisfy the following equation given a, b, and c:

``` 0 = a*x**2 + b*x + c ```

Your formulas should look like this, but using Python's operators.

x1 = (-b + (b<sup>2</sup> - 4ac)<sup>0.5</sup>)/(2a)

x2 = (-b - (b<sup>2</sup> - 4ac)<sup>0.5</sup>)/(2a)

**Hint:** you must use an asterisk (\*) between the variables and/or numbers you are multiplying, you can't leave it out like you can on paper!

Note, we will not be testing any values of a, b, and c that result in imaginary numbers, so don't worry about that. 

## Solution
```python
from pylab import *

#you will learn how this bit of code works in another exercise
a = eval(input("The value of a: "))
b = eval(input("The value of b: "))
c = eval(input("The value of c: "))
#but for now, do not change it

#you can use the variables a, b, and c in your code
x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print("The value of x1 is", x1, ", and the value of x2 is", x2)

```
