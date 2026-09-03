number = int(input("Enter a number: "))

# Initialization: start factorial at 1 and counter at 1
factorial = 1
i = 1

# Condition: continue while counter is less than or equal to number
while i <= number:

    factorial = factorial * i

    # Update: increase counter by 1
    i = i + 1

print("Factorial:", factorial)
