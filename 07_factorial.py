number = int(input("Enter a number: "))

factorial = 1
i = 1

# Initialization: i starts at 1
while i <= number:

    factorial = factorial * i

    # Update: increase i
    i = i + 1

print("Factorial:", factorial)