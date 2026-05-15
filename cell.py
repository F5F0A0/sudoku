class Cell():

    def __init__(self, cell_ID, column_ID, row_ID, value, sudoku_dimension):

        self.cell_ID = cell_ID
        self.column_ID = column_ID
        self.row_ID = row_ID
        self.value = value
        self.solved = False
        self.guessing = False
        self.start_of_branch = False
        self._values = []

        if self.value != 0:
            self.solved = True
        else:
            self.solved = False

        self.sudoku_dimension = sudoku_dimension
        self.num_possible_values = sudoku_dimension
        self.possible_values = []
        if self.value == 0:
            self.possible_values = {1: True, 2: True, 3: True}

    def set_value(self,value):
        """
        Sets the cell to the given value. This will condsider the value
        a guess. If you want to solve the cell use self.set_solve().
        """

        self.value = value
        self.guessing = True


    def set_possible_values(self):
        """
        Gives a cell the proper range of possible values dependent on
        the size of the sudoku grid.
        """

        for i in range (0, self.sudoku_dimension):
            self.possible_values.append(i+1)

    def guess(self):

        for i in range(0,len(self.possible_values)):
            if self.possible_values[i+1] == True:
                self.value = i+1

        self.set_guessing(True)

    def removed_possible_value(self, value):
        """
        Tries to remove a given value from the list of possible values
        for cell.
        """

        if self.possible_values[value] == True:
            self.possible_values[value] = False
            self.num_possible_values -= 1

        return 0

    def added_possible_value(self, value):
        """
        Tries to add a given value from the list of possible values
        for cell. If it succeeds it returns 1 to show a change has been
        made. Else it returns 0.
        """

        if self.possible_values[value] == False:
            self.possible_values[value] = True
            self.num_possible_values += 1
            return 1

    def is_solvable(self):
        if self.num_possible_values == 1:
            return 1
        else:
            return 0

    def is_start_of_branch(self):
        if self.get_start_of_branch()

    def no_possible_values(self):

        num_possible_values = self.get_num_possible_values()

        if num_possible_values == 0:
            return True

        return False

    def solve(self, value):

        self.set_value(value)
        self.set_solved()

    def unguess(self):

        if self.is_start_of_branch():
            if self.
            self.set_guessing(False)
            self.

    def set_start_of_branch(self, value):
        self.start_of_branch = value

    def set_guessing(self, value):
        self.guessing = value

    def get_num_possible_values(self):
        return self.num_possible_values

    def set_solve(self, value=0):
        if value = 0:
            for value in self.possible_values:
                if value = True:
                    self.value = value
                    self.solved = True
                    return 0
        else:
            self.value = value
            self.solved = True

    def is_solved(self):
        if self.solved():
            return True
        else:
            return False

    def get_start_of_branch(self):
        return self.start_of_branch

    def get_value_ID(self):
        return self.value

    def get_column_ID(self):
        return self.column_ID

    def get_row_ID(self):
        return self.row_ID

    def get_cell_ID(self):
        return self.cell_ID