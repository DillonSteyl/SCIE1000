# Newton's Method (2)

Recall that the key formula for Newton's method is as follows:

`x(i+1) = x(i) - f(x(i))/f'(x(i))`

Applying a single step of Newton's Method thus has the following form:

`new_x = old_x - f(old_x)/f'(old_x)`

**Task:** Write a function called `onestep(x)` that applies one step of Newton's method given an initial guess of `x`, and returns the next guess. The function and its derivative are the same as the previous exercise. Please copy and paste your previous code in this exercise for `f(x)` and `fdash(x)`. You should have three functions defined: `f(x)`, `fdash(x)`, and `onestep(x)`.

Round the answer to 5 decimal places. 

**Reminder:** Only use `exp`, not `e**`.
