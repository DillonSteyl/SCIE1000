from pylab import *

# x-coordinates
X = arange(-2*pi, 2*pi, 0.05)
# function 1
Y1 = X**2
# function 2
Y2 = X**2 + 3*sin(12*X)

# Plot the Y1 line first
plot(X,Y1, 'g', label="y = x^2")
# plot the Y2 line second
plot(X,Y2,'r', label="y = x^2 + 3*sin(12x)")

# Add titles and axis labels
title("x^2 and x^2+3*sin(12x)")
xlabel("x")
ylabel("y")

#add a legend and grid lines
legend()
grid(True)
show()
