from pylab import *

i = 1
while i <=12:
    print("Average temperature for month", i, "is", 3*sin((i+2)*2*pi/12)+25)
    i = i + 1
