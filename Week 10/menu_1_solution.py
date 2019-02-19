choice = 1

while choice != 0:
    choice = float(input("Type 1 to say hi, 2 to introduce yourself, or 0 to exit the program: "))
    if choice == 1:
        print("Hey, how are you?")
    elif choice == 2:
        favnumber = float(input("What is your favourite number: "))
        print("Wow!", favnumber, "is a great number!")

print("Thanks!")
