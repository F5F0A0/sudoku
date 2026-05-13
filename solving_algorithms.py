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

        for cell in sudoku.cells:
            if cell.solved == 1:
                pass
            else:
                if cell.num_possible_values == 1:
                    cell.set_value()
                else:
                    sudoku.update_cell(cell)

            if cell.is_solvable():
                cell.set_value()

        if sudoku.is_solved():
            sudoku.solved = 1

        print(sudoku.rows[0][0].value, end="")
        print(sudoku.rows[0][1].value)
        print(sudoku.rows[1][0].value, end="")
        print(sudoku.rows[1][1].value)