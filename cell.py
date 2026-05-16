class Cell():

    def __init__(self, cell_ID, column_ID, row_ID, value, sudoku_dimension):

        self.cell_ID = cell_ID
        self.column_ID = column_ID
        self.row_ID = row_ID
        self.value = value
        self.solved = False
        self.start_of_branch = False
        self.values = []
        self.previous_possible_values = {}

        if self.value != 0:
            self.solved = True
        else:
            self.solved = False

        self.sudoku_dimension = sudoku_dimension
        self.num_possible_values = sudoku_dimension
        self.possible_values = []

        if self.value == 0:
            self.possible_values = {1: True, 2: True, 3: True,
                                    4: True, 5: True, 6: True,
                                    7: True, 8: True, 9: True}

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
        return self.get_start_of_branch()

    def no_possible_values(self):

        num_possible_values = self.get_num_possible_values()

        if num_possible_values == 0:
            return True

        return False

    def solve(self, value):

        self.set_value(value)
        self.set_solved()

    def guess_lowest(self):

        possible_values = self.get_possible_values()

        for value in range(1,len(possible_values)+1):

            if possible_values[value] == True:
                self.set_value(value)
                self.set_possible_values(value, False)
                self.set_solved()

    def set_start_of_branch(self, value):
        self.start_of_branch = value

    def get_num_possible_values(self):
        return self.num_possible_values

    def set_solved(self, value=0):
        if value == 0:
            for value in self.possible_values:
                if value == True:
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

    def no_possible_values(self):
        """
        Checks if there are any possible values left
        to guess for this cell.
        """
        values = self.get_possible_values()

        for value in values:
            if values[value] == True:
                return False

        return True

    def update_solved(self, value):
        self.solved = value

    def set_possible_values(self, value, possible):
        self.possible_values[value] = possible

    def set_value(self, value):
        self.value = value

    def get_possible_values(self):
        return self.possible_values

    def get_guessed_values(self):
        return self.guessed_values

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