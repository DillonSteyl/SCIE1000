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
