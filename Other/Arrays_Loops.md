# Combining Multiple Themes

Now you're familiar with all the programming concepts in this course, let's look at combining some of the different aspects

**Task:** The first 10 Fibbonachi numbers are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. Edit the following program so it outputs an array with the correct numbers in it.

**Hint:** You will need to index the two previous array elements. e.g. `fibbonachi_array[0] + fibbonachi_array[1]` is equal to the third Fibbonachi number

## Program
```python
fibbonachi_array = zeros(10)
fibbonachi_array[0] = 1
fibbonachi_array[1] = 1
i=2
# what are the bounds of the while loop?
    # a fibonacci number is the sum of the two previous numbers
    i = i + 1
    
print("The first 10 Fibbonachi numbers are", fibbonachi_array)
```

## Solution
```python
fibbonachi_array = zeros(10)
fibbonachi_array[0] = 1
fibbonachi_array[1] = 1
i=2
while i < 10:
    fibbonachi_array[i] = fibbonachi_array[i-2] + fibbonachi_array[i-1]
    i = i + 1
    
print("The first 10 Fibbonachi numbers are", fibbonachi_array)
```
