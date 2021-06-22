# import sys 
# from game_parser import (parse, read_lines)

# def start(grid):
#     '''Finds the starting coordinates'''
#     i = 0
#     while i < len(grid):
#         j = 0
#         while j < len(grid[i]):
#             if grid[i][j].display == 'X':
#                 row = i
#                 col = j
#                 return row, col

#             j += 1
        
#         i += 1

# def teleport(row, col, grid):
#     i = row
#     j = col + 1 

#     while i < len(grid):
#         while j < len(grid[i]):
#             if grid[i][j].display == grid[row][col].display:
#                 row = i
#                 col = j
#                 return row, col
#             j += 1
        
#         j = 0
#         i += 1

#         if i == len(grid) - 1:
#             i = 0

# def step(row, col, move):
#     if move == 'a':
#         col -= 1
        
#     elif move == 'd':
#         col += 1

#     elif move == 'w':
#         row -= 1
        
#     elif move == 's':
#         row += 1
    
#     elif move == 'e':
#         pass
        
#     return row, col

# def valid(moves, filename):
#     '''Checks to see if the move is valid.
#     Still under development and needs more conditions (i.e. if we have visited the location already)'''
#     grid = parse(read_lines(filename))
#     row, col = start(grid)

#     num_water_buckets = 0
#     visited = []

#     for move in moves:
#         visited.append((row, col, num_water_buckets))
#         row, col = step(row, col, move)
        
#         if not (0 <= row <= len(grid) - 1) or not (0 <= col <= len(grid[row]) - 1):
#             return False
            
#         elif grid[row][col].display in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             row, col = teleport(row, col, grid)
        
#         if (row, col, num_water_buckets) in visited:
#             return False

#         elif grid[row][col].display == "*":
#             return False
            
#         elif grid[row][col].display == 'W':
#             grid[row][col].display = ' '
#             num_water_buckets += 1
                
#         elif grid[row][col].display == 'F':
#             if num_water_buckets == 0:
#                 return False
#             grid[row][col].display = ' '
#             num_water_buckets -= 1 
        
#         elif moves[-2:] == 'ee':
#             return False

#     return True

# def find_path(path, filename):
#     grid = parse(read_lines(filename))
#     row, col = start(grid)

#     for move in path:
#         row, col = step(row, col, move)

#         if grid[row][col].display in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             row, col = teleport(row, col, grid)

#     if grid[row][col].display == "Y":
#         return True

#     return False

# def string(path):
#     string = ''

#     i = 0
#     while i < len(path):
#         if i != len(path) - 1:
#             string += path[i] + ', '
        
#         else:
#             string += path[i]
        
#         i += 1
    
#     return string

# def solve(mode, filename):
#     if mode == 'BFS':
#         moves = ['a', 'd', 'w', 's', 'e']
#         queue = []
#         path = ''

#         for move in moves:
#             if valid(move, filename):
#                 queue.append(move)
        
#         while queue:
#             path = queue.pop(0)

#             for move in moves:
#                 add_in_q = path + move
#                 if valid(add_in_q, filename):
#                     queue.append(add_in_q)
            
#             if find_path(path, filename) == True:
#                 print('Path has {} moves.\nPath: {}'.format(len(path), string(path)))
#                 return True

#         print("There is no possible path.")
#         return False
    
#     elif mode == 'DFS':
#         moves = ['w', 'a', 's', 'd', 'e']
#         stack = []
#         path = ''

#         for move in moves:
#             if valid(move, filename):
#                 stack.append(move)
        
#         while stack:
#             path = stack.pop()

#             for move in moves:
#                 add_in_s = path + move
#                 if valid(add_in_s, filename):
#                     stack.append(add_in_s)
            
#             if find_path(path, filename) == True:
#                 print('Path has {} moves.\nPath: {}'.format(len(path), string(path)))
#                 return True

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
