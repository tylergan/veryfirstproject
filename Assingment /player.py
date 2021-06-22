'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This file contains the player class which holds all relevant information about the player state.

Information stored here includes:
    • Player coordinates
    • Number of water buckets
'''

class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col = 0

    def move(self, move):
        '''This function takes in an input (w, a, s, d, e) and updates the player's coordinates accordingly.

        Arguments:
            move --> the input of w, a, s, d, e
        
        The player's x and y coordinates update depending on the move received.
        '''
        if move == 'd': 
            self.col += 1
        
        elif move == 'a': 
            self.col -= 1
        
        elif move == 'w': 
            self.row -= 1
        
        elif move == 's': 
            self.row += 1

        elif move == 'e': 
            pass