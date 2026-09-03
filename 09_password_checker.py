correct_password = "python123"

password = input("Enter password: ")

# Continue asking while password is incorrect
while password != correct_password:

    print("Incorrect password. Try again.")

    password = input("Enter password: ")

print("Password correct. Access granted.")