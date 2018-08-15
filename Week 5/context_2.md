## Challenge: Party Time!


Two of your friends (who dislike each other) are throwing a party on the same day, on the same street. You've been to many of their parties, and you think you can model the number of guests in each party. The equations are as follows:

```
A[i] = A[i-1]*0.5+15+B[i-1]*(0.2+i*0.02), rounded to 0 decimal places
B[i] = B[i-1]*0.4+20+A[i-1]*(0.2+i*0.02), rounded to 0 decimal places
```

The number of guests for Friend A at hour `i` is `A[i]`. The number of guests for Friend B at hour 'i' is `B[i]`.
