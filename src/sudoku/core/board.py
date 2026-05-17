from sudoku.core.cell import Cell


class Board:
    def __init__(self, box_size=3):
        if not isinstance(box_size, int) or box_size < 1:
            raise ValueError(f"box_size must be a positive integer, got {box_size!r}")
        self.box_size = box_size
        self.size = box_size**2
        self.cells = [Cell() for _ in range(self.size**2)]

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def _validate_index(self, value, name):
        if not (0 <= value < self.size):
            raise IndexError(f"{name} {value} out of range [0, {self.size})")

    def _index(self, row, col):
        self._validate_index(row, "row")
        self._validate_index(col, "col")
        return row * self.size + col

    def get_cell(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.cells[self._index(row, col)]
        else:
            raise IndexError(f"Index {self._index} ({row}, {col}) out of range.")

    def set_value(self, row, col, value):
        if not (0 <= value <= self.size):
            raise ValueError(f"Value {value} out of range [0, {self.size}]")
        self.get_cell(row, col).value = value

    def get_row(self, row_index):
        self._validate_index(row_index, "row_index")
        start = row_index * self.size
        stop = start + self.size
        return self.cells[start:stop]

    def get_col(self, col_index):
        self._validate_index(col_index, "col_index")
        return self.cells[col_index :: self.size]

    def get_box(self, box_index):
        self._validate_index(box_index, "box_index")
        box_row = box_index // self.box_size
        box_col = box_index % self.box_size
        top_row = box_row * self.box_size
        top_col = box_col * self.box_size
        ret = []
        for i in range(self.box_size):
            for j in range(self.box_size):
                ret.append(self.get_cell(top_row + i, top_col + j))
        return ret
