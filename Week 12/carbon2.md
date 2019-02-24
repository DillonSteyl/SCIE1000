# Carbon 2

For this particular Carbon dating method, percentages below or equal to 10% can produce inaccurate results. Additionally, percentages about 100% don't make much sense. 

So, you must write a program that makes sure the user inputs a valid percentage of Carbon-14.


**Task:** Write a program that prompts the user to input the percentage of isotpes found that are Carbon-14, and keep prompting them until they enter a value that is higher than 10% and less than 100%. We will provide the input message for you. If they enter an invalid percentage, use the print statement provided to inform them of their error. 

When they have finally entered a valid percentage, use your function from the previous exercise to tell the user how old their fossil is, using the print statement provided. Make sure the number of years is rounded to 0 decimal places.

Here is an example of the program being used with input 9, 118, 50 from the user:

```
Please enter the percentage of isotopes from the sample found to be Carbon-14: 9
Please try again as this percentage is not valid.
Please enter the percentage of isotopes from the sample found to be Carbon-14: 118
Please try again as this percentage is not valid.
Please enter the percentage of isotopes from the sample found to be Carbon-14: 50
The number of years that have passed since the fossil was formed is approximately 5730.0
```

**Hint:** You will need to use a while loop to repeatedly ask the user for input until it is correct. See week 4 for 'loops of unknown length' or week 10 for 'while loop menus' if you are unsure how to do this.

