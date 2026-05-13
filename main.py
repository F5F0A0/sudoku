from sudoku import *

def main():

    sudoku = "1,0,0,0"
    cells = []
    column = 0
    row = 0

    solvable_sudoku = Sudoku(sudoku.split(","))
    solvable_sudoku.solve()

main()

