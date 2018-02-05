from pylab import *

# functions for the quadratic formula
def quad_formula_pos(a, b, c):
    ans_pos = ((-b+(b**2-4*a*c)**(1/2)/2*a)
    return(ans_pos)

a = eval(input("the value of a: "))
b = eval(input("the value of b: "))
c = eval(input("the value of c: "))

# quadratic formula
quad_pos = quad_formula_pos(a, b, c)
    
print("The solution for x is", quad_pos)
