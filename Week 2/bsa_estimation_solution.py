from pylab import *

# Input mass:
mass = float(input("Enter mass: "))
# Input height:
height = float(input("Enter height: "))

# Calculate BSA Estimates
mostellar_bsa = 0.0167*sqrt(mass*height)
dubois_bsa = 0.007184 * mass**0.425 * height**0.725
haycock_bsa = 0.024265 * height**0.3964 * mass**0.5378

# Print BSA Estimates
print("Mostellar BSA Estimate:", mostellar_bsa)
print("Dubois BSA Estimate:", dubois_bsa)
print("Haycock BSA Estimate:", haycock_bsa)
