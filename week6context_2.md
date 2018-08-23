# Fill in the functions!

Lets suppose you're in a situation where you want to save some money for an upcoming purchase, but as a broke uni student, you're finding it really difficult. 

A friend has been kind enough to provide a Python program they wrote that calculates how far they are from their savings goal by calculating the amount of money in their savings account each month. The program adds monthly interest and takes away any money spent on debts.

However, your friend has provided the code without any of the function definitions.

**Task:**
Your task is to write the function definitions that will make the program work.

**Hints**
1. There are three functions missing, so be sure to write a definition for each of them. Read the code provided carefully to determine 
what they are called, what variables need to be passed to them, and what they need to return.

2. Remember that the amount of money in the account after each month can be found using the compound interest formula, given by
```python
money = (1+r)*money_last_month
```
where r is the monthly interest rate as a decimal.

3. Functions can return any variables that have been previously defined. 

4. Debts should be removed **after** calculating the new amount of savings each month. 


# Solution
```python
GOAL_NOT_MET = 0
GOAL_MET = 1

#Write your function definitions here:
def get_new_savings(savings, interest_rate, debts):
    growth = (1+interest_rate)*savings
    total = growth - debts
    return(total)

def check_goal(savings, goal):
    if (savings >= goal):
        return(GOAL_MET)
    else:
        return(GOAL_NOT_MET)

def get_difference(savings, goal):
    difference = goal - savings
    return difference

interest_rate = float(input("Enter the monthly interest rate as a decimal: "))
savings = float(input("Enter your current savings: "))
goal = float(input("Enter the amount of money you want to save: "))
months = float(input("Enter the number of months you want to check: "))

i = 1
while (i <= months):
    print("You are currently in month", i)
    debts = float(input("Enter any debts for the month: "))
    savings = get_new_savings(savings, interest_rate, debts)
    monthly_check = check_goal(savings, goal)
    if (monthly_check == GOAL_MET):
        print("You have met your saving goal!")
        i = months
    else:
        difference = get_difference(savings, goal)
        print("You are", difference, "away from your goal.")
    i = i+1
if (monthly_check == GOAL_NOT_MET):
    print("You didn't save enough money in the given timeframe. ")
```
