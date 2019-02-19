# While Loop Menus (3)

You work in a bakery and the computer's register program has stopped working. Luckily, you have time during your break to write a new one. 

**Task:** Write a program that allows the user to enter product types and codes, and keeps a record of the total cost. Apply a special discount when applicable.

Initially, print an introductory message (provided).

In the while loop, first print the running total (initially this should be 0), and then prompt the employee to enter the type of product. If the product is a drink, the employee should enter the number '1'. If it is a freshly baked item, the employee should enter the number '2'. If it is a cabinet item, the employee should enter the number '3'. If there are no more items to buy, the employee should enter the number '0', and the program should print a final message (provided) before exiting. 

For each product type, an array of costs is provided in the program. The product code of an item corresponds to the index in the relevant array. So if the user enters '1' and then '3', this means that the customer is buying the fourth item (index 3) in the drink array (product type 1), costing $2.50. 

**Special Discount:** If the customer buys a cabinet item costing more than 4 dollars (but not equal to), allow the customer to buy a loaf of bread at half price ($1.50). The employee will enter 1 if the customer says yes, and 0 for no.

**Note:** You can assume that the employees will always enter valid product codes. They are well trained!

**Important:** The input sequences are as follows:

Test 1: input 1, 3, 2, 3, 3, 3, 1, 0. Final total is 13

Test 2: input 2, 5, 3, 2, 1, 2, 6, 0. Final total is 11

Test 3: input 3, 0, 3, 2, 0, 1, 0, 0. Final total is 11.5
