from pylab import *

HELP1000 = float(input("Type 1 if you have taken the course HELP1000, 0 otherwise"))
HELP1500 = float(input("Type 1 if you have taken the course HELP1500, 0 otherwise"))
HELP2001 = float(input("Type 1 if you have taken the course HELP2001, 0 otherwise"))

if HELP1000 == 1 and HELP1500 == 1 and HELP2001 != 1:
    print("You can take this course.")
else:
    print("You cannot take this course, sorry!")
