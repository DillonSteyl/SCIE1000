# Loops of Unknown Length

If you've been paying attention for the last few exercises, you may have noticed that you can sometimes work out how many times the loop will repeat just by reading the program. This usually happens when you are counting through a set of values (for example, from 1 to 10). But there are other ways to use while loops.

We can make a while loop that ends when the user asks it to. Observe the program below:


```
from pylab import *

number = 1

while number!=0:
    number = float(input("Give me a number to square, or enter 0 to exit the program: "))
    if number!=0:
        print("The square of", number, "is", number**2)

print("Thanks for playing!")

```

So, while the number is not 0, the program will continue to ask the user for a number and print its square. When the user enters 0, it  exits the loop and says "Thanks for playing!" 

This is pretty useful! The program will keep asking the user for new numbers until the user wants the program to end. There's a lot you can do with this, but for now we will just stick with an easy problem.

**Task:** The user wants to multiply many numbers together. Write a program that will keep asking the user for numbers until they enter 0. When they enter 0, exit the loop (and don't multiply the number by 0!). Finally, print the final large number with the statement `print("The final answer is", number")`.

For example, if the user enters 2, 5, 4, then 0, the answer should be 40. You can calculate this by starting at 1, multiplying that by 2 to get 2. Then multiplying that by 5 to get 10. Then multiplying that by 4 to get 40. 

The input message has been provided for you.


**Hint:** You will need one number to store the user's input, and another number to keep track of your big multiplied number.

```
from pylab import *

number = 1
usersNumber = 1
while usersNumber!=0:
    usersNumber = float(input("Give me a number, or enter 0 to exit the program: ))
    if usersNumber!=0:
        number = number*usersNumber


print("The final answer is", number)


```
