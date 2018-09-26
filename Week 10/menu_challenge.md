# Challenge - Buried Treasure

For this exercise you will make a buried treasure game. Here is the premise:

You are on an island to find buried treasure. The only problem is that your treasure detector is broken. Your metal detector is supposed to tell you how many moves away you are from the treasure, however sometimes it gets it wrong by slightly underestimating or overestimating the distance.

For each turn of the game you have 6 moves: left, up, right, down, dig, and stay. The island 10 meters by 10 meters, and each movement will move you by 1 meter. If you are on the edge of the island and choose to move into the ocean, you will swim around to the other side of the island. If you dig, you will find the buried treasure if it is there, otherwise you will lose a life. You have three chances to find the buried treasure before you will be too tired to dig anymore, and must go home. If you chose to stay put, nothing will happen and your treasure detector will have another go and finding the distance.


**Task:** You must complete the code so that the program behaves properly. 



```
from pylab import *
import random

def makeTreasureCoords():
    return(random.randrange(9),random.randrange(9))

def detect(position_x, position_y, treasure_x, treasure_y):
    return(max(abs(position_x - treasure_x)+abs(position_y - treasure_y)+random.randrange(-1,1),0))

def newPosition(x, y):
    return(x%9, y%9)

treasure_x, treasure_y = makeTreasureCoords()

position_x = 0
position_y = 0

found = 0
lives = 3

while found==0 and lives>0:
    print("Your position is", position_x+1, position_y+1)
    print("Your detector says the treasure is", detect(position_x, position_y, treasure_x, treasure_y), "moves away.")
    move = float(input("Type 1 to move left, 2 to move up, 3 to move right, 4 to move down, 5 to dig, and anything else to stay put: "))
    if move==5:
        if position_y==treasure_y and position_x==treasure_x:
            found = 1
            print("You found the treasure!")
        else:
            print("Sorry, there is no treasure here.")
            lives = lives - 1
            print("You have", lives,"remaining.")
    elif move==1:
        position_x, position_y = newPosition(position_x-1, position_y)
    elif move==2:
        position_x, position_y = newPosition(position_x, position_y+1)
    elif move==3:
        position_x, position_y = newPosition(position_x+1, position_y)
    elif move==4:
        position_x, position_y = newPosition(position_x, position_y-1)
```
