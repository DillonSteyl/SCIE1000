from pylab import *

height = zeros(int(12))
height[0] = 10

i = 1
while i<12:
    height[i] = round(height[i-1]*(1.2+0.4*sin(2*pi*i/4)))
    i = i + 1
