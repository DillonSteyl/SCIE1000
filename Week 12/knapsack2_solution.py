from pylab import *

def vpw(V,W,i):
    return(V[i]/W[i])

def best_item(V,W,space):
    best_index = -1
    
    i = 0
    while i<len(V):
        if W[i]<=space and vpw(V,W,i)>=vpw(V,W,best_index):
            best_index = i
        i = i + 1
        
    return(best_index)
