# Week 5 - Context Exercise 1

Suppose you are conducting an experiment based around a growth supplement you have developed and want to determine its effectiveness by testing the hormone on a group of rats. Before doing the experiment you want to model the expected outcome using Python and arrays.

You have three groups of rats, with 6 rats per group. Each group has a rat with each corresponding weight: 100g, 110g, 120g, 130g, 140g, 150g. 

Group 1 will be a control group, meaning they will have no access to the growth supplement. It is expected they will grow at a rate of 0.5g per day.

Group 2 will be given the supplement every day, and are expected to grow by 1% per day.

Group 3 will have occasional access to the supplement. There is expected to be an average growth of 1.8g every three days for each rat. 

Assuming the trial is run for 30 days, we want to determine the mass of each group of rats at the end of the trial. We also want to define an array containing the difference between the mass of groups 2 and 3 (mass of group 2 minus mass of group 3), called ‘growth_diff.’ Some hints are given below:

1. There are multiple ways to solve this problem, with or without loops. 
2. The formula for percentage growth rate after one iteration is `X*(1+p)`, where X is your inital population and p is your percentage growth rate expressed as a decimal (for example, 5% is expressed as 0.05). 
3. The formula for percentage growth rate after n interations is `X*(1+p)**n`.

Remember, store the final values for the mass in the arrays group1, group2, and group3. Store the growth difference array in an array called growth_diff.

## Solution
```python
from pylab import *

trial_days = 30 # A variable you might wish to use in your code
group1 = array([100.0,110.0,120.0,130.0,140.0,150.0])
group2 = array([100.0,110.0,120.0,130.0,140.0,150.0])
group3 = array([100.0,110.0,120.0,130.0,140.0,150.0])

group1 = group1 + (trial_days*0.5)
group2 = group2*(1.01)**trial_days
group3 = group3 + ((trial_days/3)*1.8)
growth_diff = group2-group3
```
