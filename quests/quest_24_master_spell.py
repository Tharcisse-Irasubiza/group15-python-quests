# Quest 24: The Master Spell
# Concept: Calling one function from another and passing a returned value along.

def ask_for_age():
    """Ask the user for their age and return it as an integer."""
    age = int(input("How old are you? "))
    return age

def can_they_vote(age):
    """Take an age and print whether that person can vote."""
    if age >= 18:
        print("You are old enough to vote!")
    else:
        print("Sorry, you are not old enough to vote yet.")

# Call the first function and store the value it returns
user_age = ask_for_age()

# Pass that returned value into the second function
can_they_vote(user_age)
