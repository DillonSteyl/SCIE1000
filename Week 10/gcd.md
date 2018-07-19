Note: The Modulo Operator exercise should be completed before attempting this question

For this question, you will write a program that implements an algorithm invented by Euclid, an ancient Greek mathematician. The algorithm is known as Euclid's algorithm, and finds the greatest common divisor (gcd) for any pair of integers. The greatest common divisor for a pair of numbers is the largest number that divides both of them evenly. For example:

````
gcd(15,25) = 5
gcd(21,7) = 7
gcd(9,5) = 1
gcd(8,12) = 4
````

Note that for some pairs, the only number that will divide both is 1. This means that the pair is known as 'co-prime'. 9 and 5 do not share any divisors except for 1, so they are co-prime. 

The algorithm is well known for being quick and elegant, and it is based on the fact that gcd(a,b) = gcd(b, a%b). Here it is:

Given a and b:
1. Repeat while a%b!=0 (a is not divisible by b):
    - remainder is set to a%b
    - a is set to b
    - b is set to remainder
    - This loop will always eventually get to a%b=0 and finish on its own (thanks Euclid!), so no need to put in a counter like i
2. Once the loop ends, the gcd is b

*Task:* Take a and b as input from the user (in that order), and find the greatest common divisor of a and b using the algorithm given. Once the gcd is found, use this print statement: print("The gcd is",b). 

If a and b are co-prime (their gcd is 1), use this print statement afterwards: print("These two numbers are co-prime."). 


## Solution

````
from pylab import *

a = int(input("What is a: ")
b = int(input("What is b: ")

while a%b!=0:
    remainder = a%b
    a = b
    b = remainder

print("The gcd is", b)

if b==1:
    print("These two numbers are co-prime.")
````
