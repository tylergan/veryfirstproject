'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This file contains both a BFS and a DFS path finding algorithm specific to our mazes. 
    • The BFS algorithm returns an optimal path 
    • The DFS algorithm returns a path
'''

from game import Game
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
import sys

def solve(mode, filename):
    game = Game(filename)

    if mode == 'BFS':

        commands = ['a', 'd', 's', 'w', 'e']
        queue = []
        path = ''

        for command in commands:
            add_q = path + command
            if game.validTest(add_q):
                queue.append(add_q)

        while queue:
            current_path = queue.pop(0)
            game = Game(filename)
            
            if game.validSolver(current_path):
                print('Path has {} moves.\nPath: {}'.format(len(game.moves), ', '.join(game.moves)))
                return True

            for command in commands:
                game = Game(filename)
                add_q = current_path + command

                if game.validTest(add_q) and add_q[-2:] != 'ee':
                    queue.append(add_q)
        
        print("There is no possible path.")


    elif mode == 'DFS':

        commands = ['w', 'a', 's', 'd', 'e']
        stack = []
        path = ''

        for command in commands:
            add_s = path + command
            if game.validTest(add_s):
                stack.append(add_s)

        while stack:
            current_path = stack.pop()
            game = Game(filename)
            
            if game.validSolver(current_path):
                print('Path has {} moves.\nPath: {}'.format(len(game.moves), ', '.join(game.moves)))
                return True

            for command in commands:
                game = Game(filename)
                add_s = current_path + command

                if game.validTest(add_s) and add_s[-2:] != 'ee':
                    stack.append(add_s)
        
        print("There is no possible path.")

    
    else:
        print("Usage: python3 solver.py <filename> <mode>")

try:
    filename = sys.argv[1]
    mode = sys.argv[2]

except IndexError:
    print("Usage: python3 solver.py <filename> <mode>")
    exit()

solve(mode, filename)