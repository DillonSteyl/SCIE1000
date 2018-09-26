# While Loop Menus (2)

The last program we wrote was pretty boring, let's write something that is a bit more dynamic.

**Task:** You will write a program that operates like a bank account. The user will have an initial deposit, and is allowed to deposit more money, withdraw money, or close their bank account. Each time they make a change, their balance gains interest.

Initially, ask the user to input a number (message provided). This will be their initial deposit.

In the while loop, you will first allow the user's balance to gain interest. The interest rate is 3% (So if they have 100 dollars, then they should have 103 dollars after interest. If they have -200 dollars, then they will have -206 dollars after interest). After this, you will print the user's balance (message provided). Then, you will prompt the user to make a choice (message provided). 

The menu should have the following behaviour:

Input 1: Ask the user to input a number, deposit that amount into the bank account.

Input 2: Ask the user to input a number, withdraw that amount from the bank account.

Input 3: The user has elected to close their bank account. End the while loop and print a final message (provided). 


```
from pylab import *

balance = float(input("Enter your initial deposit: "))

choice = 1

while choice != 3:
    balance = balance * 1.03
    print("Your balance is", balance)
    choice = float(input("Enter 1 for deposit, 2 for withdraw, and 3 to close the account"))
    if choice == 1:
        amount = float(input("Enter the amount to deposit: "))
        balance = balance + amount
    elif choice == 2:
        amount = float(input("Enter the amount to withdraw: "))
        balance = balance - amount
        
print("You have closed your bank account with a final balance of", balance)


```