"""Play Snakes and Ladders."""

import random

class Player:
    """ Defines a player"""
    def __init__(self, name, position=1):
        """Build a player object
        
        name -- name of the player
        position -- player position
        """
        self.name = name
        self.position = position
        
    def __repr__(self):
        return 'Player(name={})'.format(self.name)
    
    def print_name(self):
        print(self.name)


# Snakes and Ladders dictionary
SaLdic = {6: 17,
          14: 3,
          20: 15,
          24: 26,
          30: 44,
          39: 33,
          49: 62,
          66: 53,
          69: 58,
          79: 67,
          82: 86,
          84: 71,
          88: 36,
          }

#Get number of players
number_players = input('How many players?')

#Get player names
players = []
for each in range(1, 5):
    each = input('What is player', eac)

player1 = input('What is player 1\'s name?')
players.append(player1)

player1_name = input

for each in players:
    print

for each in number_players:
    each


if player.position <= 90:
    print(player.name + 'wins!')

while all([player.position < 90 for p in players]):
    


# Make a class (object) called Player
# Each player begins at position 1
# First player to get to 90 newlines

# Ask for input: how many players?
# At each player's turn, have the player press [return] to roll
# Everything else should run automatically
# When a player reaches 90, declare the winner
