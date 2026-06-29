#!/usr/bin/python3
# Quest 28: The Adventure Begins
# Goal: Build a text-based Choose Your Own Adventure game using functions
# for different locations, with at least two different endings.

def forest_path():
    print("\nYou enter a dark forest. A wolf blocks your path.")
    choice = input("Do you 'fight' or 'run'? ").lower()
    if choice == "fight":
        print("You bravely defeat the wolf and find a hidden treasure! You win!")
    else:
        print("You run safely back to the village. Adventure over.")

def river_path():
    print("\nYou reach a wide river. There's an old boat nearby.")
    choice = input("Do you 'swim' or 'use the boat'? ").lower()
    if choice == "use the boat":
        print("The boat carries you safely across to a hidden village. You win!")
    else:
        print("The current is too strong and sweeps you away. Game over.")

def start_adventure():
    print("Welcome, adventurer! You stand at a crossroads.")
    choice = input("Do you go 'forest' or 'river'? ").lower()

    if choice == "forest":
        forest_path()
    elif choice == "river":
        river_path()
    else:
        print("You stand still, confused, until night falls. The adventure ends.")

start_adventure()
