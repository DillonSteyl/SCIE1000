from pylab import *

def calculate_age(carbon):
    halflives = log(carbon/100)/log(0.5)
    years = halflives*5730
    return(years)

flag = 1

while flag == 1:
    carbon = float(input("Please enter the percentage of isotopes from the sample found to be Carbon-14: "))
    if carbon < 100 and carbon > 10:
        flag = 0
    else:
        print("Please try again as this percentage is not valid.")

years = calculate_age(carbon)
print("The number of years that have passed since the fossil was formed is approximately", round(years))
