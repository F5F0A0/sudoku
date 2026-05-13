class Cell():

    def __init__(self, cell_ID, column_ID, row_ID, value, sudoku_dimension):

        self.cell_ID = cell_ID
        self.column_ID = column_ID
        self.row_ID = row_ID
        self.value = value
        self.solved = 0

        if self.value != 0:
            self.solved = 1
        else:
            self.solved = 0

        self.sudoku_dimension = sudoku_dimension
        self.num_possible_values = sudoku_dimension
        self.possible_values = []
        if self.value == 0:
            self.possible_values = {1: True, 2: True}

    def set_value(self):
        """
        We're assuming the first possible value we find is the answer.
        This depends on the rest of the code going well, and is very dodgy.
        """

        for i in range(0,len(self.possible_values)):
            if self.possible_values[i+1] == True:
                self.value = i+1
        self.solved = 1


    def set_possible_values(self):
        """
        Gives a cell the proper range of possible values dependent on
        the size of the sudoku grid.
        """

        for i in range (0, self.sudoku_dimension):
            self.possible_values.append(i+1)

    def removed_possible_value(self, value):
        """
        Tries to remove a given value from the list of possible values
        for cell. If it succeeds it returns 1 to show a change has been
        made. Else it returns 0.
        """

        if self.possible_values[value] == True:
            self.possible_values[value] = False
            self.num_possible_values -= 1
            return 1

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

    def get_num_possible_values(self):
        return self.num_possible_values()

    def get_value_ID(self):
        return self.value

    def get_column_ID(self):
        return self.column_ID

    def get_row_ID(self):
        return self.row_ID

    def get_cell_ID(self):
        return self.cell_ID