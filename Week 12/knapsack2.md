# Knapsack Problem 2

For this task, you will need to use your `vpw` function from the previous exercise. Remember to copy paste it into the code - we will be testing for it.

**Task:** Write a function called `best_item(V,W,space)` that takes as input a list of values `V`, a list of weights `W`, and the remaining space in the knapsack `space`. As output, the function should return the index of the item with the highest value per weight, that fits in the remaining space. If there is no item that fits in the remaining space, return -1. If there are multiple items that have the highest value per weight, return the last one of those items in the list.

**Hint:** This might be a bit hard, so if you can't figure it out yourself, we have written some pseudocode for you (pseudocode is like code but written in words). You are welcome to write the function in a different way, so long as it produces the same answers. 
```
Given V, W, and space:
best_index = -1 # this variable will store the index of the item with the best vpw

i = 0 # our counter variable for the while loop
while i is less than the length of V:

    if (the weight of item i is less than or equal to space) \
        AND (the vpw of item i is greater than or equal to the vpw of the item with index best_index):
        
        update best_index to i # we have found a better item
        
    increase i by one
    
return best_index
```

You may have noticed that we ask you to access the item with index 'best_index', which initially is set to -1. With arrays, you are allowed to have negative indices! The element with index -1 is the last element in the array. The reason we are doing this is because we are sneaky - it saves us from having to write more lines of code! Essentially, if there is an item in the list that can fit in the knapsack, best_index will be the index of the best item. If there are no items that can fit in the knapsack, then best_index will be -1, which is what we want to return in that situation! Fun!

