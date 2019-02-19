# Body Surface Area Estimation

In the tutorial sheets this week, you learn about some ways to estimate the Body Surface Area (BSA) of a person, based only on their mass (kg) and their height (cm). There are many formulae to do this. 

This program estimates the BSA of a person of a given height and mass using the **Mostellar** and **Dubois & Dubois** formulae. Another formula that can be used to estimate the BSA of a person is the **Haycock** formula.
The Haycock formula, for a person of mass *M* (kg) and height *H* (cm) is as follows:

BSA = 0.024265 x H<sup>0.3964</sup> x M<sup>0.5378</sup>

**Task:** Modify this program so that it also calculates the estimated BSA using the **Haycock** formula (`haycock_bsa`). Your program should also print out the Haycock estimation below the other two estimations, with the following format:
```
Haycock BSA Estimate: (value)
```
In addition, you will need to modify the program on the left so that it prompts the user to input mass and height, respectively. Use the following input messages:

* "Enter mass: " for mass
* "Enter height: " for height
