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

Pretty neat! Multiplication, addition, subtraction, division, and exponentiation all work on arrays. Just remember to use the array() function!

This will become very useful later, but for now lets calculate some grades.

**Task:** You want to write a program that calculates all the marks for your courses simultaneously. There are three types of assessment: exams, assignments, and attendance. Fortunately, all of the courses were standardised so that each assessment type is worth the same amount. Exams are worth 50% of the total grade, assignments are worth 35%, and attendance is worth 15%. 

So for one of your courses, if you recieved 90% for your exam, 80% for your assignments, and 95% for attendance, your total grade will be 87.25%. Check this on paper to make sure you are doing the correct calculation. It should be `0.5*90 + 0.35*80 + 0.15*95 = 87.25`.

The program currently has three arrays: `exams`, `assignments`, and `attendance`. The first element of each array corresponds to your first course. The second elements all correspond to your second course, and so on. The `final` array is yet to be defined, and should be the final percentage grade for each course. 

Modify this program so that it calculates the total grade for each course you are is enrolled in, given the marks in the three arrays. Store the final grades in the variable 'final'.

Use the following print statement to end your program: print("The final marks out of 100 are:", final").

**Hint:** Don't try to over complicate it. This question is easier than it seems! You should be able to make the `final` array with juse one line of code.



## Solution
```python
from pylab import *

exams = array([82, 48, 55, 67])
assignments = array([90, 83, 64, 88])
attendance = array([100, 80, 50, 70])

final = exams*0.5+assignments*0.35+attendance*0.15

print("The final marks out of 100 are:", final)
```

