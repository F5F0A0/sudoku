from sudoku import *
from solving_algorithms import *

def main():

    two_by_two_sudoku = "1,0,0,0"
    three_by_three_sudoku = "1,2,3,0,0,0,0,0,0"

    cells = []
    column = 0
    row = 0

    solvable_sudoku = Sudoku(sudoku.split(","))
    # solvable_sudoku.solve()
    solved_sudoku = algorithm_1(solvable_sudoku)

    solved_sudoku.print_grid()

main()

