# While Loop Menus (1)

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

The things to notice about these two programs is that we have a designated 'exit number', or set of exit numbers. For the second program, we want to exit when the user enters 0. So, we make the while condition `choice!=0`, so that the while loop stops only when choice is equal to 0.

In the first program, we did the reverse. The user enters any number other than 0 to exit the program, so the while loop condition is 'finish == 0'. So when they enter 0, the while loop will finish. 

For both of these programs, we set the variables to a number that would allow the while loop to start. This inital number is meaningless, and doesn't result in anything other than entering the while loop. Imagine for the second program we set choice to 2, or 8, or -135. It would still behave exactly the same way.

Controlling while loops like this gives us a lot of power. We can put large blocks of code in the conditionals, allowing us to have lots of complex behaviour. 

**Task:** For the moment, just write a simple program that has the following menu options:

If the user inputs 1: print the message "Hey, how are you?"

If the user inputs 2: ask the user to input their favourite number, and print this message - ("Wow!", favnumber, "is a great number!")

If the user inputs 0: exit the while loop and print "Thanks!"

**Hint:** You will need a variable to control the flow of the while loop (like choice or finish), much like in the second program.

**IMPORTANT:** You may encounter the error "Code did not finish, possible infinite loop". MyPyTutor gives this error when the program takes too long to run. Sometimes this can mean an infinite loop, other times it means that the code is just still running for other reasons. For these exercises, this will happen when your program asks for more input than needed (as in, your code asks for input three times when we only expected it to ask for input twice). This means you may have an error in your stopping condition. If you cannot figure out the error in your program, try running it in Jupyter. 

To help you with debugging in Jupyter, we are giving you the numbers we use as input in our tests. The input sequences in our tests are as follows:

Test 1: input 0

Test 2: input 1, 0

Test 3: input 2, 5, 0

Test 4: input 2, 5, 1, 0

Test 5: input 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0

Test 6: input 2, 5, 2, 8, 2, -132, 0
