while True:  # Initialization: start the calculator menu loop

    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Condition: keep showing the menu until the user chooses Exit
    if choice == "5":
        print("Calculator closed.")
        break  # Termination: exit the loop when choice is 5

    if choice in ["1", "2", "3", "4"]:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)

        elif choice == "2":
            print("Result:", num1 - num2)

        elif choice == "3":
            print("Result:", num1 * num2)

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)

    else:
        print("Invalid choice. Please try again.")
