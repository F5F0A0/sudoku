from sudoku import *
from cell import *
import copy as copy

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

    return sudoku

def algorithm_2(sudoku, recursion = 0):
    """
    A simple recursive algorithm. First tries to solve the sudoku
    by comparing unsolved cells to solved cells and hoping that
    there is enough information to solve all the cells by looping
    through the Sudoku.

    If this algorithm gets through a loop of trying to solve all
    the cells in this manor, and the Sudoku has not progressed,
    then this alogrithm will choose the cell with the least possible
    values and guess the lowest possible value. This starts a new
    branch.

    If this alogrithm hits a cell with 0 possible value it will
    revert back to the start of the last branch and guess the next
    highest value. If all values have been guessed for that cell
    then the algorithm will go back to the branch previous to that
    one.
    """
    print("recursion layer = " + str(recursion))
    sudoku.guessed_cells = []

    while not sudoku.solved:

        sudoku.update_all_cells()

        for cell in sudoku.cells:
            cell_solved = cell.is_solved()
            if cell_solved == False:
                no_possible_values = cell.no_possible_values()
                if no_possible_values == True:
                    #print("no possible values")
                    return sudoku

        if sudoku.changed() == False:
            sudoku.print_grid()
            #print("Recursion layer: " + str(recursion) + " Guessing")
            cell = sudoku.easiest_cell()
            cell_copy = copy.deepcopy(cell)
            try:
                no_possible_values = cell.no_possible_values()
            except:
                #print("returned from recursion")
                return sudoku

            print(no_possible_values)

            while no_possible_values == False:
                cell.guess_lowest()
                possibly_solved_sudoku = algorithm_2(copy.deepcopy(sudoku), recursion + 1)
                print("returned from recursion layer" + str(recursion))
                print(possibly_solved_sudoku)
                solved = possibly_solved_sudoku.is_solved()
                if solved == True:
                    sudoku = possibly_solved_sudoku
                no_possible_values = cell.no_possible_values()
                cell.update_solved(False)



