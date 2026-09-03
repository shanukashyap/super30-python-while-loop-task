balance = 10000  # Initialization: set the starting account balance

while True:  # Condition: keep the ATM running until the user chooses Exit

    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Amount deposited successfully.")
            print("New balance:", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance = balance - amount
            print("Please collect your cash.")
            print("Remaining balance:", balance)

    elif choice == "4":
        print("Thank you for using the ATM.")
        break  # Termination: exit the ATM when the user chooses 4

    else:
        print("Invalid choice. Please try again.")
