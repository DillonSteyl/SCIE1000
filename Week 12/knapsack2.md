# Knapsack Problem (2)

For this task, you will need to use your `vpw` function from the previous exercise. Remember to copy paste it into the code - we will be testing for it.

**Task:** Write a function called `best_item(V,W,space)` that takes as input a list of values `V`, a list of weights `W`, and the remaining space in the knapsack `space`. As output, the function should return the index of the item with the highest value per weight, that fits in the remaining space. If there is no item that fits in the remaining space, return -1. If there are multiple items that have the highest value per weight, return the last one of those items in the list. If the lists are empty, return -1. 

**Hint:** This might be a bit hard, so if you can't figure it out yourself, we have written some pseudocode for you (pseudocode is like code but written in words). You are welcome to write the function in a different way, so long as it produces the same answers. 
```
Given V, W, and space:

# this variable will store the index of the item with the best vpw
# but will stay as -1 if we don't find any items that fit
best_index = -1  

i = 0 # our counter variable for the while loop
while i is less than the length of V:
    # we only want to consider items than can fit in the knapsack
    if the weight of item i is less than or equal to space:
    
        # we update best_index if this is the first item we've found that fits, or we have found a better item
        if (best_index is equal to -1) or (the vpw of item i is greater than or equal to the vpw of item best_index):
               update best_index to i 
        
    increase i by one
    
return best_index
```

