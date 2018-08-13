# Week 5 - Context Exercise 1

Let’s now apply all of our knowledge of arrays to solve the following problem.

Suppose you are conducting an experiment based around a growth supplement you have developed and want to determine its effectiveness by testing the hormone on a group of rats. Before doing the experiment you want to model the expected outcome using Python and arrays.

You have three groups of rats, with 6 rats per group. Each group has a rat with each corresponding weight: 100g, 110g, 120g, 130g, 140g, 150g. 

Group 1 will be a control group, meaning they will have no access to the growth supplement. It is expected they will grow at a rate of 0.5g per day.

Group 2 will be given the supplement every day, and are expected to grow by 1% per day.

Group 3 will have occasional access to the supplement. They will be given the supplement on every third day of the trial. For example, they are given the supplement on day 3, 6, 9, etc. There is expected to be a growth of 1.8g every three days for each rat. 

Assuming the trial is run for 30 days, we want to determine the mass of each group of rats at the end of the trial. We also want to define an array containing the difference between the mass of groups 2 and 3, called ‘growth_diff.’ Please do not print the arrays as output, but feel free to print them while testing your code. Some hints are given below:

1.	For group 2, you will have to use a while loop structure to update the masses as they are percentage dependent. 
2.	For groups 1 and 3 you don’t have to use a while loop, but can include these in the while loop if you would like. 
3.	Remember that percentage growth is calculated as follows: If a variable X is 10% larger than it was before, X is now equal to X + (0.1*X), where 0.1 is 10% as a decimal. The percentage growth is added to the initial value.
4.	When defining the initial array for growth_diff, the zeros() function will be useful.

## Solution
```python
from pylab import *

trial_days = 30 # A variable you might wish to use in your code
group1 = array([100.0,110.0,120.0,130.0,140.0,150.0])
group2 = array([100.0,110.0,120.0,130.0,140.0,150.0])
group3 = array([100.0,110.0,120.0,130.0,140.0,150.0])
growth_diff = zeros(int(6))

group1 = group1 + (trial_days*0.5)
group3 = group3 + ((trial_days/3)*1.8)

i = 0
while (i < trial_days):
    group2[i] = 0.01*group2[i] + group2[i]
    i = i + 1

growth_diff = abs(group2-group3)
```
