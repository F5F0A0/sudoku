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