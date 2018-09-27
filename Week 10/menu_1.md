# While Loop Menus

So far in SCIE1000, most while loops you have written have a counter (usually `i`), that starts counting at 0 or 1, and finishes once `i` reaches some number `n`. 

This isn't the only way to use while loops. There are two exercises for while loops in week 4 that use a different structure, titled 'Loops of Unknown Length'. For the following exercises we will be extending that concept.

At the very basic level, we use while loops to control the flow of the program, repeating a block of code for as long as we like. Here is an example program that demonstrates this:

```
from pylab import *

finish = 0

while finish == 0:
    finish = float(input("Type 0 to continue the loop, and any other number to stop it: "))
    
print("Done.")
```

Try running that program in Jupyter if you are unsure of its behaviour. 

We can use this to create a program that presents a menu to the user, and has different behaviour depending on their choice:

```
choice = 1

while choice != 0:
    choice = float(input("Type 1 to know the time, 2 to ask for directions, or 0 to exit the program: "))
    if choice == 1:
        print("It is time to study!")
    elif choice == 2:
        print("You are going in the right direction.")
    
print("Done.")
```

In both of these programs, we have used a variable to control the flow of the while loop (`finish` and `choice`), and have allowed the user to change this variable. 

This gives us a lot of power. We can put large blocks of code in the conditionals, allowing us to have lots of complex behaviour. 

**Task:** For the moment, just write a simple program that has the following menu options:

If the user inputs 1: print the message "Hey, how are you?"

If the user inputs 2: ask the user to input their name, and print this message - ("Hey", username, "! My name is MyPyTutor, nice to meet you.")

If the user inputs anything else: exit the while loop and print "Thanks!"

