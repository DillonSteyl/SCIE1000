# The Modulo Operator (3)

Your eccentric friend has been placed in charge of a Time Machine you built together. They have decided that they don't like to count in years, only months. This makes it difficult to pack your clothes - what kind of weather should you expect if you don't know what month it is?

**Task:** Write a function called `travel(current_month, num_months)` that outputs the season that you will arrive in. The `current_month` variable is the month you will travel from (from 0 to 11), and `num_months` is the number of months you will travel backwards or forwards in time. The output of the function should be 0 for autumn (months 2 to 4), 1 for winter (months 5 to 7), 2 for spring (months 8 to 10), and 3 for summer (months 11, 0, and 1). 

It is important to note that we will start counting the months at 0, so January will be 0 and December will be 11. 

For example, if the starting month is January (0), and you will be going forward 50 months, then the month will be March (2), because 50 months is 4 years + 2 months in the future. This would correspond with the operation `(0+50)%12`, which is equal to 2. March is in Autumn, so `travel(0, 50) = 1`. 

For an example going back in time, if the starting month is June (5), and you will be going back 6 months, then the output of the function should be 3, because 6 months prior to June (5) is December (11). This would correspond with the operation `(5-6)%12`, which is equal to 11. So `travel(5, -6) = 3`.

Unless you are very crafty, you will need conditionals in this function to handle converting from the month to the season. 

**Hint:** There is no need to write different code for going back in time vs going forward in time. Notice how in the examples the same formula is used either way. The modulo operator will work exactly how we want it to in either case. 

```
def travel(current_month, num_months):
    month = (current_month - num_months)%12
    if 2<=month<5:
        return(1)
    elif 5<=month<8:
        return(2)
    elif 8<=month<11:
        return(3)
    else:
        return(0)

```
