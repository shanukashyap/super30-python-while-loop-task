correct_password = "python123"

# Initialization: get the first password attempt
password = input("Enter password: ")

# Condition: continue while the password is incorrect
while password != correct_password:

    print("Incorrect password. Try again.")

    # Update: ask for another password attempt
    password = input("Enter password: ")

print("Password correct. Access granted.")
