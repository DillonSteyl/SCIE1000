

There are many different equations that can be used to model population growth, a few of which you learn about in SCIE1000. One important concept is that often times populations will grow proportional to the current population size. There are multiple simple models we use for this, such as exponential, and compounding. Recall, they look like this:

Expontential: P<sub>i</sub> = P<sub>0</sub> x e<sup>k x i</sup>

Compounding: P<sub>i</sub> = P<sub>i-1</sub> x (1+k)

While you are practicing Python outside of class (HINT: you should do this!) with your study group, your friend argues that these two formulas are interchangeable when k is constant. You aren't quite sure if they're right, because while they are both based on the same concept, why would we even need two different equations if they were essentially the same?

**Task:** Investigate your friend's claim. Graph the two equations on the same axis with the same initial values. If the final values are the same, print "These two equations are interchangeable when k is constant." If they are not, print "These two equations are not interchangeable."

Don't forget to label your graph correctly, and use a legend. Don't change any variable names.

After passing this exercise, take a moment to think about your results. Are the two equations interchangeable? Why or why not? And if not, which equation is most suitable for modelling the growth of a savings account that collects interest monthly, and which is most suitable for modelling a population of bacteria that multiplies rapidly with no limit on resources.

**Hint:** The compounding formula can take another form when k is constant: P<sub>i</sub> = P<sub>0</sub> x (1+k)<sup>i</sup>

**Solution**

````
from pylab import *

P = 100 # initial population. Don't change this.
k = # choose a value for the growth rate between 0.01 and 0.2
n = # choose a value for the number of time steps between 5 and 20
time = # make an array of values from 0 to n-1 (inclusive)

exponential = # use exponential to store your population values for the exponential equation
compounding = # use compounding to store your population values for the compunding equation

# Use any method you like to fill the exponetial and compounding arrays. These arrays will be checked. 

# put your print statements here

# plot your graph here

````
