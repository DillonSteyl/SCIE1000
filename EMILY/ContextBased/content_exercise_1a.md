# Context Exercise 1 - Part A
A patient’s cardiac output is estimated using the dye dilution method. A total of 8 mg of dye is injected into her heart, and the following arrays shows the measured concentrations of dye in her blood at given times as it leaves her heart.

```
t = array([0, 1, 2, 3, 4, 6, 10])
c = array([0, 34, 48, 19, 8, 1.2, 0])
```

Our goal is to write a program that will find the area under the curve of the data obtained from the dye dilution method, which can then be used to calculate the patient’s cardiac output.
The first step is writing a function that will help us complete this task. Modify this code so that the calc function will implement the trapezoidal rule, for **one** trapezoid within the data. Note that the parameters x1, x2, y1 and y2 are labelled appropriately to coincide with formulae taught in class.
