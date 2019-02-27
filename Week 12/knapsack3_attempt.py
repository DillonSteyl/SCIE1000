from pylab import *

# your vpw function here

#your best_item function here

# removes the item at index i from arrays V and W
def remove_item(V,W,i):
    # initialise the new lists of values and weights. They are shorter by 1
    newV = zeros(len(V)-1)
    newW = zeros(len(W)-1)
    
    # we use j, so as to not confuse it with i
    j = 0
    # go through each item in the list
    while j < len(V):
        # if the current item is before item i, add it to the new lists
        if j<i:
            newV[j] = V[j]
            newW[j] = W[j]
        # if the current item is after item i, add it to the new lists
        elif j>i:
            # the index for these items is 1 less
            newV[j-1] = V[j]
            newW[j-1] = W[j]
        # item i is not added to the new lists
        #update j
        j = j + 1
    return(newV, newW)

# adds the item with value iV and weight iW to the knapsack value and weight arrays
def add_item(KV, KW, iV, iW):
    # initialise the new lists of knapsack values and weights. They are longer by 1
    newKV = zeros(len(KV)+1)
    newKW = zeros(len(KW)+1)
    
    # we use j, so as to not confuse it with i
    j = 0
    # go through each item in the lists
    while j<len(KV):
        # add it to the new lists
        newKV[j] = KV[j]
        newKW[j] = KW[j]
        j = j + 1
    
    # add the new item to the end of the list
    newKV[len(newKV)-1] = iV
    newKW[len(newKW)-1] = iW
    return(newKV, newKW)


def knapsack(V,W,m):
    # write the algorithm here
    return(KV, KW, value)
