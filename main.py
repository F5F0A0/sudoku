from sudoku import *
from solving_algorithms import *

def main():

    two_by_two_sudoku = """1,0,
                           0,0"""

    three_by_three_sudoku = """1,2,3,
                               0,0,0,
                               0,0,0"""

    cells = []
    column = 0
    row = 0

    sudoku = three_by_three_sudoku
    solvable_sudoku = Sudoku(sudoku.split(","))
    # solvable_sudoku.solve()
    #solved_sudoku = algorithm_1(solvable_sudoku)
    solved_sudoku = algorithm_2(solvable_sudoku)

    solved_sudoku.print_grid()

main()

"""
You are in the middle of setting up the sudoku.revert_to_last_known_solvable
method.

You were tired and probably messed up the methods to set a cell as solved, and
the methods to set the value of a cell.

The recursive algorithm should work after you have a clean way to revert
to the last known solvable grid state.

9x9 after this!

3x3 boxes need to be added.

What does a sudoku larger than 9x9 actually mean?
"""