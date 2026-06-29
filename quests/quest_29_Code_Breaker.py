#!/usr/bin/python3

# Secret code
secret_code = 42

# Allow 3 attempts
for attempt in range(3):
    guess = int(input("Guess the secret code: "))

    if guess == secret_code:
        print("Correct! You unlocked the secret code.")
        break
    else:
        print("Incorrect guess.")

else:
    print("Game Over! You've used all 3 attempts.")
