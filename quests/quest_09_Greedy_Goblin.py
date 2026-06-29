#!/usr/bin/python3

# Total gold pieces and number of friends
gold_pieces = 27
friends = 4

# Calculate how many pieces each friend gets
each_friend_gets = gold_pieces // friends

# Calculate the remainder (what the goblin keeps)
goblin_keeps = gold_pieces % friends

# Print the results
print(f"Each friend gets {each_friend_gets} gold pieces.")
print(f"The goblin keeps {goblin_keeps} gold piece(s).")
