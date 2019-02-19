from pylab import *

i = -3
while i <= 3:
    if i < 0:
        print("Negative:", i)
    elif i == 0:
        print("Zero:", i)
    else:
        print("Positive:", i)
    i = i + 1
