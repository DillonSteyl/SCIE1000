# Knapsack Problem (3)

Recall, the greedy algorithm is as follows:

**The Greedy Algorithm:**
You are given a knapsack with a maximum weight, a list of items with their corresponding values and weights.

Repeat until you can't fit anything else into the knapsack:
- Find the item on the list with the highest value per weight, that can fit in the remaining space in the knapsack.
- Put it in the knapsack
- Remove it from the list

With the functions you have written so far, you are able to identify the item that needs to be placed in the knapsack next. For the rest of the algorithm, you need some functions that will help you add the item to the knapsack, and remove it from the list. 

**Task:** Write two functions `remove_item(V,W,i)` and `add_item(KV, KW, iV, iW)`, described below:

`remove_item(V,W,i)` takes as input the list of values V, the list of weights W, and the index for the item to remove i. It returns two lists, newV and newW, that 
