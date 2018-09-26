# While Loop Menu (3)

You work in a bakery and the computer's register program has broken. Luckily, you have time during your break to write a new one. 

**Task:** Write a program that allows the user to enter product types and codes, and keeps a record of the total cost. Apply a special discount when applicable.

Initially, print an introductory message (provided).

In the while loop, first print the running total (initially this should be 0), and then prompt the employee to enter the type of product. If the product is a drink, the employee should enter the number '1'. If it is a freshly baked item, the employee should enter the number '2'. If it is a cabinet item, the employee should enter the number '3'. If there are no more items to buy, the employee should enter the number '0', and the program should print a final message (provided) before exiting. 

For each product type, an array of costs is provided in the program. The product code of an item corresponds to the index in the relevant array. So if the user enters '1' and then '3', this means that the customer is buying the fourth item (index 3) in the drink array (product type 1), costing $2.50. 

**Special Discount:** If the customer buys a cabinet item costing more than 4 dollars (but not equal to), allow the customer to buy a loaf of bread at half price ($1.5). The employee will enter 1 if the customer says yes, and 0 for no.

**Note:** You can assume that the employees will always enter valid product codes. They are well trained!

```
from pylab import *

drinks = array([3, 3.5, 2, 2.5, 6, 3, 3, 5, 2.5])
fresh = array([2.5, 2.5, 2.5, 3, 3, 3, 2, 0.5, 0.5, 1.5, 5, 5])
cabinet = array([4, 4, 4.5, 6, 3.5, 5, 3.5, 3.5])

total = 0

product_type = 1

while product_type!=0:
    print("The total is", total)
    product_type = float(input("Enter the product type (1 = drinks, 2 = fresh, 3 = cabinet, 0 to exit): "))
    if product_type == 1:
        product_code = float(input("Enter the product code: "))
        total = total + drinks[product_code]
    elif product_type == 2:
        product_code = float(input("Enter the product code: "))
        total = total + fresh[product_code]
    elif product_type == 3:
        product_code = float(input("Enter the product code: "))
        if cabinet[product_code]>4:
            choice = float(input("Enter 1 for yes, 0 for no: "))
            if choice==1:
                total = total + 1.5
        total = total + cabinet[product_code]
     
    

print("The final total is", total)



```
