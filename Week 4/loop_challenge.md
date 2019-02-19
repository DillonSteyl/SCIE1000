# Challenge: Go Team!

You are in charge of a chain of merchandise stalls at sports facilities across Queensland, where Science Ball is played all year round between just two teams. Unfortunately, Science Ball fans are fiercely loyal, and will not buy merchandise from stores that sell goods for the other team that month.

To make the most amount of money, you need to decide when to stock merchandise for Team A and when to stock merchandise for Team B for each of your stalls. Team loyalty is quite volatile for Science Ball fans, but after some research you have figured out how to predict the number of fans for each team using sine waves for any given month. Each sports facility has a different number for the amplitude and vertical shift, but they all follow the same base equation:

```
Number of fans for team A: amplitudeA*sin(2*pi*(i-1)/3)+shiftA
Number of fans for team B: amplitudeB*sin(2*pi*(i+3)/12)+shiftB
```

Where i is the current month, with Janurary being month i=1.


**Task:** Four input statements are written that will prompt the user to enter the amplitudes and vertical shift values for each team, and store them as variables. 

For each month (1 to 12), find which team has the most number of fans using the above equations, and print a message with the format "Team X has the most fans for month i". If both teams have the same number of fans, print a message with the format "Both teams are equally popular for month i".

Meanwhile, keep track of how many months each team has the most number of fans, not counting ties. After printing the 12 messages, print another message with the format "Team X has the most fans for n months." If both teams are equally popular, use the message "Both teams are equally popular."


**Hint 1:** You will need a while loop with if/elif/else statements inside, and you will need some if/elif/else statements for the final message.

**Hint 2:** Just like in Loop Introduction (4), you will need another variable to keep track of how many months team A or team B has the most fans over a year. 
