from pylab import *

#These two lines allow h to be random chosen from the range 0 to 114. Do not change these lines. 
import random
h = random.randint(0, 114)

# Write your program below:
a = arange(0,114.1,1)
SS = 3*a**0.5
AW = 0.675*SS

h_SS = 3*h**0.5
h_AW = 3*h**0.5*0.675

SS_vertical_x = array([25, 25])
AW_vertical_x = array([55, 55])
vertical_y = array([0, 35])

plot(a,SS,color='green',label="Spring/Summer")
plot(a,AW,color='orange',label="Autumn/Winter")
plot(SS_vertical_x, vertical_y, 'r', linewidth = 3)
plot(AW_vertical_x, vertical_y, 'r--', linewidth = 3)


if h_SS<15:
    plot(h, h_SS, 'ro', label='Number of Species in S/S')
else:
    plot(h, h_SS, 'ko', label='Number of Species in S/S')
    
if h_AW<15:
    plot(h, h_AW, 'rs', label='Number of Species in A/W')
else:
    plot(h, h_AW, 'ks', label='Number of Species in A/W')




title("Species Area Curve in Different Seasons")
xlabel("Area (hectares)")
ylabel("Number of Species")
grid(True)
legend()
show()

# Do Not Modify Below This Line
savefig("output.png")
