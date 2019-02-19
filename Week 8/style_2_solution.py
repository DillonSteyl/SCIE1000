from pylab import *

X = arange(0, 10.1, 0.1)
Y1 = -0.2*X + 2
Y2 = 0.2*X - 2
Y3 = (-0.2*X+2)*(sin(X))
Y4 = (0.2*X-2)*(sin(X))

plot(X, Y1, marker='x', linestyle=':', color='k')
plot(X, Y2, marker='x', linestyle=':', color='k')
plot(X, Y3, color='c')
plot(X, Y4, color='c')
title("Functions of X and Y")
xlabel("X value")
ylabel("Y value")

show()

# Do not modify (this code is necessary for MyPyTutor to show output):
savefig("output.png")
