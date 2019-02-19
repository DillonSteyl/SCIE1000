from pylab import *


# costs to visit each planet (in billions of dollars)
costs = array([18, 13, 5, 25, 20, 17, 8, 7])

planet = int(input("Which planet would you like to visit (0 for Mercury, 1 for Venus, etc): "))

if planet==0:
    print(costs[0], costs[1])
elif planet==7:
    print(costs[6], costs[7])
else:
    print(costs[planet-1], costs[planet], costs[planet+1])

if costs[planet]>=10:
    print("Excellent choice!")
else:
    print("A popular destination!")

costs[planet] = costs[planet] + 2
