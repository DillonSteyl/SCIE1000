# Introduction to Arrays (2) - Operations on Arrays

Now that we know how to create arrays in Python, let's talk about what we can do to them. Some of the operations you have used so far in the course work on arrays too. For example, we can multiply every value in an array like this:

```python
X = array([1, 2, 3, 4])
print(2*X)
```

The output is:

```
[2, 4, 6, 8]
```

Python performs the operation on *each* element in the *entire* array. So it does the operation on the first element by itself, then the second, and so on. Let's have another look:

```python
X = array([1, 2, 3, 4, 5, 6, 7, 8, 9])
Y = X**2+2*X
print(Y)
```

The output is:

```
[ 3  8 15 24 35 48 63 80 99]
```

And this works on two arrays at the same time too!

```python
X = array([1, 2, 3, 4])
Y = array([5, 6, 7, 8])
Z = X*Y
print(Z)
```

The output is:

```
[ 5 12 21 32]
```

It's important to note how this works. The operations occur one element at a time. When there are multiple arrays in an equation, it does the operation on the first elements, then the second elements, and so on. So first it multiplies 1 by 5, which becomes the first element of Z. Then it multiplies 2 by 6, which becomes the second element of Z. It works the same way as this no matter how complicated your equation is, or how many arrays are used.

**Note:** Having multiple arrays in one equation will only work if the arrays have the same length. 

Pretty neat! Multiplication, addition, subtraction, division, and exponentiation all work on arrays. Just remember to use the array() function!

**Task:** Make an array filled with the values 1, 4, 9, 16 and assign it to the array `squares`. Make another array filled with the values 1, 8, 27, 64 and assign it to the array `cubes`.
Now, take the square root of the `squares` array, take the cube root of the `cubes` array, and add them together and assign them to the variable `result`. 
