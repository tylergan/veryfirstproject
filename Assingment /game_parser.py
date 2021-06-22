'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This file contains functions that will read my board configuration, strip it, and then output the file as a matrix of objects.
'''

from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

cell_elements = {
    'X': Start,
    'Y': End,
    ' ': Air,
    '*': Wall,
    'F': Fire,
    'W': Water
}

def read_lines(filename):
    """Read in a file and return the contents as a list of strings.
    """
    try:
        with open(filename, 'r') as txt:
            ls = []

            finished = False
            while not finished:
                grid = txt.readline().strip()

                if grid == '':
                    finished = True

                else:
                    ls.append(grid)
    
        return ls 
    
    except FileNotFoundError:
        print('{} does not exist!'.format(filename))
        exit()
        
def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    teleport_disp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    grid = [] 
    start_count = 0 
    end_count = 0 
    visited_pads = [] 

    for row in lines:
        cell_row = []

        for game_cell in row:
            if game_cell not in cell_elements and  game_cell not in teleport_disp:
                raise ValueError('Bad letter in configuration file: {}.'.format(game_cell))

            elif game_cell == 'X':
                start_count += 1
            
            elif game_cell == 'Y':
                end_count += 1

            elif game_cell in teleport_disp:
                cell = Teleport()
                cell.display = game_cell
                cell_row.append(cell)

                #checking to see if we have already visited the matching pads
                teleport_counter = 0
                for visited in visited_pads:
                    if visited in visited_pads:
                        teleport_counter += 1
                
                #if not, we are going to search for matching teleporting pads.
                if teleport_counter != 2:
                    teleport_counter = 0

                    for searchRow in lines:
                        
                        for searchPair in searchRow:
                            if game_cell == searchPair:
                                teleport_counter += 1
                                visited_pads.append(searchPair)
                    
                    if teleport_counter != 2:
                        raise ValueError(('Teleport pad {} does not have an exclusively matching pad.'.format((game_cell))))
            
            if game_cell not in teleport_disp:
                cell = cell_elements[game_cell]()
                cell_row.append(cell)

        grid.append(cell_row)

    if start_count != 1:
        raise ValueError('Expected 1 starting position, got {}.'.format(start_count))

    elif end_count != 1:
        raise ValueError('Expected 1 ending position, got {}.'.format(end_count))

    return grid