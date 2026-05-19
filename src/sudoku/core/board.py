from math import isqrt

from sudoku.core.cell import Cell


class Board:
    """An NxN Sudoku grid composed of Cell objects.

    Supports any size N such that N = len_box_row * len_box_col, with both
    dimensions >= 2. For perfect-square N, box dimensions default to
    sqrt(N) x sqrt(N). Otherwise (e.g. 6, 12), the caller must provide
    len_box_row and len_box_col explicitly.

    Examples:
        Board([[0]*9 for _ in range(9)])                       # 9x9, 3x3 boxes
        Board(grid, len_box_row=2, len_box_col=3)                    # 6x6 with 2x3 boxes
        Board([[0]*16 for _ in range(16)], len_box_row=2, len_box_col=8)  # 16x16 with 2x8 boxes

    Attributes:
        size: the N in NxN.
        len_box_row: number of rows in each box.
        len_box_col: number of columns in each box.
        grid: 2D list of Cell objects, indexed as grid[row][col].
    """

    def __init__(
        self,
        grid: list[list[int]],
        len_box_row: int = None,
        len_box_col: int = None,
    ):
        """Build a Board from a 2D grid of integers.

        Args:
            grid: NxN list of lists of ints. A value of 0 means empty;
                non-zero values become "given" cells (puzzle clues that
                the solver must not modify).
            len_box_row, len_box_col: dimensions of each box. Pass both or
                neither. If both omitted, N must be a perfect square
                and box dimensions default to sqrt(N) x sqrt(N).

        Raises:
            ValueError: if the grid isn't square, the size isn't a perfect
                square and box dimensions weren't provided, box dimensions
                don't satisfy len_box_row * len_box_col == N, or only one of
                len_box_row / len_box_col is provided.
        """
        self.size = len(grid)

        # Determine box dimensions: derive from sqrt(size) if neither was
        # passed; otherwise require both and validate the product matches size.
        if len_box_row is None and len_box_col is None:
            root = isqrt(self.size)
            if root * root != self.size:
                raise ValueError(f"Size {self.size} is not a perfect square.")
            self.len_box_row = root
            self.len_box_col = root
        elif len_box_row is not None and len_box_col is not None:
            if len_box_row < 2 or len_box_col < 2:
                raise ValueError("len_box_row and len_box_col must each be at least 2.")
            if len_box_row * len_box_col != self.size:
                raise ValueError("len_box_row * len_box_col must equal size.")
            self.len_box_row = len_box_row
            self.len_box_col = len_box_col
        else:
            raise ValueError("Must pass both len_box_row and len_box_col, or neither.")

        # Validate row lengths before building any cells, so we don't leave
        # the Board in a half-constructed state on bad input.
        for i, row in enumerate(grid):
            if len(row) != self.size:
                raise ValueError(
                    f"Grid must have dimensions NxN. "
                    f"Got {self.size}x{len(row)} for row {i}."
                )

        # Build the 2D array of Cells. Non-zero values become givens — those
        # are the puzzle clues the solver isn't allowed to modify.
        self.grid = [[None] * self.size for _ in range(self.size)]
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                self.grid[i][j] = Cell(
                    row=i,
                    col=j,
                    value=value,
                    is_given=(value != 0),
                    size=self.size,
                )


if __name__ == "__main__":
    # 9x9
    b = Board([[0] * 9 for _ in range(9)])
    print(b.size, b.len_box_row, b.len_box_col)  # 9 3 3

    # 6x6 with 2x3 boxes
    b = Board([[0] * 6 for _ in range(6)], len_box_row=2, len_box_col=3)
    print(b.size, b.len_box_row, b.len_box_col)  # 6 2 3

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
