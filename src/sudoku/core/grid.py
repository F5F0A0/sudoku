from math import isqrt

from sudoku.core.cell import Cell


class Grid:
    """An NxN Sudoku grid composed of Cell objects.

    Supports any size N such that N = box_row_size * box_col_size, with both
    dimensions >= 2. For perfect-square N, box dimensions default to
    sqrt(N) x sqrt(N). Otherwise (e.g. 6, 12), the caller must provide
    box_row_size and box_col_size explicitly.

    Examples:
        Grid([[0]*9 for _ in range(9)])                       # 9x9, 3x3 boxes
        Grid(grid, box_row_size=2, box_col_size=3)                    # 6x6 with 2x3 boxes
        Grid([[0]*16 for _ in range(16)], box_row_size=2, box_col_size=8)  # 16x16 with 2x8 boxes

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
        """Build a Grid from a 2D grid of integers.

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
        # the Grid in a half-constructed state on bad input.
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
        if not self.is_grid_valid():
            raise ValueError(
                "Initial grid violates Sudoku rules (duplicate values in row, column, or box)."
            )

    def get_cell(self, i: int, j: int) -> Cell:
        return self.grid[i][j]

    def get_row(self, i: int) -> list[Cell]:
        """Return all Cells in row i"""
        return self.grid[i]

    def get_col(self, j: int) -> list[Cell]:
        """Return all Cells in col j"""
        return [row[j] for row in self.grid]

    def get_box(self, i: int, j: int) -> list[Cell]:
        """Return all Cells in a box containing cell with index (i, j)"""
        row_start = (i // self.box_row_size) * self.box_row_size
        col_start = (j // self.box_col_size) * self.box_col_size
        row_end = row_start + self.box_row_size
        col_end = col_start + self.box_col_size
        return [
            self.grid[r][c]
            for r in range(row_start, row_end)
            for c in range(col_start, col_end)
        ]

    def get_empty_cells(self) -> list[Cell]:
        """returns list of all empty Cells"""
        return [cell for row in self.grid for cell in row if cell.is_empty]

    def find_first_empty_cell(self) -> Cell | None:
        """returns the first empty Cell in row-major order, or None if full"""
        for row in self.grid:
            for cell in row:
                if cell.is_empty:
                    return cell
        return None

    def get_all_units(self) -> list[list[Cell]]:
        """All rows, columns, and boxes of the grid as lists of Cells."""
        rows = [self.get_row(i) for i in range(self.size)]
        cols = [self.get_col(j) for j in range(self.size)]
        boxes = [
            self.get_box(r, c)
            for r in range(0, self.size, self.box_row_size)
            for c in range(0, self.size, self.box_col_size)
        ]
        return rows + cols + boxes

    def is_grid_valid(self) -> bool:
        """Return True if no row, column, or box contains a duplicate nonzero value.

        Does not check completeness; an empty grid is valid by this definition.
        """
        for unit in self.get_all_units():
            value_set = set()
            for cell in unit:
                if cell.is_empty:
                    continue
                if cell.value in value_set:
                    return False
                value_set.add(cell.value)
        return True

    def is_grid_solved(self) -> bool:
        """Return True iff the grid is fully filled and has no rule violations."""
        return self.find_first_empty_cell() is None and self.is_grid_valid()

    def get_cell_peers(self, i, j) -> set[Cell]:
        """all cells in the same row, column, or box as (i, j), excluding (i, j) itself. Set of Cells."""
        peers = set(self.get_row(i)) | set(self.get_col(j)) | set(self.get_box(i, j))
        peers.discard(self.get_cell(i, j))
        return peers

    def get_cell_candidates(self, i, j) -> set[int]:
        """digits 1..size that could legally go at (i, j). Empty set if the cell is already filled."""
        used = set(
            cell.value for cell in self.get_cell_peers(i, j) if not cell.is_empty
        )
        return set(range(1, self.size + 1)) - used

    def copy_grid(self) -> "Grid":
        """deep-enough copy that the solver can mutate without touching the original. Has one gotcha: don't share the candidates set between copies."""
        new_grid = Grid(
            grid=[[0] * self.size for _ in range(self.size)],
            box_row_size=self.box_row_size,
            box_col_size=self.box_col_size,
        )
        for i in range(self.size):
            for j in range(self.size):
                old = self.get_cell(i, j)
                new = new_grid.get_cell(i, j)
                new.value = old.value
                new.is_given = old.is_given
                new.candidates = old.candidates.copy()
        return new_grid

    def __str__(self):
        s = ""
        row_len = 0
        for i in range(self.size):
            if i % self.box_row_size == 0 and i != 0:
                s += "-" * (row_len - 1) + "\n"
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
                if i == 0 and j == self.size - 1:
                    row_len = len(s)

        s = "-" * (row_len - 1) + "\n" + s
        s += "-" * (row_len - 1)
        return s


if __name__ == "__main__":
    from sudoku.core.basic_9x9_solver import parse
    from sudoku.solver.backtracking import BacktrackingSolver

    inkala = parse(
        "8........"
        "..36....."
        ".7..9.2.."
        ".5...7..."
        "....457.."
        "...1...3."
        "..1....68"
        "..85...1."
        ".9....4.."
    )
    b = Grid(inkala)
    # for cell in b.col(1):
    #     print(cell.value)
    print(b)
    print(f"is_valid: {b.is_grid_valid()}")
    print(f"is_solved: {b.is_grid_solved()}")

    small = parse("01..............")
    b2 = Grid(small)
    print(b2)
    print(f"is_valid: {b2.is_grid_valid()}")
    print(f"is_solved: {b2.is_grid_solved()}")

    my_solver = BacktrackingSolver()
    sol = my_solver.solve(b)
    print(sol)
