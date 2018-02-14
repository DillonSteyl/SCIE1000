## The 'and' operator

Being able to check conditions in sequence is useful, but there are some situations where it just isn't efficient. Consider a situation where you are in charge of writing code for a theme park. On the roller coasters, all riders must be above 130cm tall, and below 200cm tall. However, riders who are between 110cm and 130cm are allowed on the ride if they are accompanied by an adult.

This is a situation where multiple conditions need to be true at the same time (they are above 110cm AND they need an adult). We could try putting multiple if/else statements in sequence, or we can use the 'and' operator and make our if statements feel more natural. Here is the usual structure of an if statement that includes the 'and' operator:

```
if condition1 and condition2:
    #do a thing if BOTH conditions are true.
    
```

Note that you aren't limited to just two conditions, you can have many conditions separated by 'and'. You can keep adding conditions for as long as you like. Here is an example with three conditions:

```
if condition1 and condition2 and condition3:
    #do a thing if ALL conditions are true.
```

We can use this for our rollercoaster problem:

```
height = eval(input("What is the height (cm) of the rider: "))
adult = eval(input("Type 1 if accompanied by an adult, 0 otherwise: "))

if height>200:
    print("Sorry, you cannot ride.")
elif height>=130:
    print("You may ride. Have fun!")
elif height>=110 and adult==1:
    print("You may ride. Have fun!")
else:
    print("Sorry, you cannot ride.")
```

**Task:** Write a program to determine if a student is allowed to take the imaginary course HELP2000. A student may only take HELP2000 if they have completed HELP1000 and HELP1500 but haven't completed HELP2001. 

Ask the student which courses of the three they have taken, and store their response in the variables HELP1000, HELP1500, and HELP2001. The student will say '1' if they have taken the course, and '0' if they haven't (like the adult variable in the rollercoaster problem).

Print the message "You can take this course." if they are allowed to take the course, and "You cannot take this course, sorry!" otherwise. 

You should be able to do this with just one if statement (and an else statement), using 'and' operators.

##Solution

````
HELP1000 = eval(input("Type 1 if you have taken the course HELP1000, 0 otherwise"))
HELP1500 = eval(input("Type 1 if you have taken the course HELP1500, 0 otherwise"))
HELP2001 = eval(input("Type 1 if you have taken the course HELP2001, 0 otherwise"))

if HELP1000 == 1 and HELP1500 == 1 and HELP2001!=1:
    print("You can take this course.")
else:
    print("You cannot take this course, sorry!")
````
