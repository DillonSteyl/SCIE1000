# The Modulo Operator (3)

Your eccentric friend has been placed in charge of a Time Machine you built together. They have decided that they don't like to count in years, only months. This makes it difficult to pack your clothes - what kind of weather should you expect if you don't know what month it is?

**Task:** Write a function called `travel(current_month, num_months)` that outputs the season that you will arrive in. The `current_month` variable is the month you will travel from (from 0 to 11), and `num_months` is the number of months you will travel back in time. The output of the function should be 0 for autumn, 1 for winter, 2 for spring, and 3 for summer. 

It is important to note that we will start counting the months at 0, so January will be 0 and December will be 11. 

For example, if the starting month is June (5), and you will be going back 18 months, then the output of the function should be 3, because 18 months prior to June (5) is December (11).


**Hint:** Remember that negatives work just fine with mod, no need to worry. For example, (5-6)%12 = 11. 

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
