secret_number = 42

guess = int(input("Guess the number: "))

# Continue until the user guesses correctly
while guess != secret_number:

    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Guess again: "))

print("Congratulations! You guessed correctly.")