from pylab import *

trial_days = 30 # A variable you might wish to use in your code
group1 = array([100.0,110.0,120.0,130.0,140.0,150.0])
group2 = array([100.0,110.0,120.0,130.0,140.0,150.0])
group3 = array([100.0,110.0,120.0,130.0,140.0,150.0])

group1 = group1 + (trial_days*0.5)
group2 = group2*(1.01)**trial_days
group3 = group3 + ((trial_days/3)*1.8)
growth_diff = group2-group3
