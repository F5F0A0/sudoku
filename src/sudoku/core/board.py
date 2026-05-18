from sudoku.core.cell import Cell


class Board:
    def __init__(self, box_size=3):
        if not isinstance(box_size, int) or box_size < 1:
            raise ValueError(f"box_size must be a positive integer, got {box_size!r}")
        self.box_size = box_size
        self.size = box_size**2
        self.cells = [Cell() for _ in range(self.size**2)]

    def __str__(self):
        ret = ""
        for row in range(self.size):
            if row % self.box_size == 0:
                ret += "---------------------------------------\n"
            for col in range(self.size):
                value = str(self.get_cell(row, col).value)
                if col == 0:
                    ret += f"| {value}"
                elif col == self.size - 1:
                    ret += f" | {value} |\n"
                elif col % self.box_size == 0:
                    ret += f" || {value}"
                else:
                    ret += f" | {value}"
        ret += "---------------------------------------\n"
        return ret

    def _validate_index(self, value, name):
        if not (0 <= value < self.size):
            raise IndexError(f"{name} {value} out of range [0, {self.size})")

    def _index(self, row, col):
        self._validate_index(row, "row")
        self._validate_index(col, "col")
        return row * self.size + col

    def get_cell(self, row, col):
        return self.cells[self._index(row, col)]

    def set_cell(self, row, col, value):
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

    def _box_index(self, row, col):
        return (row // self.box_size) * self.box_size + col // self.box_size

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

    def is_cell_empty(self, row, col):
        return self.get_cell(row, col).value == 0

    def empty_cells(self):
        ret = []
        for row in range(self.size):
            for col in range(self.size):
                if self.is_cell_empty(row, col):
                    ret.append((row, col))
        return ret

    def is_valid_move(self, row, col, value):
        # return true if the value is not present
        # in its row, col, or box

        for cell in self.get_col(col):
            if cell.value == value:
                return False
        for cell in self.get_row(row):
            if cell.value == value:
                return False
        for cell in self.get_box(self._box_index(row, col)):
            if cell.value == value:
                return False
        return True

    def is_solved(self):
        return all(cell != 0 for cell in self.cells) and is_valid(grid)


if __name__ == "__main__":
    b = Board()
    print(len(b.empty_cells()))  # 81 on a fresh board
    b.set_cell(0, 0, 5)
    b.set_cell(0, 1, 3)
    print(len(b.empty_cells()))  # 79
    print(b.empty_cells()[:3])  # [(0, 2), (0, 3), (0, 4)] — first three empties
    print(b)
    print(b.is_valid_move(0, 1, 3))
    print(b.is_valid_move(0, 1, 7))
