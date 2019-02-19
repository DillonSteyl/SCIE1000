# While Loop Menus (4) - Buried Treasure!

For this exercise you will make a buried treasure game. Here is the premise:

You are on an island to find buried treasure. The only problem is that your treasure detector is broken. Your treasure detector is supposed to tell you how many moves you are away from the treasure. However, sometimes it gets it wrong by slightly underestimating or overestimating the distance.

For each turn of the game you have 6 moves: left, up, right, down, dig, and stay. The island is 10 meters by 10 meters, and each movement will move you by 1 meter. If you are on the edge of the island and choose to move into the ocean, you will swim around to the opposite side of the island. If you dig, you will find the buried treasure if it is there, otherwise you will lose a life. You have three chances to find the buried treasure before you will be too tired to dig anymore, and must go home. If you choose to stay put, nothing will happen and your treasure detector will have another go at finding the distance.


**Task:** You must complete the code so that the program behaves properly. Most of it has been written for you. There are three functions in this program, and you are not expected to understand how they work - but you are welcome to try!

For each turn of the game, a set of messages is printed and the user is asked for input. You do not need to change any of these messages.

If the player decides to move, you must calculate their new position with the help of the `newPosition` function. You do not need to print anything. For example, moving left means their y coordinate stays the same, and their x coordinate is one less, so x-1. 

If the player decides to dig, you must first check if the buried treasure is at their location (has the same x and y values). If so, print the message ("You found the treasure!") and make sure the while loop finishes. If the buried treasure is not there, the player must lose a life and the program should print the messages ("Sorry, there is no treasure here.") and ("You have", lives,"of your lives remaining.").

If the player enters any other number, do nothing and let the program loop back to the start of the while loop again. 

Once the while loop ends, print the message ("You are out of lives, better luck next time!") if they have no lives left. Otherwise, print nothing.

**Important:** This program uses a random number generator. To ensure that the output is the same as ours, include the line `random.seed(n)` below the `import random` line in your program **only** if you run it in Jupyter. Input sequences and `n` values are as follows:

Test 1: input 5, 5, 5. The player loses. `n = 1`

Test 2: input 4, 3, 3, 5. The player wins. `n = 1`

Test 3: input 8, 8, 8, 2, 8, 8, 8, 5. The player wins. `n = 2`
