# Multiple Inputs (3)

Here is a slightly more complicated example from the world of physics! Consider the following equation:

`x = (v0 * t) + (0.5 * a * t**2)`

This is known as a *kinematic equation*, or an *equation of motion*, and it describes the motion of an object in one dimension (assuming constant acceleration).

* `x` denotes the object's total displacement (the distance from the *starting point* to the object)
* `t` describes the time elapsed
* `v0` denotes the object's initial velocity
* `a` denotes the object's acceleration

So, given the initial velocity and acceleration of the object, we can work out what the displacement of the object is at any given time!

You've just been given a physics homework sheet with **hundreds** of questions using this equation. Let's write a function to make it easier!

**Task:** Write a function called `displacement` which takes *initial velocity*, *acceleration* and *time* (in that order) as input, and returns the displacement *x* using the equation above.
