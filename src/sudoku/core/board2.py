from sudoku.core.cell2 import Cell2


class Board2:
    def __init__(self, box_size=3):
        self.box_size = box_size
        self.size = box_size**2
        self.cells = [Cell2() for _ in range(self.size**2)]

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def _index(self, row, col):
        return row * self.size + col

    def get_cell(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.cells[self._index(row, col)]
        else:
            raise IndexError("Index {self._index} ({row}, {col}) out of range.")

    def set_value(self, row, col, value):
        self.get_cell(row, col).value = value

    def get_row(self, row_index):
        start = row_index * self.size
        stop = start + self.size
        return self.cells[start:stop]

    def get_col(self, col_index):
        pass

    def get_box(self, box_index):
        pass
