# Knapsack Problem

For this set of exercises, you will write code based on algorithms represented using a combination of words and code. In the real world this is called pseudocode, a way to communicate algorithms to a human audience, often without a specific programming language in mind. Kind of like how mathematical equations look different when written on paper vs written in Python. Usually pseudocode contains a good amount of mathematical notation, but our pseudocode will use mostly a mix of Python syntax and English. Turning written concepts into code is an important skill to have as a scientist, as you may often need to convert other people's algorithms and methods into code to use them yourself. For these exercises you will convert our written words into a program that solves the 'knapsack problem'.

The Knapsack Problem is an optimisation problem that appears in a variety of settings, and is solved using techniques from mathematics and computer science. The basic version of the problem is very simple: You have a knapsack and a list of items with varying weights and values. You want to fill your knapsack up with as much value as possible, but the knapsack can only carry so much weight. So, you must be careful about which items you choose to pack. 

There are many algorithms designed to solve this problem, to varying degrees of success. It is often a trade off between speed and quality. For this set of exercises you will be using a 'Greedy Algorithm', which chooses speed and simplicity over quality. In computer science, a greedy algorithm is one that just makes the best decision in the moment, without planning ahead.

Below is a brief description of a greedy algorithm for the basic knapsack problem. It follows the basic structure of a program, but uses only words and indentation - the beginning of pseudocode! We will give you more detailed pseudocode later on.

**The Greedy Algorithm:**
Given a list of items with values in dollars, their corresponding weights in kilograms, and a maximum knapsack weight in kilograms:

Repeat until you can't fit anything else into the knapsack:
    Find the item on the list with the highest number of dollars per kilogram, that can fit in the remaining space in the knapsack
    Put it in the knapsack
    Remove it from the list of items

Done! 

This algorithm works because it tries to fit items into the knapsack based on their value per weight. It can sometimes leave unfilled space in the knapsack, which sometimes means it's not the best answer, but it works pretty well for simple problems!

We will help you write this algorithm step by step over the next few exercises. For now, you will just write a function that finds an item's value per weight using the following formula:

Given an item's value (v) and weight (w), the vpw (value per weight) is defined as `vpw = v/w`.  

**Task:** Write a function called `vpw(V, W, i)` that takes in a list of values `V`, a list of weights `W`, and an index `i`, and outputs the value per weight of the item with index `i`. The item will have the same index in both of the lists, so the value of item `i` will be `V[i]`, and the weight will be `W[i]`.

Example: With `V = [3, 5, 2]`, `W = [6, 2, 1]`, and `i = 1`, the output of `vpw(V, W, i)` is `2.5`.
