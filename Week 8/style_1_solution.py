from pylab import *

# Data to use for plotting. A is line 1, B is line 2, etc.
X = arange(-3, 3.1, 0.1)
A = X
B = X**2
C = X**3
D = -7*X
E = 5*X

# Write your program below:
plot(X,A,'g--')
plot(X,B,color='purple', marker='s', linewidth=0.5)
plot(X,C,marker='8', color='k', linestyle='None')
plot(X,D,linewidth=5)
plot(X,E,color='xkcd:blood orange', linestyle='-.', marker='.', linewidth=2)
show()
# Do not modify below this line
savefig("output.png")
