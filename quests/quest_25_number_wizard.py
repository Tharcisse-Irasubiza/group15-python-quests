# Quest 25: The Number Wizard
# Grand Challenge: upgrade the guessing game to say "too high" or "too low".

import random

# The wizard picks a secret number between 1 and 20
secret_number = random.randint(1, 20)

print("Welcome to the Number Wizard! I'm thinking of a number between 1 and 20.")

guess = 0  # start with a value that can't be the secret number

# Keep asking until the player guesses correctly
while guess != secret_number:
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {secret_number}. You are a true Number Wizard!")
