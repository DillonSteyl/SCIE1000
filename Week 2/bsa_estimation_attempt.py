from pylab import *

# Input mass:

# Input height:


# Calculate BSA Estimates
mostellar_bsa = 0.0167 * sqrt(mass*height)
dubois_bsa = 0.007184 * mass**0.425 * height**0.725

# Print BSA Estimates
print("Mostellar BSA Estimate:", mostellar_bsa)
print("Dubois BSA Estimate:", dubois_bsa)