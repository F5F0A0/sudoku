from cell import *
import math as math

class Sudoku():

    def __init__(self,sudoku):

        self.initial_sudoku = sudoku
        self.dimension = int(math.sqrt(len(sudoku)))
        self.rows = []
        self.columns = []
        self.cells = []
        self.solved = 0
        self.past_board_states = []

        self.init_rows()
        self.init_columns()
        self.create_cells()


    def duplicates(self, array):
        """On the first encounter with a value this function uses a
        sorted array to mark that value as seen. If it sees that number
        a second time it returns True. Otherwise it returns False.

        Works on any length array.
        """
        seen_numbers = [0]*len(array)

        for cell in array:
            if cell.value == 0:
                pass
            elif not seen_numbers[cell.value-1]:
                seen_numbers[cell.value-1] = 1
            else:
                return 1

        return 0

    def is_solved(self):
        """Checks for duplicates in all rows and columns. NEED TO
        ADD 3x3 box for 9x9 sudoku."""

        for cell in self.cells:
            if cell.value == 0:
                return False

        for row in self.rows:
            if self.duplicates(row):
                return False

        for column in self.columns:
            if self.duplicates(column):
                return False

        return True

    def update_cell(self, cell):
        """
        Updates the possible values a cell can be by checking values in
        its corrisponding row and column. NEED TO ADD 3x3 BOX for the
        9x9 sudoku.
        """
        row = self.rows[cell.row_ID]
        column = self.columns[cell.column_ID]
        for row_cell in row:
            if row_cell.value !=0:
                cell.remove_possible_value(row_cell.value)
        for column_cell in column:
            if column_cell.value != 0:
                cell.remove_possible_value(column_cell.value)

    def update_all_cells(self):
        """
        Makes a single pass through the sudoku grid. If a cell has
        a single possible value it will solve it. Otherwise it will
        try to reduce the possible values by comparing to the solved
        values in its row and column. NEED TO ADD 3x3 BOX for the
        9x9 sudoku.
        """

        for cell in self.cells:
            if cell.solved == 1:
                pass
            elif cell.is_solvable():
                cell.set_value()
            else:
                if cell.num_possible_values == 1:
                    cell.set_value()
                else:
                    self.update_cell(cell)

    def row_missing_values(self, row):

        missing_values = [1] * self.dimension

        for cell in self.cells:
            if cell.value == 0:
                pass
            else:
                missing_values[cell.value] = 0

    def create_cells(self):
        """
        Instantiates each cell in the sudoku as a class object.
        Then assigns that cell to its respective row and column.
        NEEDS TO ADD IT TO 3x3 GRID FOR 9x9 SUDOKU!
        """
        column = 0
        row = 0
        id = 0

        for value in self.initial_sudoku:

            cell = Cell(id,column,row,int(value),self.dimension)
            self.cells.append(cell)
            self.rows[row].append(cell)
            self.columns[column].append(cell)

            if column < self.dimension - 1:
                column += 1
            else:
                column = 0
                row += 1
            id += 1

    def init_rows(self):

        for i in range(0, self.dimension):
            self.rows.append([])

    def init_columns(self):

        for i in range(0, self.dimension):
            self.columns.append([])


