# Quest 5: The Echoing Cave
# Concept: Reassigning variables - the value in a variable's "box" can change.

# Set the player's starting health
player_health = 100
print(f"Starting health: {player_health}")

# A monster attacks! Lose 25 health.
player_health = player_health - 25
print(f"A monster attacks! Health is now: {player_health}")

# The player finds a potion! Gain 10 health.
player_health = player_health + 10
print(f"You drink a potion! Health is now: {player_health}")

# Show the final health
print(f"Final health: {player_health}")
