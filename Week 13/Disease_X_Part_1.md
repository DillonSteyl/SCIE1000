# Disease X (1)


You have been hired by the City of Atlantis to assist them in making decisions about infectious diseases. After learning about a new infectious disease, called Disease X, that has appeared in parts of Madagascar, you are worried that an outbreak could severely impact the city's population. 

Disease X has been shown to cause death for some people, and is highly infectious. You decide to run a quick simulation to see the impact a single infected person would cause. Here is everything you know about Atlantis and Disease X that will help you to run the simulation:

Infection rate (a): 2.5 per week (For 1 week, the number of new infections is `a*I*S/N`

Recovery rate (b): 0.5 per week (For 1 week, the number of new recoveries is `b*I`

Death rate (d): 0.0001 per week (For 1 week, the number of new deaths is `d*I`

Total population of Atlantis (N): 25000000

Initial Immune population (`R[0]`): 0

Initial Infected (`I[0]`): 1

Initial Susceptible (`S[0]`): 24999999

Initial Deceased (`[D]`): 0

**Task:** Use the initial values given to see the effect of a single infected person on the population of Madagascar, using an SIRD model. Use a while loop to calculate the changes in each of the groups over 20 weeks, with a step size of 0.1 week (that's overall 201 steps including step 0). Then, print the number of deaths and the maximum number of people infected at once using the print statements provided. Plot a graph of the population over time, with all four population groups. 

The title of your graph should be "Disease X". The lines should be labelled "Susceptible", "Infected", "Recovered", and "Deceased". Your x-axis should be labelled "Time", and your y-axis should be labelled "Population". Make sure you include a legend.

**Hint 1:** If you are having trouble with this task, a similar program is written in the textbook in the SIR section (near the end of the course). Note that it does not include the Deceased category, so you will have to take that into account.

**Hint 2:** You can find the maximum value of an array, A, by using the max function: max(A). 

**Solution**

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
