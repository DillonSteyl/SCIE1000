

There are many different equations that can be used to model population growth, a few of which you learn about in SCIE1000. One important concept is that often times populations will grow proportional to the current population size. There are multiple simple models we use for this, such as exponential, and compounding. Recall, they look like this:

Expontential: P<sub>i</sub> = P<sub>0</sub> x e<sup>k x i</sup>

Compounding: P<sub>i</sub> = P<sub>i-1</sub> x (1+k)

While you are practicing Python outside of class (HINT: you should do this!) with your study group, your friend argues that these two formulas are interchangeable when k is constant. You aren't quite sure if they're right, because while they are both based on the same concept, why would we even need two different equations if they were essentially the same?

**Task:** Investigate your friend's claim. Graph the two equations on the same axis with the same initial values. If the final values rounded to five decimal places are the same, print "These two equations are interchangeable when k is constant." If they are not, print "These two equations are not interchangeable."

Don't forget to label your graph correctly, and use a legend. Don't change any variable names.

After passing this exercise, take a moment to think about your results. Are the two equations interchangeable? Why or why not? And if not, which equation is most suitable for modelling the growth of a savings account that collects interest monthly, and which is most suitable for modelling a population of bacteria that multiplies rapidly with no limit on resources.

**Hint 1:** The compounding formula can take another form when k is constant: P<sub>i</sub> = P<sub>0</sub> x (1+k)<sup>i</sup>
**Hint 2:** Don't forget the round() function. Example: round(2.24869231, 2) = 2.25

**Solution**

````
from pylab import *

P = 100
k = 0.05
n = 30
time = arange(0, n)

exponential = zeros(n)
compounding = zeros(n)

i = 0
while i<n:
    exponential[i] = P*exp(k*i)
    compounding[i] = P*(1+k)**(i)
    i = i + 1


if round(compounding[n-1], 5) == round(exponential[n-1], 5):
    print("These two equations are interchangeable when k is constant.")
else:
    print("These two equations are not interchangeable.")

plot(time, exponential, label="exponential")
plot(time, compounding, label="compounding")

title("Exponential vs Compounding)
xlabel("Time")
ylabel("Population")
legend()
show()

````
