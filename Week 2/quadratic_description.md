#Solving Quadratics

Students in high school often have to find solutions to quadratic formulas many times, and it gets pretty tiring. You're at University now, so let's streamline this. 

**Task:** For this exercise, you must write code that will find the two possible values of x that satisfy the following equation given a, b, and c:

``` 0 = a*x**2 + b*x + c ```

Ask the user for input and store the numbers as a, b, and c. Print the answers at the end given the print statements we provide. 

**Hint 1:** In case you have forgotten, your formulas should look like this, but using Python's operators.

x1 = (-b + (b<sup>2</sup> - 4ac)<sup>0.5</sup>)/(2a)

x2 = (-b - (b<sup>2</sup> - 4ac)<sup>0.5</sup>)/(2a)

**Hint 2:** Remember, you must use an asterisk (\*) between the variables and/or numbers you are multiplying, you can't leave it out like you can on paper!

Note: Python can handle imaginary numbers (where you take the square root of a negative number) perfectly fine, so don't worry about that. 

## Solution
```python
from pylab import *

a = float(input("The value of a: "))
b = float(input("The value of b: "))
c = float(input("The value of c: "))

x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print("The value of x1 is", x1, ", and the value of x2 is", x2)

```
