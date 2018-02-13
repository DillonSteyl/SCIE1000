

After running your simulation, you find that just under 5000 people would die if no action is taken after a single person becomes infected. As well, at the peak of the pandemic, around half the population would be sick. You inform the government about this and they are very alarmed.

Fortunately, a successful vaccine is developed in Europe for Disease X. The government says they will vaccinate 1000000 citizens per week, which they hope will be enough to significantly reduce the number of deaths. Will it be enough, or should they close the borders?

**Task:** Run your simulation again (you may borrow your code from the last exercise) but taking into account vaccinations. To do this, for each step calculate the new values for each of the groups as usual, and then move the vaccinated people from the Susceptible group to the Recovered group after. Recall, a step in your simulation is 0.1 weeks, so make sure to adjust your vaccination rate accordingly.

**Hint:** Make sure you do not vaccinate more people than exist in the Susceptible group - it should not drop below zero! Use an if/else statement to only vaccinate when there are people in the Susceptible group. 

Your while loop should look a bit like this:

````
 i = start
 while i<end:
     # calculate new S, I, R, D without vaccinations as in last exercise 
     # then, move vaccinated people from Susceptible to Recovered based on updated values (you need an if statement here)
     # i = i + 1
 
````

Use the same print statements and initial conditions as the last exercise. Good luck!

**Solution:**
````
from pylab import *

weeks = 20
N = 25000000
a = 2.5
b = 0.5
d = 0.0001
stepSize = 0.1
time = arange(0, weeks+0.1, stepSize)
numSteps = size(time)
S = zeros(numSteps)
I = zeros(numSteps)
R = zeros(numSteps)
D = zeros(numSteps)

S[0] = N - 1
I[0] = 1
R[0] = 0
D[0] = 0

i = 0
while i<numSteps-1:
    S[i+1] = S[i] + stepSize*(-a*S[i]*I[i]/N)
    I[i+1] = I[i] + stepSize*(a*S[i]*I[i]/N - b*I[i] - d*I[i])
    R[i+1] = R[i] + stepSize*(b*I[i])
    D[i+1] = D[i] + stepSize*(d*I[i])
    if S[i+1]<100000:
        R[i+1] = R[i+1] + S[i+1]
        S[i+1] = 0
    else:
        S[i+1] = S[i+1] - 100000
        R[i+1] = R[i+1] + 100000
    i = i+ 1
    
    
print("The total number of deaths is", D[numSteps-1])
print("The maximum number of people infected at once is", max(I))

plot(time, S, "g-", label="Susceptible")
plot(time, I, "b-", label="Infected")
plot(time, R, "k-", label="Recovered")
plot(time, D, "r-", label="Dead")
legend()
show()


# do not modify (this code is necessary for MyPyTutor to show output):
savefig("output.png")

````
