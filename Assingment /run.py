'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This file is the run engine of our game. It has two modes: a play mode and a normal mode.
'''

from game import Game
import os
import sys
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def play_mode():
    invalid = Wall()

    X = Start()
    X.starting(game)
    print(game.gridstr())

    while True:
        move = input('Input a move: ').lower()

        if move not in game.conditions:
            os.system('clear')
            print(game.gridstr())
            print('Please enter a valid move (w, a, s, d, e, q).\n')
        
        elif move == 'q':
            print('\nBye!')
            exit()
        
        else:
            os.system('clear')
            game.game_move(move)
            
            if not game.IsValid():
                invalid.step(game)

            else:
                game.grid[game.player.row][game.player.col].step(game)
           
            
def normal_mode():
    invalid = Wall()

    X = Start()
    X.starting(game)
    print(game.gridstr())

    while True:
        move = input('Input a move: ').lower()

        if move not in game.conditions:
            print(game.gridstr())
            print('Please enter a valid move (w, a, s, d, e, q).\n')
        
        elif move == 'q':
            print('\nBye!')
            exit()
        
        else:
            game.game_move(move)
            
            if not game.IsValid():
                invalid.step(game)

            else:
                game.grid[game.player.row][game.player.col].step(game)

try:
    filename = sys.argv[1]

except IndexError:
    print('Usage: python3 run.py <filename> [play]')
    exit()

game = Game(filename)

if len(sys.argv[1:]) != 2:
    normal_mode()

else:
    mode = sys.argv[2]
    if mode == 'play':
        play_mode()
        
    else:
        normal_mode()