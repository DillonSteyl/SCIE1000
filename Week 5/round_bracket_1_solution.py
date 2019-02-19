from pylab import *

my_array = zeros(int(5))

i = 0
while i < 5:
    my_array[i] = [i+1] * 7
    i = i + 1

print(my_array)
