# import copy
# from game import Game
# from cells import (
#     Start,
#     End,
#     Air,
#     Wall,
#     Fire,
#     Water,
#     Teleport
# )
# import sys

# def solve(mode, filename):
#     game = Game(filename)

#     if mode == 'BFS':
        # commands = ['a', 'd', 'w', 's', 'e']

        # X = Start()
        # X.starting(game)
        # game.visited.append((game.player.row, game.player.col, game.player.num_water_buckets))
        # queue = [game]
        # while queue:
        #     current = queue.pop(0)

        #     for command in commands:
        #         #creating a new instance of the game class which will inherit the attributes of the root node.
        #         neighbour = Game(filename)
        #         neighbour.player.row, neighbour.player.col, neighbour.player.num_water_buckets = current.player.row, current.player.col, current.player.num_water_buckets
        #         neighbour.visited = current.visited #might have to edit this function
        #         neighbour.grid = copy.deepcopy(current.grid)
        #         #we feed that instance of the class a move
        #         neighbour.solver_move(command)

        #         #we check whether that move is a valid move
        #         if neighbour.ValidSolver() and (neighbour.player.row, neighbour.player.col, neighbour.player.num_water_buckets) not in current.visited:
        #             #we will conduct the cell's function where our game state is current present
        #             neighbour.grid[neighbour.player.row][neighbour.player.col].ValidStep(neighbour)
        #             #we will update our neighbour's visited and moves list by inheriting the previous visited and move lists of the parent
        #             neighbour.visited.append((neighbour.player.row, neighbour.player.col, neighbour.player.num_water_buckets))
        #             neighbour.moves = current.moves.copy() + [command]
        #             print(neighbour.gridstr())
        #             #we will add the instances to the current parent's children
        #             current.children.append(neighbour)

        #             #we will do a check to see if we have found a solution
        #             if neighbour.grid[neighbour.player.row][neighbour.player.col].display == 'Y':
        #                 print('Path has {} moves.\nPath: {}'.format(len(neighbour.moves), ', '.join(neighbour.moves)))
        #                 return True
                    
        #             elif neighbour.grid[neighbour.player.row][neighbour.player.col].display in neighbour.teleport_disp:
        #                 neighbour.grid[neighbour.player.row][neighbour.player.col].teleport(neighbour)
        
        #     for child in current.children:
        #         queue.append(child)
            
        # print("There is no possible path.")
        # return False
        
#     elif mode == 'DFS':
#         commands = ['w', 's', 'a', 'd', 'e']

#         X = Start()
#         X.starting(game)
#         game.visited.append((game.player.row, game.player.col, game.player.num_water_buckets))
#         stack = [game]
#         while stack:
#             current = stack.pop()

#             for command in commands:

#                 neighbour = Game(filename)
#                 neighbour.player.row, neighbour.player.col, neighbour.player.num_water_buckets = current.player.row, current.player.col, current.player.num_water_buckets
#                 neighbour.grid = copy.deepcopy(current.grid)
#                 neighbour.visited = current.visited 

#                 neighbour.solver_move(command)

#                 if neighbour.ValidSolver() and (neighbour.player.row, neighbour.player.col, neighbour.player.num_water_buckets) not in current.visited:
#                     neighbour.grid[neighbour.player.row][neighbour.player.col].ValidStep(neighbour)

#                     neighbour.visited += [(neighbour.player.row, neighbour.player.col, neighbour.player.num_water_buckets)]
#                     neighbour.moves = current.moves + [command]

#                     current.children.append(neighbour)

#                     if neighbour.grid[neighbour.player.row][neighbour.player.col].display == 'Y':
#                         print('Path has {} moves.\nPath: {}'.format(len(neighbour.moves), ', '.join(neighbour.moves)))
#                         return True
                        
#                     elif neighbour.grid[neighbour.player.row][neighbour.player.col].display in neighbour.teleport_disp:
#                         neighbour.grid[neighbour.player.row][neighbour.player.col].teleport(neighbour)
            
#             for child in current.children:
#                 stack.append(child)
        
#         print("There is no possible path.")
#         return False
    
#     else:
#         print("Usage: python3 solver.py <filename> <mode>")

# try:
#     filename = sys.argv[1]
#     mode = sys.argv[2]

# except IndexError:
#     print("Usage: python3 solver.py <filename> <mode>")
#     exit()

# solve(mode, filename)