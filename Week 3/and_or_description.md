This is still under construction. Likely to be in an extras section and split up into multiple exercised. 


### The 'and' operator

Being able to check conditions in sequence is useful, but there are some situations where it just isn't efficient. Consider a situation where you are in charge of writing code for a theme park. On the roller coasters, all riders must be above 130cm tall, and below 200cm. However, riders who are between 110cm and 130cm are allowed on the ride if they are accompanied by an adult.

This is a situation where multiple conditions need to be true at the same time. For this, we can use the 'and' operator. Here is the usual structure of an if statement that includes the 'and' operator:

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

This is good, but we can do better. Another operator can help.

### The 'or' operator

Much like the 'and' operator, the 'or' operator joins two conditions to be evaluated as true or false together. The 'and' operator only runs the code if BOTH conditions are true. The 'or' operator runs the code if EITHER or BOTH conditions are true. Here is how it works:

```
if condition1 or condition2:
    #do a thing if EITHER condition is true
```

Just like 'and' operators, you can have many 'or' operators, like this:

```
if condition1 or condition2 or condition3:
    #do a thing if ANY of the conditions are true.
```
 
We can have even more fun with this. You can make if statements using 'and' and 'or', with the help of brackets to make order clear.   Here is an example:

```
if condition1 or (condition2 and condition3):
    #do a thing if condition1 is true, OR if BOTH condition2 and condition3 are true
```    
These can be very helpful! See how this makes the rollercoaster problem even easier:
 
```
height = eval(input("What is the height (cm) of the rider: "))
adult = eval(input("Type 1 if accompanied by an adult, 0 otherwise: "))

if height<=200 and (height>=130 or (height>=110 and adult==1)):
    print("You may ride. Have fun!")
else:
    print("Sorry, you cannot ride.")

 

