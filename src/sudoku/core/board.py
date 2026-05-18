from math import isqrt

from sudoku.core.cell import Cell


class Board:
    def __init__(
        self, grid: list[list[int]], box_rows: int = None, box_cols: int = None
    ):
        self.size = len(grid)

        # check that the user has either passed in both box_rows and box_cols or omitted both
        # for a 6x6 sudoku with 6 boxes, box_rows = 2, box_cols = 3
        if box_rows is None and box_cols is None:
            root = isqrt(self.size)
            if root * root != self.size:
                raise ValueError(f"Size {self.size} is not a perfect square.")
            self.box_rows = root
            self.box_cols = root
        elif box_rows is not None and box_cols is not None:
            if box_rows * box_cols != self.size:
                raise ValueError("box_rows * box_cols must equal size")
            self.box_rows = box_rows
            self.box_cols = box_cols
        else:
            raise ValueError("must pass in box_rows and box_cols or omit both")

        # check that the numbers entered match the dimensions expected
        for i, row in enumerate(grid):
            if len(row) != self.size:
                raise ValueError(
                    f"Grid must have dimensions NxN. Got {self.size}x{len(row)} for row {i}."
                )
        # construct the grid and cells
        self.grid = [[None] * self.size for _ in range(self.size)]
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                self.grid[i][j] = Cell(
                    row=i, col=j, value=value, is_given=(value != 0), size=self.size
                )


if __name__ == "__main__":
    # 9x9
    b = Board([[0] * 9 for _ in range(9)])
    print(b.size, b.box_rows, b.box_cols)  # 9 3 3

    # 6x6 with 2x3 boxes
    b = Board([[0] * 6 for _ in range(6)], box_rows=2, box_cols=3)
    print(b.size, b.box_rows, b.box_cols)  # 6 2 3

    # Should raise: 6 isn't a perfect square
    try:
        Board([[0] * 6 for _ in range(6)])
    except ValueError as e:
        print("caught:", e)

    # Should raise: bad row length
    try:
        Board([[0] * 9, [0] * 8] + [[0] * 9 for _ in range(7)])
    except ValueError as e:
        print("caught:", e)
