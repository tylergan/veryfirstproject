'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This tests specfic aspects of my game file; this includes:
    • Updating player coordinates
    • Updating player water buckets
    • Player interactions with fire, walls and the end object
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

def test_game():
    '''This function will test:
        • Updating player coordinates
        • Updating player water buckets
        • Player interactions with fire, walls and the end object
    
    This is necessary to ENSURE that the information regarding my game state IS being updated and stored accordingly in 
    this class. Otherwise, my game itself and my solver will not work.
    '''
    water = Water()
    fire = Fire()
    wall = Wall()
    end = End()
    game = Game('board_simple.txt')
    game.game_move('s')
    assert (game.player.row, game.player.col) == (1, 0), 'Player moves down.'
    
    game.game_move('w')
    assert (game.player.row, game.player.col) == (0, 0), 'Player moves up.'

    game.game_move('d')
    assert (game.player.row, game.player.col) == (0, 1), 'Player moves right.'

    game.game_move('a')
    assert (game.player.row, game.player.col) == (0, 0), 'Player moves left.'

    water.ValidStep(game)
    assert game.player.num_water_buckets == 1, 'Player collects one water bucket.'

    fire.ValidStep(game)
    assert game.player.num_water_buckets == 0, 'Player put out the fire with one water bucket.'

    assert fire.solve(game) == False, 'Player walks into fire without enough water buckets.'

    assert fire.solve(game) == False, 'Player walks into fire without enough water buckets.'

    assert wall.solve(game) == False, 'Player walks into a wall which is not valid.'

    assert end.solve(game) == True, 'Player reaches the finishing point.'

def run_tests():
    test_game()

run_tests()