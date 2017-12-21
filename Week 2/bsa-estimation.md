# Body Surface Area Estimation

In the tutorial sheets this week, you learned about some ways to estimate the Body Surface Area (BSA) of a person, based only on their mass (kg) and their height (cm). There are many formulae to do this. 

This program estimates the BSA of a person of a given height and mass using the **Mostellar** and **Dubois & Dubois** formulae. Another formula that can be used to estimate the BSA of a person is the **Haycock** formula.
The Haycock formula, for a person of mass *M* (kg) and height *H* (cm) is as follows:

BSA = 0.024265 x H<sup>0.3964</sup> x M<sup>0.5378</sup>

**Task:** Modify this program so that it also calculates their estimated BSA using the **Haycock** formula. Your program should also print out the Haycock estimation below the other two estimations, with the following format:
```
Haycock BSA Estimate: (value)
```
In addition, you will need to modify the program below so that it prompts the user to input mass and height, respectively.

## Program
```python
from pylab import *

# Input mass:

# Input height:


# Calculate BSA Estimates
mostellar_bsa = 0.0167*sqrt(mass*height)
dubois_bsa = 0.007184 * mass**0.425 * height**0.725

# Print BSA Estimates
print("Mostellar BSA Estimate:", mostellar_bsa)
print("Dubois BSA Estimate:", dubois_bsa)

```

## Solution
```python
from pylab import *

# Input mass:
mass = eval(input("Enter mass: "))
# Input height:
height = eval(input("Enter height: "))

# Calculate BSA Estimates
mostellar_bsa = 0.0167*sqrt(mass*height)
dubois_bsa = 0.007184 * mass**0.425 * height**0.725
haycock_bsa = 0.024265 * height**0.3964 * mass**0.5378

# Print BSA Estimates
print("Mostellar BSA Estimate:", mostellar_bsa)
print("Dubois BSA Estimate:", dubois_bsa)
print("Haycock BSA Estimate:", haycock_bsa)

```
