from sudoku import *
from cell import *

def algorithm_1(sudoku):
    """
    A VERY naive alogorithm that checks each cell against the values
    already in its rows and columns. Remove those values from the cell
    if they have not been already. If a cell is down to one possible
    value we solve that cell.

    Loop back through if not solved. Hope.
    """

    while not sudoku.solved:

        sudoku.update_all_cells()

        if sudoku.is_solved():
            sudoku.solved = 1

    return sudoku

def algorithm_2(sudoku):
    """
    The idea for this recursive algorithm is to use the naive algorithm until
    it hits a wall. Then this algorithm will simply find the first cell with
    two possible values and guess the lower value. If this algorithm runs into
    a cell with 0 possible values then it will revert to the last time it guessed
    a value and guess the next highest possible value.

    And then I need a way to guess
    the lower value and have it auto update that there has been a change in the
    sudoku grid.
    """

    while True:

        if sudoku.is_solvable_grid_state():
            if sudoku.changed():
                sudoku.update_all_cells()
            else:
                sudoku.guess_easiest_cell()
            if sudoku.is_solved():
                return sudoku

        else:
            sudoku.revert_to_last_known_solvable()

