from math import isqrt

from sudoku.core.cell import Cell


class Board:
    """An NxN Sudoku grid composed of Cell objects.

    Supports any size N such that N = box_row_size * box_col_size, with both
    dimensions >= 2. For perfect-square N, box dimensions default to
    sqrt(N) x sqrt(N). Otherwise (e.g. 6, 12), the caller must provide
    box_row_size and box_col_size explicitly.

    Examples:
        Board([[0]*9 for _ in range(9)])                       # 9x9, 3x3 boxes
        Board(grid, box_row_size=2, box_col_size=3)                    # 6x6 with 2x3 boxes
        Board([[0]*16 for _ in range(16)], box_row_size=2, box_col_size=8)  # 16x16 with 2x8 boxes

    Attributes:
        size: the N in NxN.
        box_row_size: number of rows in each box.
        box_col_size: number of columns in each box.
        grid: 2D list of Cell objects, indexed as grid[row][col].
    """

    def __init__(
        self,
        grid: list[list[int]],
        box_row_size: int = None,
        box_col_size: int = None,
    ):
        """Build a Board from a 2D grid of integers.

        Args:
            grid: NxN list of lists of ints. A value of 0 means empty;
                non-zero values become "given" cells (puzzle clues that
                the solver must not modify).
            box_row_size, box_col_size: dimensions of each box. Pass both or
                neither. If both omitted, N must be a perfect square
                and box dimensions default to sqrt(N) x sqrt(N).

        Raises:
            ValueError: if the grid isn't square, the size isn't a perfect
                square and box dimensions weren't provided, box dimensions
                don't satisfy box_row_size * box_col_size == N, or only one of
                box_row_size / box_col_size is provided.
        """
        self.size = len(grid)

        # Determine box dimensions: derive from sqrt(size) if neither was
        # passed; otherwise require both and validate the product matches size.
        if box_row_size is None and box_col_size is None:
            root = isqrt(self.size)
            if root * root != self.size:
                raise ValueError(f"Size {self.size} is not a perfect square.")
            self.box_row_size = root
            self.box_col_size = root
        elif box_row_size is not None and box_col_size is not None:
            if box_row_size < 2 or box_col_size < 2:
                raise ValueError(
                    "box_row_size and box_col_size must each be at least 2."
                )
            if box_row_size * box_col_size != self.size:
                raise ValueError("box_row_size * box_col_size must equal size.")
            self.box_row_size = box_row_size
            self.box_col_size = box_col_size
        else:
            raise ValueError(
                "Must pass both box_row_size and box_col_size, or neither."
            )

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

    def cell(self, i: int, j: int) -> Cell:
        return self.grid[i][j]

    def row(self, i: int) -> list[Cell]:
        """Return all cells in row i"""
        return self.grid[i]

    def col(self, j: int) -> list[Cell]:
        """Return all cells in col j"""
        return [row[j] for row in self.grid]

    def box(self, i: int, j: int) -> list[Cell]:
        """Return all cells in a box containing cell with index (i, j)"""
        row_start = (i // self.box_row_size) * self.box_row_size
        col_start = (j // self.box_col_size) * self.box_col_size
        row_end = row_start + self.box_row_size
        col_end = col_start + self.box_col_size
        return [
            self.grid[r][c]
            for r in range(row_start, row_end)
            for c in range(col_start, col_end)
        ]

    def __str__(self):
        s = ""
        for i in range(self.size):
            if i % self.box_row_size == 0:
                s += "---------------------------------------\n"
            for j in range(self.size):
                value = str(self.grid[i][j].value)
                if value == "0":
                    value = " "
                if j == 0:
                    s += f"| {value}"
                elif j == self.size - 1:
                    s += f" | {value} |\n"
                elif j % self.box_col_size == 0 and j != 0:
                    s += f" || {value}"
                else:
                    s += f" | {value}"
        s += "---------------------------------------"
        return s


if __name__ == "__main__":
    from sudoku.core.basic_9x9_solver import parse

    # inkala = parse(
    #     "8........"
    #     "..36....."
    #     ".7..9.2.."
    #     ".5...7..."
    #     "....457.."
    #     "...1...3."
    #     "..1....68"
    #     "..85...1."
    #     ".9....4.."
    # )
    # b = Board(inkala)
    # # for cell in b.col(1):
    # #     print(cell.value)
    # print(b)

    small = parse("01..............")
    b2 = Board(small)
    print(b2)
