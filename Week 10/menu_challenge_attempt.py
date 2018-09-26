
from pylab import *

# We need to use the random library to randomly choose a treasure position, and get the detector reading
import random

# this function returns a randomly chosen position for the buried treasure
def makeTreasureCoords():
    return(random.randrange(9),random.randrange(9))

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
    
    # moves the player left
    if move==1:
        position_x, position_y = newPosition(position_x-1, position_y)
    ### ----------- This is where you should write your code ------------
    
    
# if the player has no lives left, let them know they lost
if lives==0:
    print("You are out of lives, better luck next time!")
