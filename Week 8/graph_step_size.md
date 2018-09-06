# Step Sizes - Oscillatory Motion

Oscillatory motion is modelled using periodic functions. The motion of a spring is considered oscillatory when it is displaced from its equilibrium position. For example, if we have a spring and attach a weight to the end of it so that the spring stretches, and then release it from this position, the position of the weight as a function of time can be modelled as a sinusoidal function. With friction present, this motion is damped and eventually ceases, however for this problem we will assume there is no friction such that the spring follows a simple sinusoidal model.

Suppose we have a spring that is stretched to 0.5m away from its equilibrium position due to the presence of a weight at the end of the spring. Note that this change in displacement is represented as a **negative** value. When released, the weight position oscillates with a period of 0.5 seconds. 

**Task:**
We want to write a program that will plot the position of the weight **away** from the equilibrium position (in metres) as a function of time, for 10.5 seconds. We also want to investigate the effect of using different step sizes, to implement the plotting. You will need to plot the function with spacings of 0.01, 0.15 and 0.5 seconds. Time arrays holding the corresponding sample times will be labelled t1, t2, and t3 respectively, with corresponding variables x1, x2 and x3 that will map the weight's position.

This will require the following steps:
1.	Create an array for each set of sample times you will use for plotting, labelling them t1, t2, and t3. The first value in each array should be 0, and the last values should be 10.5. Step sizes should be 0.01, 0.15, and 0.5 for each array respectively.
2.	Create a model to determine the position of the weight. Each model will have a phase shift of 0.125 and a period of 0.5 in the model `Asin(2pi(t-D)/B) + C`. It is up to you to determine the amplitude from the context given. 
3.	Plot each function on the same graph. Add a vertical shift of 2 to the function x2 and a vertical shift of 4 to the function x3. This will not change the shape of your models, but will separate them vertically so you can easily see your results. 
4. Give your graph the title 'Oscillation of a spring", and label the x axis as 'Time (s)'.
5. Label each line of the plot using the following labels: '0.01s Samples', '0.15s Samples', '0.5s Samples'. Make sure you include a legend.

After you have completed the exercise, observe the efect of different step sizes on the appearances of the lines. With small step sizes, the line looks like the corresponding function. With larger step sizes, the lines will look jagged. With step sizes that are much to large, the line does no correspond well to the function at all. It's important to choose a step size that accurately displays the function, but does not take too long for the program to run. 

**Note:** You must plot the lines in the order x1, x2, x3, otherwise some tests may be failed.

## Solution
```python
from pylab import *

# Create your time arrays here:
t1 = arange(0,10.51,0.01)
t2 = arange(0,10.6,0.15)
t3 = arange(0,11,0.5)

# Create your models for position here:
x1 = 0.5*sin(4*pi*(t1-0.125))
x2 = 0.5*sin(4*pi*(t2-0.125))+2
x3 = 0.5*sin(4*pi*(t3-0.125))+4

# Produce your plot here:
plot(t1, x1, label='0.01s Samples')
plot(t2, x2, label='0.15s Samples')
plot(t3, x3, label='0.5s Samples')

title("Oscillation of a spring")
xlabel("Time (s)")

legend()
show()

# Do Not Modify Below This Line
savefig("output.png")
```
