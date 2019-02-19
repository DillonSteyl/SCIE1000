# Indexes (1) - Accessing Array Elements.

While it's fun to do operations on an entire array, it can often be useful to access *individual entries* in an array. To access an individual entry in an array, we use its **index**, which refers to its position in the array. If we have an array called `A`, and we want to access the entry at position `i` of the array, we use `A[i]`. For example, `A[2]` refers to the entry in position 2 of the array `A`.

**Important:** In Python, the first element of an array has index `0`. This also means that for an array of size `n`, the *last* element in the array has index `n-1`. Make sure you remember this! Take a look at the following program:

```python
number_array = array([3, 6, 9, -12, 15])
print("First element is:", number_array[0])
print("Last element is:", number_array[4])
print("Middle element is:", number_array[2])
```

The output is:

```
First element is: 3
Last element is: 15
Middle element is: 9
```

**Task:** Modify this program so that it prints the first and fourth prime. To do this, replace the comments `#?#` with the appropriate index.
