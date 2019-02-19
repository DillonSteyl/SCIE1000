# Euler's Method (1)

For the following exercises you will be writing a program that implements Euler’s method (pronounced ‘oy-ler’). It may be the case that you have not yet encountered Euler’s method in the course. Euler’s method can be found in Chapter 10.2 of your notes, which gives a good description of why this algorithm works. But for our purposes, we only need to know the algorithm itself - so there's no need to worry if you are yet to understand it.

Euler’s method is used to approximate a function when only the derivative and a particular value is known. Given an initial value ` current y`, a corresponding value `x`, and a step size `h`, the next value for `y` is calculated using the following formula:

`next y = current y + f'(x)*h`

If you want to calculate more steps, just reuse the formula but with your new `y` value. The new `x` value is also updated to `x+h`. 

This can be a bit daunting at first, so we will start with the easiest part: writing a function for the derivative. 

**Task:** To start, write a function called `fdash(x)`, that returns the value of the derivative at x. The formula for the derivative which we will be using as a placeholder is:

`fdash = 0.05x * exp(0.05x)`

Round the output to 5 decimal places. Do not print anything, call your function, or ask for any input. 

**Important:** For this set of exercises, make sure to use the `exp` function instead of `e**`, otherwise you will sometimes get slightly different answers!
