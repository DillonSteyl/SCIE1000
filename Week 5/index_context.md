Indexes (3)

It's important to remember that you cannot access elements of an array that don't exist. If your array has only 3 elements, then asking for the element at index 8 will lead to an error! The usual error message would be: `IndexError: index 8 is out of bounds for axis 0 with size 3`. Keep an eye out for it in class!

Recall, the last element in an array has index `size-1`, where size is the number of elements in the array. So, the only valid index values are from 0 to size-1. [Note: In python, a negative index is actually still valid, but we do not use them in SCIE1000.] 


**Task:** 
