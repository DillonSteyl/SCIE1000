# Introduction

The questions for this week involve systems of differential equations, which are used in applications like life cycle modelling and infectious disease modelling.

While this first exercise will not involve differential equations, it will help you complete the remaining exercises for this week. So make sure you get it right before moving on. 

**Task:** Write a function named `highest(A)` that returns the index of the highest element in the array A. If there are multiple elements in the array that are equally high, return the index of the first element with that value. You can assume that the array will not be empty. 

Here are a couple examples:

Given `A = [3,6,1,5,7,6]`, the answer is 4. (Because 7 is the highest number in the array, and its index is 4)

Given `A = [0,0,4,1,4,4]`, the answer is 2. (Because 4 is the highest number in the array, and the index of the first occurrence is 2)

Given `A = [8]`, the answer is 0. (Because 8 is the highest number in the array, and its index is 0)

**Hint:** Along with a while loop, you will need an extra variable that keeps track of the index of the highest element found so far. 
