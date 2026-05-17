class Row():

    def __init__(self, dimension):

        cells = []*dimension

    def solved_values(self):
        """
        Returns all the solved values from all the cells
        in the row.
        """

        values = []

        for cell in self.cells:
            if cell.is_solved()
                values.append(cell.value)

        return values

    # def needed_values(self):
    #     """
    #     Returns all needed values to completely solve
    #     the row.
    #     """
    #
    #     values = []
    #     for values in range(1,self.dimension+1):
    #         values.append(value)
    #
    #     for cell in self.solved_values(self):
