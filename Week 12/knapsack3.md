# Knapsack Problem (3)

With the functions you have written so far, you are able to identify the item that needs to be placed in the knapsack next. For the rest of the algorithm, you need some functions that will help you add the item to the knapsack, and remove it from the list. We have written these for you! There are easier ways to write these functions, but they require programming concepts that are beyond the scope of this course. This way, you are welcome to read these functions and see how we've done it. 

You are now ready to write the final function. Here is the full algorithm in words:
```
Given V (list of values), W (list of weights), m (maximum weight of knapsack):

space = m # variable for keeping track of the space left in the knapsack
knapsack_value = 0 # variable for keeping track of the value of the knapsack
KV = empty array (length 0) # array for keeping track of the value of items added to the knapsack
KW = empty array (length 0) # array for keeping track of the weight of items added to the knapsack

# variable for storing the index of the item to be added to the knapsack
# when it is later set to -1, it means no more items can be added to the knapsack
best_index = 0

# keep adding items until we can't anymore. 
repeat while best_index is not equal to -1:
    # get the index of the next item to add to the knapsack
    best_index is updated to the output of best_item(V,W,space)
    
    # if there is an item that can be added to the knapsack
    if best_index is not equal to -1:
        # add the item to the knapsack
        KV, KW updated to the output of add_item(KV, KW, V[best_index], W[best_index])
        
        # update the knapsack values
        space is updated to space minus the weight of the item
        knapsack_value is updated to knapsack_value plus the value of the item
        
        # remove the item from the list
        V, W updated to the output of remove_item(V, W, best_index)
        
return KV, KW, and knapsack_value
```

**Task:** Write a function called `knapsack(V,W,m)` that takes as input a list of values `V`, a list of weights `W`, and the maximum weight of the knapsack `m`. As output, return the list of values of items put into the knapsack `KV`, the list of weights of those items `KW`, and the total value of the knapsack `knapsack_value`.

**Hint:** To create an empty array, simply use the array function but without any elements. For example, `A = array([])` will create an array of length 0. 

Some input-output examples:

1. Input: `V = [5, 11, 7]`, `W = [2, 4, 3]`, m = 5
Output: `KV = [11]`, `KW = [4]`, knapsack_value = 11 (notice that this isn't the best answer, but it is the one your algorithm will produce)

2. Input: `V = [1, 3, 4, 5, 6, 7]`, `W = [20, 1, 2, 1, 2, 3]`, m = 6
Output: `KV = [5, 6, 3, 4]`, `KW = [1, 2, 1, 2]`, knapsack_value = 18

3. Input: `V = [25, 64, 16, 4]`, `W = [4, 8, 3.5, 1]`, m = 16.5
Output: `KV = [64, 25, 16, 4]`, `KW = [8, 4, 3.5, 1]`, knapsack_value = 109

4. Input: `V = [15, 13, 13, 12, 11, 9, 9, 9, 4, 3, 2]`, `W = [5, 2, 7, 3, 5, 2, 4, 6, 1, 1, 1]`, m = 10
Output: `KV = [13, 9, 4, 12, 3, 2]`, `KW = [2, 2, 1, 3, 1, 1]`, knapsack_value = 43
