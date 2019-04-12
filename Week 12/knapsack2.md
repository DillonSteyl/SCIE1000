# Knapsack Problem (2)

**Note:** For this task, you will need to use your `vpw` function from the previous exercise. Remember to copy paste it into the code - we will be testing for it.

For this exercise you will write a function that finds the best item in the list of items, based on each item's value per weight. We want the function to return the index of the best item, or -1 if no more items can fit in the knapsack. If multiple items have the best value per weight, the index of the last one in the list should be returned. Below is the pseudocode for this algorithm.

```
Given V (list of values), W (list of weights), and space (remaining space in knapsack):

best_index = -1  

for the index of each item in the knapsack:
    if the current item can fit in the remaining space:   
        if (best_index is equal to -1) or (vpw of the current item >= vpw of item with index best_index):
               update best_index to current index
    
return best_index
```

The pseudocode says to cycle through the index of each item in the knapsack, but doesn't explicitly tell you how to do it! A while loop would work well there, with a variable keeping track of the index of the current item (from 0 to just less than the length of V or W).

**Task:** Write a function called `best_item(V,W,space)` that takes as input a list of values `V`, a list of weights `W`, and the remaining space in the knapsack `space`. As output, the function should return the index of the item with the highest value per weight, that fits in the remaining space. If there is no item that fits in the remaining space, return -1. If there are multiple items that have the highest value per weight, return the last one of those items in the list. If the lists are empty, return -1. 


