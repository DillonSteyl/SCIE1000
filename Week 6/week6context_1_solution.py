from pylab import *

def ratio(tumoursize, weight):
    thickness = weight/20
    ratio = tumoursize/thickness
    return(ratio)

tumoursize = float(input("Enter the tumour size (mm): "))
weight = float(input("Enter the patient weight (kg): "))
result = ratio(tumoursize, weight)

if result < 0.5:
    print("The chance of receiving a true positive and negative result from the FOBT screen are 50% and 95% respectively.")
elif result <= 1.5:
    print("The chance of receiving a true positive and negative result from the FOBT screen are 75% and 95% respectively.")
else:
    print("The tumour is now in stage III or IV.")
