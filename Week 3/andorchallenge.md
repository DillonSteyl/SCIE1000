# Challenge: Roller coaster!

**Task:** You are in charge of writing code for a theme park. On one of the roller coasters, all riders must be greater than or equal to 130cm tall, and less than or equal to 200cm tall. However, riders who are between 100cm and 130cm tall are allowed on the ride if they are accompanied by an adult. The theme park wants to automate the process of checking that someone is allowed to ride.

Your job is to write some code that asks for the rider's height and whether they are accompanied by an adult. The height will be in cm, and then you will be given the number '1' if the rider is accompanied by an adult, and '0' otherwise. Then, you will print "Enjoy your ride!" if the person is allowed to ride, and "Sorry, you cannot ride this rollercoaster." otherwise. 

Challenge yourself and write the program using only one if statement and an else statement, with the help of `and` and `or`. 

## Solution

```python
from pylab import *

height = float(input("Enter your height: "))
adult = float(input("Enter 1 if you are accompanied by an adult, and 0 otherwise"))

if height=<200 and (height>=130 or (height>100 and adult==1)):
    print("Enjoy your ride!")
else:
    print("Sorry, you cannot ride this rollercoaster.")



```


