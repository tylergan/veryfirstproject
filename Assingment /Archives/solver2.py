from queue import Queue
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
        queue = Queue()
        path = ''

        for command in commands:
            add_q = path + command
            if game.validTest(add_q):
                queue.put(add_q)
        
        i = 0
        while queue:
            current_path = queue.get()
            game = Game(filename)
            
            if game.validSolver(current_path):
                print("FOUND")
                print("number of moves: {}".format(len(game.moves)))
                print(game.moves)
                print("\niterations: {}".format(i))
                return True

            for command in commands:
                game = Game(filename)
                add_q = current_path + command

                if game.validTest(add_q) and add_q[-2:] != 'ee':
                    queue.put(add_q)
            
            i += 1
        
        print("FAILED")
        print("iterations: {}".format(i))
        return False



try:
    filename = sys.argv[1]
    mode = sys.argv[2]

except IndexError:
    print("Usage: python3 solver.py <filename> <mode>")
    exit()

solve(mode, filename)