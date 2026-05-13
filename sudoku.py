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

    def solve(self):
        """
        A VERY naive alogorithm that checks each cell against the values
        already in its rows and columns. Remove those values from the cell
        if they have not been already. If a cell is down to one possible
        value we solve that cell.

        Loop back through if not solved. Hope.
        """

        while not self.solved:

            for cell in self.cells:
                if cell.solved == 1:
                    pass
                else:
                    if cell.num_possible_values == 1:
                        cell.set_value()
                    else:
                        self.update_cell(cell)

                if cell.is_solvable():
                    cell.set_value()

            if self.is_solved():
                self.solved = 1

        print(self.rows[0][0].value, end="")
        print(self.rows[0][1].value)
        print(self.rows[1][0].value, end="")
        print(self.rows[1][1].value)


    def update_cell(self, cell):
        """
        Updates the possible values a cell can be by check values in
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

    def row_missing_values(self, row):

        missing_values = [1] * self.dimension

        for cell in self.cells:
            if cell.value == 0:
                pass
            else:
                missing_values[cell.value] = 0

    def create_cells(self):

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


