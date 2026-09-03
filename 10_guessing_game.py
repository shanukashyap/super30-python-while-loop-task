secret_number = 42

# Initialization: get the first guess
guess = int(input("Guess the number: "))

# Condition: continue while the guess is incorrect
while guess != secret_number:

    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    # Update: ask the user for another guess
    guess = int(input("Guess again: "))

print("Congratulations! You guessed correctly.")
