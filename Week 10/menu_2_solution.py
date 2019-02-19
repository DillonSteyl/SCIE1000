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
