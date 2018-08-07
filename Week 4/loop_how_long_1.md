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




**Task:** Due to inflation, a dollar today is not worth the same as it was last year, and will not be worth the same next year either. So how do you compare the cost of things from different years? One way is using purchasing power. Today, $1000 can buy a particular amount of goods and services. In the future, $1000 dollars will buy less goods and services due to inflation. So, its purchasing power has decreased.

The user wants to know the purchasing power of $1000 for particular different years. Ask the user for the year using the message "Enter the year you want to know about, or enter 0 to exit the program: ", and use the following equation to tell them the purchasing power for $1000 for that year with a predicted 3% inflation rate. 

`purchasing power for year vs 2018 = 1000*(1.03)**(2018-year)`

Use the message `"The purchasing power:", 1000*(1.03)**(2018-year), "in year", year`

If the user inputs 0, exit the program and print the message `"Thanks, and have a good day!"`

```
from pylab import *

year = 1

while year!=0:
    year = float(input("Enter the year you want to know about, or enter 0 to exit the program: "))
    if year!=0:
        print("The purchasing power of $1000 dollars in year", year, "is", value, "compared to 2018.")

print("Thanks, and have a good day!")

```


