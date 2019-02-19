from pylab import *

HELP2000 = float(input("Type 1 if you have taken HELP2000, and 0 otherwise: "))
HELP2001 = float(input("Type 1 if you have taken HELP2001, and 0 otherwise: "))
HELP2500 = float(input("Type 1 if you have taken HELP2500, and 0 otherwise: "))
HELP3001 = float(input("Type 1 if you have taken HELP3001, and 0 otherwise: "))

if (HELP2000 == 1 or HELP2001 == 1) and HELP2500 == 1 and HELP3001==0:
    print("You can take this course.")
else:
    print("You cannot take this course, sorry!")
