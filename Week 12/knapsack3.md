# Knapsack Problem (3)

Recall, the greedy algorithm is as follows:

**The Greedy Algorithm:**
You are given a knapsack with a maximum weight, a list of items with their corresponding values and weights.

Repeat until you can't fit anything else into the knapsack:
- Find the item on the list with the highest value per weight, that can fit in the remaining space in the knapsack.
- Put it in the knapsack
- Remove it from the list

With the functions you have written so far, you are able to identify the item that needs to be placed in the knapsack next. For the rest of the algorithm, you need some functions that will help you add the item to the knapsack, and remove it from the list. We have written these for you! There are easier ways to write these functions, but they require programming concepts that are beyond the scope of this course. This way, you are welcome to read this functions and see how we've done it. 
