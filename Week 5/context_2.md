## Challenge: Party Time!


Two of your friends (who dislike each other) are throwing a party on the same day, on the same street. You've been to many of their parties, and you think you can model the number of guests in each party. The equations are as follows:

```
A[i] = A[i-1]*0.6 + 18 + B[i-1]*(0.2), rounded to 0 decimal places
B[i] = B[i-1]*0.4 + 25 + A[i-1]*(0.25), rounded to 0 decimal places
```

The number of guests for Friend A at hour `i` is `A[i]`. The number of guests for Friend B at hour 'i' is `B[i]`. These equations were made by making the prediction that 60% of Friend A's guests will stay at that party, 18 new guests would join, and 25% of the guests will switch to Friend B's party (the other 15% will go home). The same is said for Friend B, except with different values. 

You want to analyse these two equations, finding the average, maximum, and total number of guests for both models. You also want to find the largest difference. 

These equations are a bit complex, so you also want to simplify them. You decide that the best way is to model them with a linear equation. So you want your program to print the slope for each equation, based on the first and last values.

**Task:**

Given that the parties will last 8 hours:
1. Calculate the number of guests for Friend A and B, and store them in the arrays friendA and friendB, respectively.
2. Calculate the average, max, and sum for each model. Print them using the message provided. Store them in the variables provided. 
3. Calculate the difference between the number of people at each party for each hour. Store this in the array diff. Each value should be positive. 
4. Print the maximum value in the diff array, using the message provided. Also store it in the variable maxDiff.
5. Calculate the slopes for both models using the formula: `m = (ylast - yfirst)/(xlast - xfirst)`. In this scenario, y is the number of people, x is the hour. The hours start at 0 and end at 7. Store the slopes in the variables slopeA and slopeB
6. Print the message "Friend X will have the most popular party.", where X is the friend with the heighest slope value. If they are equal, print the message "The parties will be equally popular."


**Hint:** Depending on how you implement this, you may use the absolute function on arrays. The absolute function makes all values positive. This function will work on both numbers and arrays. Given an array A, the absolute function is `abs(A)`.
