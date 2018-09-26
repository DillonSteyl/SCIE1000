# Challenge - Buried Treasure

For this exercise you will make a buried treasure game. Here is the premise:

You are on an island to find buried treasure. The only problem is that your treasure detector is broken. Your metal detector is supposed to tell you how many moves away you are from the treasure. However, sometimes it gets it wrong by slightly underestimating or overestimating the distance.

For each turn of the game you have 6 moves: left, up, right, down, dig, and stay. The island is 10 meters by 10 meters, and each movement will move you by 1 meter. If you are on the edge of the island and choose to move into the ocean, you will swim around to the other side of the island. If you dig, you will find the buried treasure if it is there, otherwise you will lose a life. You have three chances to find the buried treasure before you will be too tired to dig anymore, and must go home. If you chose to stay put, nothing will happen and your treasure detector will have another go at finding the distance.


**Task:** You must complete the code so that the program behaves properly. Most of it has been written for you. There are three functions in this program, and you are not expected to understand how they work - but you are welcome to try!

For each turn of the game, a set of messages are printed and the user is asked for input. You do not need to change any of these messages.

If the player decides to move, you must calculate their new position with the help of the `newPosition` function. You do not need to print anything.

If the player decides to dig, you must first check if the buried treasure is at their location (has the same x and y values). If so, print the message "you found the treasure." and make sure the while loop finishes. If the buried treasure is not there, the player must lose a life and the program should print the messages ("Sorry, there is no treasure here.") and ("You have", lives,"remaining.").

If the player enters any other number, do nothing and let the program loop back to the start of the while loop again. 

Once the while loop ends, print the message ("You are out of lives, better luck next time!") if they have no lives left. Otherwise, print nothing.



```

from pylab import *

# We need to use the random library to randomly choose a treasure position, and get the detector reading
import random

# this function returns a randomly chosen position for the buried treasure
def makeTreasureCoords():
    return(random.randrange(10),random.randrange(10))

# this function returns the reading from the broken treasure detector
def detect(position_x, position_y, treasure_x, treasure_y):
    return(max(abs(position_x - treasure_x)+abs(position_y - treasure_y)+random.randrange(-1,2),0))

# this function moves the player to the other side of the island, when necessary
def newPosition(x, y):
    return(x%9, y%9)

# the treasure coordinates are randomly generated
treasure_x, treasure_y = makeTreasureCoords()

# the player starts at this position
position_x = 0
position_y = 0

# found is set to 1 if the player has found the treasure, 0 otherwise
found = 0
# the player starts with 3 lives
lives = 3

# this while loop runs so long as the treasure has not been found, and the player is not out of lives
while found==0 and lives>0:
    
    # prints the position and detector reading for the player (Adding 1 so it goes from 1 to 10, instead of 0 to 9)
    print("Your position is", position_x+1, position_y+1)
    print("Your detector says the treasure is", detect(position_x, position_y, treasure_x, treasure_y), "moves away.")
    
    # prints the options and asks for input
    print("Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.")
    move = float(input("Enter your choice: "))
    
    # the player digs for treasure
    if move==5:
    # checks if they found the treasure
        if position_y==treasure_y and position_x==treasure_x:
            found = 1
            print("You found the treasure!")
        else:
            # take a life because there is no treasure here
            print("Sorry, there is no treasure here.")
            lives = lives - 1
            print("You have", lives,"remaining.")
    # moves the player
    elif move==1:
        position_x, position_y = newPosition(position_x-1, position_y)
    elif move==2:
        position_x, position_y = newPosition(position_x, position_y+1)
    elif move==3:
        position_x, position_y = newPosition(position_x+1, position_y)
    elif move==4:
        position_x, position_y = newPosition(position_x, position_y-1)
    
    
# if the player has no lives left, let them know they lost
if lives==0:
    print("You are out of lives, better luck next time!")
    
```

NOTE FOR TESTING: SET THE RANDOM SEED BEFORE IMPORTING THE ATTEMPT FILE TO ENSURE THE CORRECT BEHAVIOUR FOR EACH TEST. IS THIS EVEN POSSIBLE?
