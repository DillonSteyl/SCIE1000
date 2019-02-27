# Knapsack Problem

The Knapsack Problem is an optimisation problem that appears in a variety of settings, and is solved using techniques from mathematics and computer science. 

The basic version of the problem is very simple: You have a knapsack and a list of items with varying weights and values. You want to fill your knapsack up with as much value as possible, but the knapsack can only carry so much weight. So, you must be careful about which items you choose to pack. 

There are many algorithms designed to solve this problem, to varying degrees of success. The algorithms that are guaranteed to find the best answer will often take longer to run. The algorithms that are quick to run will often give answers that aren't the best. So it's a trade off between speed and quality!

For this set of exercises, you will be using one of the quick algorithms - called a 'Greedy Algorithm'. In computer science, a greedy algorithm is one that doesn't look ahead, and just makes the best decision in the moment. On some problems they work really well and give the best answers, and on others they will do okay, but aren't guaranteed to produce the best answer. The knapsack problem is one that the greedy algorithm is okay at - the answers it produces are pretty good, but not guaranteed to be the best. 

Below is a brief description of a greedy algorithm for the basic knapsack problem. Before you read it, give yourself a minute to think about how you would solve a basic knapsack problem. How would you systematically try to make good choices? How would you choose the first item to pack in the knapsack, and the second, and so forth? The more opportunities you give yourself to come up with algorithms yourself, the better you will be at understanding them. 

**The Greedy Algorithm:**
You are given a knapsack with a maximum weight, a list of items with values in dollars, and their corresponding weights in kilograms.

Repeat until you can't fit anything else into the knapsack:
- Find the item on the list with the highest number of dollars per kilogram, that can fit in the remaining space in the knapsack.
- Put it in the knapsack
- Remove it from the list

Done! 

This algorithm works because it tries to fit items into the knapsack based on their value per weight - which is the goal overall. You want the knapsack to have the highest value possible with a maximum weight. It can sometimes leave unfilled space in the knapsack, which sometimes means it's not the best answer. Regardless, it works pretty well for simple problems!

We will help you write this algorithm step by step over the next few exercises. For now, we will just write a function that finds an item's value per weight.

**Task:** Write a function called `vpw(V, W, i)` that takes in a list of values `V`, and list of values `W`, and an index `i`, and outputs the value per weight of the item with index `i`.
