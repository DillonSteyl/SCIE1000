# Context Exercise 1 - Part A
A patient’s cardiac output is estimated using the dye dilution method. A total of 8 mg of dye is injected into her heart, and the following arrays shows the measured concentrations of dye in her blood at given times as it leaves her heart.

```
t = array([0, 1, 2, 3, 4, 6, 10]) # seconds
c = array([0, 34, 48, 19, 8, 1.2, 0]) # mg/L
```

Our goal is to write a program that will find the area under the curve of the data obtained from the dye dilution method, which can then be used to calculate the patient’s cardiac output.

This requires implementing the following steps:
1. Write a function that will help us complete this task. Modify this code so that the calc function will implement the trapezoidal rule, for one trapezoid within the data. Note that the parameters x1, x2, y1 and y2 are labelled appropriately to coincide with formulae taught in class.
2. Use the calc function to find the area under the curve of the data obtained from the dye dilution method. print your result with the format AUC = **ANSWER**.
3. Use this result obtained from implementing the trapezoidal rule over all the dye dilution method data to find the cardiac output of the patient, in the units of litres per minute. Remember that the total dye injected into the patient's heart is 8mg. Consider using dimensional analysis to help you understand how to calculate this value. 

Modify the code below as indicated below. 
