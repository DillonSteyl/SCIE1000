from pylab import *

def vpw(V,W,i):
    return(V[i]/W[i])

def best_item(V,W,space):
    best_index = -1
    i = 0
    while i<len(V):
        if W[i]<=space:
            if best_index ==-1 or vpw(V,W,i)>=vpw(V,W,best_index):
                best_index = i
        i = i + 1
    return(best_index)

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
    space = m
    knapsack_value = 0
    KV = array([])
    KW = array([])
    best_index = 0
    while best_index!=-1:
        best_index = best_item(V,W,space)
        if best_index!=-1:
            KV, KW = add_item(KV, KW, V[best_index], W[best_index])
            space = space - W[best_index]
            knapsack_value = knapsack_value + V[best_index]
            V, W = remove_i
    return(KV, KW, knapsack_value)
