from droodbot.sudoku import *
from droodbot.solving_algorithms import *


def main():

    two_by_two_sudoku = """1,0,
                           0,0
                        """

    three_by_three_sudoku = """1,2,3,
                               0,0,0,
                               0,0,0
                            """

    nine_by_nine_sudoku = """
                          0,8,9,0,0,1,0,0,0,
                          2,0,5,9,6,0,0,0,1,
                          0,0,0,8,0,0,5,0,3,
                          0,1,0,0,0,5,0,0,0,
                          0,0,0,0,3,0,0,2,0,
                          0,0,6,0,0,4,0,0,7,
                          0,0,0,0,9,0,0,0,6,
                          0,0,3,0,0,0,0,1,0,
                          6,0,0,0,0,0,0,0,2
                          """

    cells = []
    column = 0
    row = 0

    sudoku = nine_by_nine_sudoku
    solvable_sudoku = Sudoku(sudoku.split(","))
    # solvable_sudoku.solve()
    # solved_sudoku = algorithm_1(solvable_sudoku)
    solved_sudoku = algorithm_2(solvable_sudoku)

    solved_sudoku.print_grid()


main()
