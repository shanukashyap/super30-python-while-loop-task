number = int(input("Enter a number: "))

# Initialization: start the total sum at 0
total = 0

# Convert negative number to positive for digit processing
number = abs(number)

# Condition: continue while digits are remaining
while number > 0:

    digit = number % 10
    total = total + digit

    # Update: remove the last digit
    number = number // 10

print("Sum of digits:", total)
