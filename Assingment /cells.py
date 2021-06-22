'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: Store all my classes in this file which will be used to create my objects in my maze.

Note: Each Class has a solve() and a ValidStep() instance method; this is specific to my BFS/DFS algorithm.
    • solve() --> used to determine whether the move is valid.
    • ValidStep() --> used to conduct a VALID instance method within the game.
'''

class Start:
    def __init__(self):
        self.display = 'X'

    def step(self, game):
        print(game.gridstr()) #only prints the board

    def starting(self, game):
        '''Finds the starting coordinates of where the player should START in respect to X
        
        Returns:
            • Starting player coordinates
        '''

        i = 0
        while i < len(game.grid):
            j = 0
            while j < len(game.grid[i]):
                if game.grid[i][j].display == self.display: #we will update our player's coordinates to match the starting coordinates
                    game.player.row = i
                    game.player.col = j
                    break

                j += 1
        
            i += 1
    
    def solve(self, game):
        return True
    
    def ValidStep(self, game):
        pass 

class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        '''If we are able to reach this object (Y), we win the game and end the game. 
        
        Returns:
            • A congratulatory message with a history of the moves we have made and the number of moves we have made.
        '''

        print(game.gridstr())

        win_msg = '\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its' \
                  ' former glory of rainbow and sunshine! Peace reigns over the lands.'

        print(win_msg)
        if len(game.moves) == 1:
            print('\nYou made {} move.'.format(len(game.moves)))
            print('Your move: ' + ', '.join(game.moves))
        
        else:
            print('\nYou made {} moves.'.format(len(game.moves)))
            print('Your moves: ' + ', '.join(game.moves))
        
        win_disp = '\n=====================\n' \
                     '====== YOU WIN! =====\n' \
                     '====================='   

        print(win_disp)
        exit()
    
    def solve(self, game):
        return True
    
    def ValidStep(self, game):
        return True

class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        print(game.gridstr())
    
    def solve(self, game):
        return True
    
    def ValidStep(self, game):
        pass


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        '''This ensures we cannot move through walls.
        '''

        if game.moves[-1] == 'w':
            game.player.move('s')

        elif game.moves[-1] == 's':
            game.player.move('w')

        elif game.moves[-1] == 'a':
            game.player.move('d')
            
        elif game.moves[-1] == 'd':
            game.player.move('a')
        
        del game.moves[-1]

        print(game.gridstr())
        print('You walked into a wall. Oof!\n')
    
    def solve(self, game):
        return False
    
    def ValidStep(self, game):
        pass

class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        '''This will determine two things: whether you lose the game or whether you extinguish a fire.

        You may only extinguish a fire if you have one or more water buckets. Otherwise, you lose.
        '''

        if game.player.num_water_buckets == 0:
            print(game.gridstr())
            print('\nYou step into the fires and watch your dreams disappear :(.\n')

            lose_msg = 'The Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm...'\
                       ' You have been roasted.'

            print(lose_msg)

            if len(game.moves) == 1:
                print('\nYou made {} move.'.format(len(game.moves)))
                print('Your move: ' + ', '.join(game.moves))
                            
            else:
                print('\nYou made {} moves.'.format(len(game.moves)))
                print('Your moves: ' + ', '.join(game.moves))
            
            lose_disp = '\n=====================\n'\
                          '===== GAME OVER =====\n'\
                          '====================='   

            print(lose_disp)
            exit()

        game.player.num_water_buckets -= 1
        game.grid[game.player.row][game.player.col] = Air()

        print(game.gridstr())
        print('With your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!\n')
    
    def solve(self, game):
        if game.player.num_water_buckets == 0:
            return False
        return True
    
    def ValidStep(self, game):
        game.player.num_water_buckets -= 1
        game.grid[game.player.row][game.player.col] = Air()


class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        '''This will increase our player's water bucket counter by 1
        '''

        game.player.num_water_buckets += 1
        game.grid[game.player.row][game.player.col] = Air()

        print(game.gridstr())
        print("Thank the Honourable Furious Forest, you've found a bucket of water!\n")
    
    def solve(self, game):
        return True
    
    def ValidStep(self, game):
        game.player.num_water_buckets += 1
        game.grid[game.player.row][game.player.col] = Air()


class Teleport:
    def __init__(self):
        self.display = 0

    def step(self, game):
        '''An instance method that will teleport a player from a particular teleporter location to another teleporter location
        '''

        #starting indexes to conduct the "brute force" method and find the mathcing number of that pair in the matrix
        i = game.player.row 
        j = game.player.col + 1 

        while i < len(game.grid):

            while j < len(game.grid[i]):
                if game.grid[i][j].display == game.grid[game.player.row][game.player.col].display: 
                    game.player.row = i
                    game.player.col = j
                    
                    print(game.gridstr())
                    print('Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.\n')
                    
                    return (game.player.row, game.player.col)

                j += 1
            
            j = 0 #reset j to 0
            i += 1

            if i == len(game.grid) - 1: #we want to reset the coordinate to 0 to start from the top of the matrix again to search for our matching element.
                i = 0
    
    def solve(self, game):
        return True
    
    def ValidStep(self, game):
        i = game.player.row 
        j = game.player.col + 1 

        while i < len(game.grid):

            while j < len(game.grid[i]):
                if game.grid[i][j].display == game.grid[game.player.row][game.player.col].display:
                    game.player.row = i
                    game.player.col = j
                    return (game.player.row, game.player.col)

                j += 1
            
            j = 0
            i += 1

            if i == len(game.grid) - 1:
                i = 0