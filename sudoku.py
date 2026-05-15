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
        self.init_rows()
        self.init_columns()
        self.create_cells()
        self.has_changed = True
        self.solvable_grid_state = True
        self.guessed_cells = []
        self.guessing = False

    def changed(self):
        """
        Used to see if the Sudoku board state has changed since
        last checked. Resets the flag to False now that it has
        been checked.
        """

        if self.has_changed == True:
            self.update_changed(False)
            return True

        return False

    def duplicates(self, array):
        """
        On the first encounter with a value this function uses a
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
        """
        Checks for duplicates in all rows and columns. NEED TO
        ADD 3x3 box for 9x9 sudoku.
        """

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

    def print_grid(self):

        for row in self.rows:

            for cell in row:
                print(cell.value, end="")
            print("")

    def update_changed(self, value):
        """
        Used to update the self.has_changed flag. There should
        be no reason this needs to be used in an algorithm. This
        is for behind the scenes bookkeeping only.
        """

        self.has_changed = value

    def update_cell(self, cell):
        """
        Updates the possible values a cell can be by checking values in
        its corrisponding row and column. NEED TO ADD 3x3 BOX for the
        9x9 sudoku.
        """
        row = self.rows[cell.get_row_ID()]
        column = self.columns[cell.get_column_ID()]

        for row_cell in row:
            if row_cell.value !=0:
                if cell.removed_possible_value(row_cell.value):
                    self.update_changed()

        for column_cell in column:
            if column_cell.value != 0:
                if cell.removed_possible_value(column_cell.value):
                    self.update_changed(True)

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
            else: self.update_cell(cell)

            if cell.no_possible_values():
                self.set_solvable_grid_state(False)

            if cell.is_solvable():
                cell.set_solved()
                self.update_changed(True)


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

    def guess_easiest_cell(self):
        """
        Looks for the unsolved cell with the least possible values.
        Uses the lowest value not yet guessed for that cell. Sets that
        cell as a start of a solving branch. If the board is shown to
        be unsolvable you can use that cell as a breakpoint when navigating
        backwards to the last solvable board state.
        """
        least_possible = 2
        found = False

        while not found:

            for row in self.rows:
                for cell in row:
                    if cell.get_num_possible_values() == least_possible:
                        cell.guess()
                        cell.set_start_of_branch(True)
                        self.set_guessing(True)
                        self.add_guessed_cell(cell)
                        self.update_changed(True)

                        return 0

            least_possible += 1

    def revert_to_last_known_solvable(self):

        guessed_cells = self.get_guessed_cells()
        index = len(guessed_cells)-1,

        for in range(index, 0, -1):
            guessed_cells[i].


    def add_guessed_cell(self, cell):
        self.guessed_cells.append(cell)

    def set_guessing(self, value):
        self.guessing = value

    def set_solvable_grid_state(self, value):
        self.solvable_grid_state = value

    def is_solvable_grid_state(self):
        return self.solvable_grid_state

    def get_guessed_cells(self):
        return self.guessed_cells

    def get_row(self, ID):
        return self.rows[ID]

    def get_column(self, ID):
        return self.column[ID]






