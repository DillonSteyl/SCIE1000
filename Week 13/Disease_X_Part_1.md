# Disease X (1)


You have been hired by the City of Atlantis to assist them in making decisions about infectious diseases. After learning about a new infectious disease, called Disease X, that has appeared in parts of Madagascar, you are worried that an outbreak could severely impact the city's population. 

Disease X has been shown to cause death for some people, and is highly infectious. You decide to run a quick simulation to see the impact a single infected person would cause. Here is everything you know about Atlantis and Disease X that will help you to run the simulation:

Infection rate (a): 2.5 per week (For a single week (step size = 1), the number of new infections is `a*I*S/N`)

Recovery rate (b): 0.5 per week (For a single week (step size = 1), the number of new recoveries is `b*I`)

Death rate (d): 0.0001 per week (For a single week (step size = 1), the number of new deaths is `d*I`)

Total population of Atlantis (N): 25000000

Initial Immune population (`R[0]`): 0

Initial Infected (`I[0]`): 1

Initial Susceptible (`S[0]`): 24999999

Initial Deceased (`D[0]`): 0

**Task:** Your goal is to create 4 arrays called `S`, `I`, `R`, and `D`, storing the susceptable, infected, recovered (immune) and deceased populations of Atlantis respectively. You should use a while loop to calculate the population in each of these groups over 20 weeks with a step size of 0.1. This means that there are a total of 201 steps (including step 0). Your arrays should store **all** of these values.

Since the step size is not equal to 1, you must multiply the changes in the population by the step size to get the correct answer. 

Once you have the arrays calculated, modify the included print statements to print the **total number of deaths** and the **maximum number of infected people during a single step**.

**Hint:** You can use the `max(A)` function to print the maximum value of an array `A`.

**Solution**

```python
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
```
