number = int(input("Enter an integer: "))

# Initialization: start the digit count at 0
count = 0

# Special case: 0 is a one-digit number
if number == 0:
    count = 1

else:
    # Continue until all digits have been processed
    while number > 0:

        count = count + 1

        # Update: remove the last digit
        number = number // 10

print("Number of digits:", count)
