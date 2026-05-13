from sudoku import *
from solving_algorithms import *

def main():

    sudoku = "1,0,0,0"
    cells = []
    column = 0
    row = 0

    solvable_sudoku = Sudoku(sudoku.split(","))
    # solvable_sudoku.solve()
    solved_sudoku = algorithm_1(solvable_sudoku)

    for row in solved_sudoku.rows:
        for cell in row:
            print(cell.value, end="")
        print("")

main()

