# Carbon (1)

Geologists use a technique called radiometric dating to determine the direct age of fossil material. Organic matter will usually contain Carbon-14, an isotope of the standard Carbon-12 element which has two extra neutrons in its nucleus. This results in the isotope being unstable, and over time, it will decay into Nitrogen-14, a stable element.

Radiometric dating is the process of comparing the ratio of these elements present in organic materials to determine their age. So for example, material that has just been preserved into a fossil will only have Carbon-14 atoms present. These atoms will then decay into Nitrogen-14. *It should be noted that the half-life for this decay is **5,730** years.*

This half-life can then be used to determine how long ago the fossil was formed. For example, if the amount of Carbon-14 and Nitrogen-14 is equal, then half of the original Carbon-14 has decayed, so one half-life has passed since the fossil was formed. If 75% of the original Carbon-14 has decayed, then two half-lives have passed since the fossil was formed, giving the fossil an age of approximately11460 years.

**Task:** Write a function called `calculate_age(carbon)` that calculates the age of a fossil sample in years, where the input `carbon` is the percentage of Carbon-14 found in the sample. 

**Hint:** It is helpful to first calculate the number of half-lives given the Carbon-14 percentage. The formula for the number of half-lives is log(c)/log(0.5), where c is the percentage of Carbon-14 divided by 100. 


