# Introduction

For this week there are two sets of exercises:

1. (moderate) The Modular Operator. You will be introduced to a new operator, 'modulo', that you can use like addition, subtaction, multiplication, etc. This content isn't needed for the course but can be a lot of fun. For the final exercise you will implement an algorithm invented thousands of years ago by Euclid, a Greek mathematician. 
2. (challenging) While Loop Menus. In this set of exercises we will expand on an alternative way to use while loops that we briefly went over in week 4. This content is helpful for the course (and can appear in exams and assignments sometimes), and for your programming in general. For the final exercise you will write a program that allows the user to play a buried treasure game. 


**Task:** Write a program that takes a number `n` as input from the user, and prints ":)" `n` times. 


```
from pylab import *

n = float(input("Give me a number: "))

i = 0
while i<n:
    print(":)")
    i = i + 1

```
