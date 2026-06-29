# Quest 15: The Nested Riddle
# Concept: Nested if statements - an if statement inside another if statement.

# First choice: left or right (.lower() lets the answer be in any case)
direction = input("You reach a fork in the path. Do you go 'left' or 'right'? ").lower()

if direction == "left":
    # This second question is only asked if the player chose "left"
    action = input("You face a deep river. Do you 'swim' or 'wait'? ").lower()
    if action == "swim":
        print("You swim across and find a hidden treasure chest! You win!")
    else:
        print("You wait too long and night falls. The adventure ends here.")
else:
    print("You go right and hit a dead end. Better luck next time, adventurer.")
