GOAL_NOT_MET = 0
GOAL_MET = 1

# Write your function definitions here:


interest_rate = float(input("Enter the interest rate as a decimal: "))
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
