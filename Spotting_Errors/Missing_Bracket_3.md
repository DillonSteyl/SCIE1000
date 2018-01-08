# Spot the Error

**Task:** Find an fix the error in the following code

**Hint:** Take a closer look at the while loop contents

## Program
```python

print("this is a program to model the fish population over time")

#growth value
r = 1.35

#initial number of fish
init = eval(input("Input the initial number of fish: "))

#carrying capacity
k = eval(input("Input the carrying capacity of the fish population"))

#number of years to project for
years = eval(input("Input the number of years to be modelled"))

print("Year \t Number of Fish")

i=0
while i < years:
    if i==0:
        fish = init
    else:
         fish = (r*fish*(1-(fish/k))
    print(i, "\t", round(fish))
    i = i + 1

```

## Solution
```python

print("this is a program to model the fish population over time")

#growth value
r = 1.35

#initial number of fish
init = eval(input("Input the initial number of fish: "))

#carrying capacity
k = eval(input("Input the carrying capacity of the fish population"))

#number of years to project for
years = eval(input("Input the number of years to be modelled"))

print("Year \t Number of Fish")

i=0
while i < years:
    if i==0:
        fish = init
    else:
         #missing bracket in fish population calculation
         fish = (r*fish*(1-(fish/k)))
    print(i, "\t", round(fish))
    i = i + 1

```
