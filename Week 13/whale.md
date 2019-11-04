# Whales vs Zooplankton

The bow-head whale feeds primarily on zooplankton by swimming forward with its mouth open and capturing the small organisms in the water. The whale and zooplankton populations are closely related, as changes in one results in changes in the other. In fact, the whales and the zooplankton form a predator prey relationship, and the change in their populations for a specific area can be modelled using the following equations:

`W' = -W + 0.03*Z*W`
`Z' = 0.4*Z - 0.025*Z*W`

Where W is the number of whales in the area and Z is the weight of the zooplankton population in the area in thousands of metric tonnes. With a step size of s, this means that the populations each year can be modelled using the following equations:

`next W = current W + s*W'`
`next Z = current Z + s*Z'`

**Task:** Model the population of whales and zooplankton over 20 years, with a step size of 0.1 years. The starting values for the whales is 12, and the starting value for the zooplankton is 40. Store the populations in arrays named `W` for the whales and `Z` for the zooplankton. There should be 201 steps, including the initial step (step 0). 

Find the step number for when the number of whales reaches is highest value, and store it in the variable provided. Repeat for the zooplankton. 

Print the highest number of whales and zooplankton using the print statements provided.

Print the number of steps between the highest number of whales and the highest number of zooplankton using the print statements provided. The number of steps between the peaks should be positive.

**Hint 1:** You may find it helpful to use the highest(A) function you wrote earlier.  

**Hint 2:** The abs(x) function can be used to make a number positive.
