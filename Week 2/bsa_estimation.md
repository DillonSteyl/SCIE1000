# Body Surface Area Estimation

In the tutorial sheets this week, you learned about some ways to estimate the Body Surface Area (BSA) of a person, based only on their mass (kg) and their height (cm). There are many formulae to do this. 

This program estimates the BSA of a person of a given height and mass using the **Mostellar** and **Dubois & Dubois** formulae. Modify this program so that it also calculates their estimated BSA using the **Haycock** formula, and prints this estimation below the other two. 

The **Haycock** formula, for a person of mass *M* (kg) and height *H* (cm) is as follows:
BSA = 0.024265 x H<sup>0.3964</sup> x M<sup>0.5378</sup>

Make sure you use the *variable names* when writing the formula, not the actual numerical values!

```python

mass = 70
height = 175

mostellar_bsa = 0.0167*sqrt(mass*height)
dubois_bsa = 0.007184 * mass**0.425 * height**0.725


print(mostellar_bsa)
print(dubois_bsa)


```