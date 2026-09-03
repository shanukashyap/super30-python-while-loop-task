total = 0  # Initialization: start the total at 0

while True:  # Condition: continue looping until the user enters 0

    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break  # Termination: stop the loop when the user enters 0

    total = total + number

print("Sum:", total)
