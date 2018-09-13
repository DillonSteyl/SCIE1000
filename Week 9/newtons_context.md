# Newton's Method (5) - Voltages


Capacitors are a crucial electrical component that are used in the development of both micro-electronic products and large scale circuit development. To summarise briefly, they consist of two conductive metal plates, and store energy, similar to a battery. 

Between the two plates is a voltage difference. It is possible that the voltage difference across a capacitor is too high, and causes the component to rupture and fail.  

You have been given a particular capacitor whose maximum voltage difference is 10000V, and you want to know the current at which this occurs.

The following equation gives the voltage difference (in volts) given a current c (in amps). 

`V(c) = ce^(0.05c)*1000`

It's derivative is as follows:

`V'(c) = (50c + 1000)e^(0.05 c)`

If we wanted to solve this using Newton's Method, then V(c) would be replaced with:

`W(c) = ce^(0.05c)*1000-10000`

Notice that when `W(c)` is equal to 0, that same `c` value will correspond with `V(c)` equalling 10000. Note that the derivative will stay the same (10000 has no `c` term, so it disappears when differentiated).

It's not that hard to calculate the current for the maximum voltage difference for just one capacitor. But, you have been given a box of capacitors all with different maximum voltage differences but the same equation for voltage difference. So, this means that W(c) becomes:

`W(c) = ce^(0.05c)*1000 - max_voltage`

where `max_voltage` is the maximum voltage difference for that capacitor in volts. 

You want to find out which capacitors you can use through different circuits, all with different currents. 

**Task:** Write a function called `will_it_rupture(current, max_voltage)`, where `current` is the current you want to use through your circuit in amps, and voltage is the maximum voltage difference for that particular capacitor in volts. `will_it_rupture` will return two values, the first is 0 if the capacitor should not be used with that current, and 1 otherwise (that is, if the maximum voltage difference is less than or equal to the current used in the circuit, then it is not acceptable to use that capacitor). The second variable is the current at which the maximum voltage difference occurs for that capacitor. 

Copy paste your code from the previous exercises. You want the `f`, `fdash`, `onestep` and `newtons` functions.

You will have to make the following changes to your existing functions before writing your `will_it_rupture` function:

1. The `fdash` function should use the `V'(c)` equation given.

2. The `f` function should take in two variables as input: `f(x, max_voltage)`. The equation used should be the `W(c)` function. 

3. The `onestep` function should take in two variables as input: `onestep(x, max_voltage)`. The `f` function is called in this function, so that should be updated so that the `max_voltage` variable is also passed in.

4. The `newtons` function should take in four variables as input: `newtons(x, n, p, max_voltage)`. Again, since the `onestep` function has been updated to take in the `max_voltage` variable, the line where the `onestep` function is called needs to be update so that the `max_voltage` variable is passed in. Additionally, the `newtons` function should be changed to return only one variable: the final guess. It should no longer return the number of steps.  

For simplicity, set `n = 15` and `p = 1` for Newton's Method, and start with an initial guess of `x = 1`. You are still expected to round the output of the `f`, `fdash`, and `onestep` functions to 5 decimal places.

**Note:** We have written tests for all five of the functions, so you can check to see where your errors are. 

# Solution


```
def f(c, max_voltage):
    y = round(c*exp(0.05*c)*1000 - max_voltage,5)
    return(y)
    
def fdash(c):
    d = round((50*c + 1000)*exp(0.05*c),5)
    return(d)
    
def onestep(x, max_voltage):
    newguess = round(x - f(x, max_voltage)/fdash(x),5)
    return(newguess)
    
def newtons(x, n, p, max_voltage):
    currentStep = 1
    stop = 0
    while stop==0 and currentStep <= n:
        previous = x
        x = onestep(x, max_voltage)
        if 100*abs(previous - x)/previous < p:
            stop = 1
        currentStep = currentStep + 1
    return(x)
    
def will_it_rupture(current, max_voltage):
    guess = newtons(1, 15, 1, max_voltage)
    if guess<=current:
        return(0, guess)
    else:
        return(1, guess)
    
    
```
