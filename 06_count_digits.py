number = int(input("Enter an integer: "))

count = 0

# Continue until no digits remain
while number > 0:

    count = count + 1

    # Remove the last digit
    number = number // 10

print("Number of digits:", count)