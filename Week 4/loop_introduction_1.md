# Introduction to Loops

Sometimes, it is useful to write programs which can run some commands more than once. To do this, we use a *loop* structure, which allows Python to run a block of code multiple times. The loop structure we will talk about here is the `while` loop. The structure of a `while` loop is as follows:

```python
while condition:
    # do some stuff if condition is true
    # do some more stuff if condition is true
    
# this code will run after the loop is complete (once the condition is false)
```

The structure is similar to conditionals, in that you need to *indent* the code that is "inside" the loop. Here's an example of how you might use a `while` loop to write a program which counts to 5.

```python
i = 1
while i <= 5:
    print("Count:", i)
    i = i + 1
print("Finished!")
```
The output of this code is:
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
Finished!
```

Take special note of this line in the program: `i = i + 1`. This line of code simply increments the value of `i`. Without this line of code, the loop would continue forever, continuously printing "Count: 1". This is because nothing in the loop would change the value of i, and the *while condition* `i <= 5` would never be false!

**Task:** Modify the following program so that it prints the squares of all the numbers from 1 to 4. Your output should be:
```
1 squared: 1
2 squared: 4
3 squared: 9
4 squared: 16
```
Make sure the program doesn't loop forever!

## Solution
```python
from pylab import *

i = 1
while i <= 4:
    print(i, "squared:", i**2)
    i = i + 1
```
