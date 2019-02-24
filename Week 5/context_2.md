## Challenge: Party Time!

Two of your friends (who dislike each other) are throwing a party on the same day, on the same street. You've been to many of their parties, and you think you can model the number of guests in each party. The equations are as follows:

```
A[i] = A[i-1]*0.6 + 18 + B[i-1]*(0.2), rounded to 0 decimal places
B[i] = B[i-1]*0.4 + 25 + A[i-1]*(0.25), rounded to 0 decimal places
```

The number of guests for Friend A at hour `i` is `A[i]`. The number of guests for Friend B at hour `i` is `B[i]`. The equations look a bit complex, but you will learn how to write them towards the end of the course. You don't need to understand them to complete this exercise, but we will explain them in case you are interested. These equations were made by making the prediction that 60% of Friend A's guests will stay at that party (`A[i-1]*0.6`), 18 new guests would join (`18`), and 20% of the guests at Friend B's party will switch to Friend A's party (`B[i-1]*(0.2)`). The same is said for Friend B, except with different values. 

You want to analyse these two equations, finding the average, maximum, and total number of guests for both models. You also want to find the largest difference. 

**Task:**

Given that the parties will last 8 hours and there are initially 10 guests at each party in the first hour:

1. Calculate the number of guests for Friend A and B, and store them in the arrays friendA and friendB, respectively. Do not forget to round each value to zero decimal places as they are calculated.

2. Calculate the average, max, and sum for each model. Store them using the following variable names: avgA, maxA, sumA, and avgB, maxB, sumB. Print them using the message provided.

3. Calculate the difference between the number of people at each party for each hour. Store this in the array diff. Each value should be positive. See the hint if you need help with this.

4. Print the maximum value in the diff array, using the message provided. Also store it in the variable maxDiff.

5. Print the message "Friend X will have the most popular party.", where X is the friend with the highest average number of guests per hour. If they are equal, print the message "The parties will be equally popular."


**Hint:** Depending on how you implement this, you may want to use the absolute function on an array. The absolute function makes all values positive, and will work on both numbers and arrays. Given an array A, the absolute function is `abs(A)`. It will also work for expressions, so the absolute value of two arrays X and Y added together is `abs(X+Y)`.
