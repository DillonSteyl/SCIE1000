# 2.6 - Spot the Error (1)

```python
from pylab import *

#This is a program to calculate the hypotenuse of a triangle

#ANS: MISSING BRACKETS AT END OF INPUT LINES
a = eval(input("Enter the first side length of the triange: "))
b = eval(input("Enter the second side length of the triange: "))

h_squared = a**2 + b**2
h = h_squared**(1/2)

print("The third side length of the triangle is", h)
```

# 3.6 - Spot the Error (1)

```python
from pylab import *

#This is a program to output the size category of an adult dog based on its weight

weight = eval(input("Enter the weight of the dog in kg: "))

#ANS: MISSING COLONS AT THE END OF CONDITIONALS LINES
if weight<0:
    print("The weight is negative, this is not valid")
elif weight<5:
    print("The weight of this dog is that of a small breed dog")
elif weight<23:
    print("The weight of this dog is that of a medium breed dog")
else:
    print("The weight of this dog is that of a large breed dog")
```

# 3.7 - Spot the Error (2)

```python
from pylab import *

answer = eval(input("Answer to the Ultimate Question of Life, the Universe, and Everything"))

if answer == 42:
    #ANS: MISSING BRACKETS AROUND THE PRINT STATEMENT
    print("So long and thanks for all the fish")
```
