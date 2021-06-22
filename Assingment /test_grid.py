'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This tests specfic aspects of my grid function.

Note: Most of the negative test cases are the same as our test_parser file as all error checks are done in my parser file.
'''

from grid import grid_to_string
from player import Player
from game_parser import (parse, read_lines)
from cells import Start

def test_grid():
    '''Most of the negative test cases are the same as our test_parser file as all error checks are done in my parser file. 
    However, the checks done here are to ensure that the errors are being caught before any grid to string conversions occur.'''
    #positive test case
    player = Player()
    player.row, player.col = 0, 2
    assert grid_to_string(parse(read_lines('board_simple.txt')), player) == '**A**\n*   *\n**Y**\n\nYou have 0 water buckets.\n', 'TEST: Successful print!'

    #negative test case
    try:
        grid_to_string(parse(read_lines('board_error_unknown_elem.txt')), player)
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: Unknown Elem ValueError.'
        assert str(e) == 'Bad letter in configuration file: T.', 'TEST: Unknown Elem ValueError message.'

    try:
        grid_to_string(parse(read_lines('board_error_many_starts.txt')), player)
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: Many Starts ValueError.'
        assert str(e) == 'Expected 1 starting position, got 5.', 'TEST: Many Starts ValueError message.'

    try:
        grid_to_string(parse(read_lines('board_error_no_start.txt')), player)
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: No Starts ValueError.'
        assert str(e) == 'Expected 1 starting position, got 0.', 'TEST: No Starts ValueError message.'
    
    try:
        grid_to_string(parse(read_lines('board_error_many_ends.txt')), player)
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: Many Ends ValueError.'
        assert str(e) == 'Expected 1 ending position, got 3.', 'TEST: Many Ends ValueError message.'
    
    try:
        grid_to_string(parse(read_lines('board_error_uneven_pads.txt')), player)
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: Uneven Pads ValueError.'
        assert str(e) == 'Teleport pad 1 does not have an exclusively matching pad.', 'TEST: Uneven Pads ValueError message.'

def run_tests():
    test_grid()

test_grid()