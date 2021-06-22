'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This file contains my entire game class which stores all information about the state of the game; this is necessary for my run and solver.

Information stored here include:
    • The player state.
    • The grid state

Instance methods here are either used for the run file or the solver file.
    • game_move(), gridstr(), and IsValid() is for the run file
    • solver_move(), validTest(), and validSolver() is for the solver file
'''

from game_parser import (parse, read_lines)
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

class Game:
    def __init__(self, filename):
        self.filename = filename
        self.grid = parse(read_lines(self.filename))
        self.player = Player()
        self.moves = []

        self.conditions = ['w', 'a', 's', 'd', 'e', 'q']

    #game instance methods
    def game_move(self, move):
        self.player.move(move)
        self.moves.append(move)

    def gridstr(self):
        return grid_to_string(self.grid, self.player)

    def IsValid(self):
        if not (0 <= self.player.row <= len(self.grid) - 1):
            return False
        
        elif not (0 <= self.player.col <= len(self.grid[self.player.row]) - 1):
            return False
        
        return True
    
    #solver instance methods:
    def solver_move(self, move):
        self.player.move(move)
    
    def validTest(self, commands):
        '''This will check to see if the solver move is valid.
        '''
        visited = []
        X = Start()
        X.starting(self)
        visited.append((self.player.row, self.player.col, self.player.num_water_buckets))

        for command in commands:
            self.game_move(command)

            if (self.player.row, self.player.col, self.player.num_water_buckets) in visited:
                return False

            elif not (0 <= self.player.row <= len(self.grid) - 1) or not (0 <= self.player.col <= len(self.grid[self.player.row]) - 1):
                return False
            
            elif (self.grid[self.player.row][self.player.col].solve(self)) == False:
                return False
            
            visited.append((self.player.row, self.player.col, self.player.num_water_buckets))

            self.grid[self.player.row][self.player.col].ValidStep(self)

        return True
    
    def validSolver(self, commands):
        '''This will check to see if our solver has found a solution.
        '''
        X = Start()
        X.starting(self)

        for command in commands:
            self.game_move(command)
            if self.grid[self.player.row][self.player.col].ValidStep(self) == True:
                return True
        
        return False