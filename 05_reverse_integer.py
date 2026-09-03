number = int(input("Enter an integer: "))

# Initialization: start the reversed number at 0
reverse = 0

# Store whether the original number was negative
is_negative = number < 0

# Convert negative number to positive for digit processing
number = abs(number)

# Condition: continue while digits are remaining
while number > 0:

    digit = number % 10
    reverse = reverse * 10 + digit

    # Update: remove the last digit
    number = number // 10

# Restore the negative sign if needed
if is_negative:
    reverse = -reverse

print("Reversed number:", reverse)
