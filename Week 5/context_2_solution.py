from pylab import *

friendA = zeros(int(8))
friendB = zeros(int(8))

friendA[0] = 10
friendB[0] = 10

i = 1
while i<8:
    friendA[i] = round(friendA[i-1]*0.6+18+friendB[i-1]*(0.2))
    friendB[i] = round(friendB[i-1]*0.4+25+friendA[i-1]*(0.25))
    i = i + 1

avgA = mean(friendA)
maxA = max(friendA)
sumA = sum(friendA)
avgB = mean(friendB)
maxB = max(friendB)
sumB = sum(friendB)

print("Friend A -- Avg:", avgA, "Max:", maxA, "Sum:", sumA)
print("Friend B -- Avg:", avgB, "Max:", maxB, "Sum:", sumB)

diff = abs(friendA-friendB)
maxDiff = max(diff)

print("The maximum difference is", maxDiff)

if avgA>avgB:
    print("Friend A will have the most popular party.")
elif avgB>avgA:
    print("Friend B will have the most popular party.")
else:
    print("The parties will be equally popular.")
