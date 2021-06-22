'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This tests specfic aspects of my parser file; this includes:
    • If the file is not found
    • If there is an abstract element in the board
    • If there are too many/little ends and/or starts
    • If there a teleporting pad does not have an exclusively matching pad
'''

from game_parser import (parse, read_lines)

def test_parse():
    '''This function is testing:
        • If the file is not found
        • If there is an abstract element in the board
        • If there are too many/little ends and/or starts
        • If there a teleporting pad does not have an exclusively matching pad
    
    This is neccessary to ENSURE that my algorithm CAN catch errors present in boards (non-valid boards), preventing the 
    player from playing invalid board configurations.
    '''
    try:
        parse(read_lines('board_error_unknown_elem.txt'))
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: Unknown Elem ValueError.'
        assert str(e) == 'Bad letter in configuration file: T.', 'TEST: Unknown Elem ValueError message.'

    try:
        parse(read_lines('board_error_many_starts.txt'))
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: Many Starts ValueError.'
        assert str(e) == 'Expected 1 starting position, got 5.', 'TEST: Many Starts ValueError message.'

    try:
        parse(read_lines('board_error_no_start.txt'))
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: No Starts ValueError.'
        assert str(e) == 'Expected 1 starting position, got 0.', 'TEST: No Starts ValueError message.'
    
    try:
        parse(read_lines('board_error_many_ends.txt'))
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: Many Ends ValueError.'
        assert str(e) == 'Expected 1 ending position, got 3.', 'TEST: Many Ends ValueError message.'
    
    try:
        parse(read_lines('board_error_uneven_pads.txt'))
    
    except Exception as e:
        assert type(e) == ValueError, 'TEST: Uneven Pads ValueError.'
        assert str(e) == 'Teleport pad 1 does not have an exclusively matching pad.', 'TEST: Uneven Pads ValueError message.'

def run_tests():
    test_parse()

run_tests()