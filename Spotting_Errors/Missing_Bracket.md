# Spot the Error

**Task:** Find an fix the error in the following code

**Hint:** 

## Program
```python

print("This is a program to solve the quadratic formula, given input for a, b and c for a quadratic formula")
print("0 = ax^2 + bx + c")

#functions for the quadratic formula
def quad_formula_pos(a, b, c):
    ans_pos = ((-b+(b**2-4*a*c)**(1/2)/2*a)
    return(ans_pos)
    
#functions for the quadratic formula
def quad_formula_neg(a, b, c):
    ans_neg = ((-b-(b**2-4*a*c)**(1/2))/2*a)
    return(ans_neg)

a = input("the value of a: ")
b = input("the value of b: ")
c = input("the value of c: ")

# quadratic formula
quad_pos = quad_formula_pos(a, b, c)
quad_neg = quad_formula_neg(a, b, c)
    
print("The solution for x is", quadrat_pos, "or", quad_neg)
```

## Solution
```python

print("This is a program to solve the quadratic formula, given input for a, b and c for a quadratic formula")
print("0 = ax^2 + bx + c")

#functions for the quadratic formula
def quad_formula_pos(a, b, c):
    #missing bracket in positive quadratic formula
    ans_pos = ((-b+(b**2-4*a*c)**(1/2))/2*a) 
    return(ans_pos)
    
#functions for the quadratic formula
def quad_formula_neg(a, b, c):
    ans_neg = ((-b-(b**2-4*a*c)**(1/2))/2*a)
    return(ans_neg)

a = input("the value of a: ")
b = input("the value of b: ")
c = input("the value of c: ")

# quadratic formula
quad_pos = quad_formula_pos(a, b, c)
quad_neg = quad_formula_neg(a, b, c)
    
print("The solution for x is", quadrat_pos, "or", quad_neg)

```
