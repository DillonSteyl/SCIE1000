Capacitors are a crucial electrical component that are used in the development of both micro-electronic products and large scale circuit development. To summarise briefly, they consist of two conductive metal plates, and store energy, similar to a battery. 

Between the two plates is a voltage difference. It is possible that the voltage difference across a capacitor is too high, and causes the component to rupture and fail. 

Suppose the voltage across a capacitor is given by 
```python
V(t) = K*e**(50*t)
```
where K is a constant. The initial voltage across the component is 20V.

We want to write a program that predicts the time the capacitor will rupture using Newton’s method, and also determine the current passing through the capacitor at the time of rupture. The maximum voltage difference permitted across the component is 10,000V, and the current across the capacitor will be given by
```python
Vdash(t) * Capacitance
```
where the capacitance is equivalent to 3 * 10^-6.

Below are some tips for writing your program:
1. Functions are recommended for this program. Consider where these would be helpful. 
2. This question will require you to do some quick calculations prior to writing your program. Refer to the steps outlined in class on how to implement Newton’s method to ensure you are on the right track. 
3. Vdash(t), the derivative of V(t), is equivalent to 50 times V(t). If you want the derivative of V(t) + k, where k is some constant, the derivative will still be Vdash(t).
4. Use an initial estimate of … for the Newton’s method and apply 5 steps. 
