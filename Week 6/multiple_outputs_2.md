# Fill in the Functions (1)

**Task:** A program has been written but the functions have gone missing and there aren't any good comments! Define and write the functions so that the program passes all the tests. 

**Note:** Please use `exp` instead of `e**` when calculating exponentials in this question, as they may give slightly different answers. Additionally, we will not input any y1=0  or y2=0 values into the exponential function, so there's no need to worry about that. 

To solve this you may want to try finding the formulas on paper first. Try it yourself before reading the hint below:

**Hint:**

For Linear equations: 

Find m first by using the formula for m. Then, use m and one of the points to find c by rearranging `y = m*x + c`.

For Exponential equations:

You can't guarantee that one of the x values is 0 (which would mean the corresponding y value is A0). But, we will not give you any y values that are 0, so that means we can do the following maths without worrying about dividing by 0 or calling log(0).

So, if both sets of values are subbed into the Exponential equation you get:

`y1 = A0 * exp(k*x1)`
`y2 = A0 * exp(k*x2)`

If you divide these two equations you get:

`y1/y2 = A0*exp(k*x1)/(A0*exp(k*x2))`

Which simplifies to:

`y1/y2 = exp(k*(x1-x2))`

Rearranged to find k:

`k = log(y1/y2)/(x1-x2)` (log here being the natural log). 

Once k is found, one of the equations can be rearranged to find A0:

`A0 = y/(exp(k*x)`

So that's only two lines of calculations you need. First to find k, and then to find A0.
