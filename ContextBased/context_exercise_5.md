Geologists use a technique called radiometric dating to determine the direct age of fossil material. Organic matter will usually contain Carbon-14, an isotope of the standard Carbon-12 element which has two extra neutrons in its nucleus. This results in the isotope being unstable, and over time, it will decay into Nitrogen-14, a stable element.

Radiometric dating is the process of comparing the ratio of these elements present in organic materials to determine their age. So for example, material that has just been preserved into a fossil will only have Carbon-14 atoms present. These atoms will then decay into Nitrogen-14. It should be noted that the half-life for this decay is 5,730 years. 

This half-life can then be used to determine how long ago the fossil was formed. For example, if the amount of Carbon-14 and Nitrogen-14 is equal, then half of the original Carbon-14 has decayed, so one half-life has past since the fossil was formed. 

Your task is to write a program that will calculate the direct age of a fossil sample. It should include the following features:
1. Prompt the user to input the percentage of isotopes found that are Carbon-14. The user should be asked to try again **and** reprompted if the value they enter is larger than or equal to 100. This will require the use of a while loop menu. Also, percentages below or equal to 10% are not valid for this carbon-dating method, as it limits the validity of the result obtained, so any percentage lower than this should also not be accepted **and** reprompt the user to enter another value. Use 'carbon' as the variable name for this value. 
2. Calculate the number of half-lives that have passed since the fossil was formed and display this on screen. Use 'halflives' as the variable name for this value. 
3. Calculate the number of years that have passed since the fossil was formed and display this on screen. Use 'years' as the variable name for this value. 

The user input prompt should be displayed as follows:

Please enter the percentage of isotopes from the sample found to be Carbon-14:

If the input is larger than 100, or equal to or less than 10, the user should receive the following message:

Please try again as this percentage is not valid. 

Output should be displayed as follows:

The number of half-lives that have passed since the fossil was formed is **ANSWER.**

The number of years that have passed since the fossil was formed is **ANSWER.**

# Solution
```python
from pylab import *

# Write your program below
flag = 1

while flag == 1:
    carbon = float(input("Please enter the percentage of isotopes from the sample found to be Carbon-14: "))
    if carbon < 100 and carbon > 10:
        flag = 0
    else:
        print("Please try again as this percentage is not valid.")

halflives = log(carbon/100)/log(0.5)
years = halflives*5730
print("The number of half-lives that have passed since the fossil was formed is", halflives)
print("The number of years that have passed since the fossil was formed is", years)
```
