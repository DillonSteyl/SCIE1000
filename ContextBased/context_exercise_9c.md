When it comes to programming, one of the most important rules is to not repeat yourself too much. If you have to do the same thing multiple times, then there is usually a better way to code it.

To continue helping the Republic of Madagascar solve their infectious disease problem, you will need to run a lot of simulations. Instead of copy pasting your code each time, why not write a function that will take all the input values and tell you everything you need to know. 

**Task:** Write a function that takes all necessary values as input, and runs the simulation like in the last exercise (with vaccinations). The function should be versatile - you should let the user choose whether or not they want to plot the simulation, and if they want important values printed. Return the number of deaths at the end of the function - this is the most important number. 

Everything should work the same as in the previous exercise, including the print statements. 

Of course, you may copy your code from the previous exercise. 

**Note:** Yes, this will be a big function! Good luck!

**Solution:**
````
from pylab import *

def runSimulation(weeks, N, a, b, d, v, stepSize, message, graph):
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
        if S[i+1]<v*stepSize:
            R[i+1] = R[i+1] + S[i+1]
            S[i+1] = 0
        else:
            S[i+1] = S[i+1] - v*stepSize
            R[i+1] = R[i+1] + v*stepSize
        i = i+ 1

    if message==1:
        print("The total number of deaths is", D[numSteps-1])
        print("The maximum number of people infected at once is", max(I))
    
    if graph==1:
        plot(time, S, "g-", label="Susceptible")
        plot(time, I, "b-", label="Infected")
        plot(time, R, "k-", label="Recovered")
        plot(time, D, "r-", label="Dead")
        legend()
        show()
  
    return D[numSteps-1]

# do not modify (this code is necessary for MyPyTutor to show output):
savefig("output.png")
````
