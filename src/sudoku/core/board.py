"""
Board: an NxN Sudoku grid composed of Cell objects.
 
Supports arbitrary sizes:
  - 4x4 with 2x2 boxes
  - 9x9 with 3x3 boxes (classic)
  - 16x16 with 4x4 boxes
  - 6x6 with 2x3 boxes (rectangular)
  - 12x12 with 3x4 boxes
  - ...
 
Box dimensions default to sqrt(size) x sqrt(size). If size isn't a perfect
square (e.g. 6, 12), you must pass box_rows and box_cols explicitly.
"""

from math import sqrt
from sudoku.core.cell import Cell


class Board_Old:
    def __init__(
        self,
        size: int = 9,
        grid: list[list[int]] | None = None,
        box_rows: int | None = None,
        box_cols: int | None = None,
    ):
        """Build an NxN board of Cells.
 
        Args:
            size: the N in NxN. If grid is given, size is inferred from it
                  and this argument is ignored.
            grid: optional initial values. Non-zero values become 'givens'.
            box_rows, box_cols: box dimensions. If omitted, defaults to
                  sqrt(size) x sqrt(size); raises if size isn't a perfect square.
                  box_rows * box_cols must equal size.
        """
        # TODO:
        #   1. If grid is provided, set self.size = len(grid). Otherwise self.size = size.
        #   2. Determine box dimensions:
        #        - If box_rows and box_cols are both None:
        #            root = isqrt(self.size)
        #            if root * root != self.size: raise ValueError(...)
        #            self.box_rows = self.box_cols = root
        #        - Else (both must be provided and box_rows * box_cols == self.size):
        #            self.box_rows = box_rows
        #            self.box_cols = box_cols
        #   3. Build self.cells: an NxN list of Cell objects.
        #        - Pass size=self.size into each Cell.
        #        - If grid is provided, set value=grid[r][c] and is_given=(grid[r][c] != 0).
        if len(grid) > 0: # if grid is provided, set self.size = len(grind)
            self.size = len(grid) 
        else: 
            self.size = size
        if box_rows == None and box_cols == None:
            root = isqrt(self.size)
            if root * root != self.size: 
                raise ValueError()
            self.box_rows = box_rows
            self.box_cols = box_cols
        


    @property
    def size(self) -> int:
        # Provided so the rest of the code can refer to self.size cleanly.
        # (Will be set by __init__ above.)
        return self._size
 
    @size.setter
    def size(self, value: int) -> None:
        self._size = value
 
    # ---------- Basic accessors ----------
 
    def cell(self, r: int, c: int) -> Cell:
        """Return the Cell at (r, c)."""
        # TODO
        raise NotImplementedError
 
    def row(self, r: int) -> list[Cell]:
        """Return all cells in row r."""
        # TODO
        raise NotImplementedError
 
    def col(self, c: int) -> list[Cell]:
        """Return all cells in column c."""
        # TODO
        raise NotImplementedError
 
    def box(self, r: int, c: int) -> list[Cell]:
        """Return all cells in the box containing (r, c).
 
        Box dimensions are self.box_rows x self.box_cols.
        """
        # TODO:
        #   br = (r // self.box_rows) * self.box_rows
        #   bc = (c // self.box_cols) * self.box_cols
        #   Collect from br..br+box_rows, bc..bc+box_cols.
        raise NotImplementedError
 
    # ---------- Derived queries ----------
 
    def peers(self, r: int, c: int) -> set[Cell]:
        """All cells sharing a row, column, or box with (r, c), excluding itself."""
        # TODO: union of row, col, box; remove the cell itself.
        raise NotImplementedError
 
    def candidates(self, r: int, c: int) -> set[int]:
        """Digits 1..size that could legally go in (r, c) right now.
        Returns empty set if the cell is already filled.
        """
        # TODO:
        #   1. If cell not empty, return set().
        #   2. used = {p.value for p in peers if not p.is_empty}
        #   3. return set(range(1, self.size + 1)) - used
        raise NotImplementedError
 
    def empty_cells(self) -> list[Cell]:
        """All empty cells, in row-major order."""
        # TODO
        raise NotImplementedError
 
    # ---------- Validity ----------
    def units(self) -> list[list[Cell]]:
        """
        Return a list of the 27 sudoku units (9 rows, 9 columns, and 9 boxes). Each unit
        contains the list of lists of cells that inhabit it.
        """
        rows = [self.row(i) for i in range(self.size)]
        cols = [self.col(j) for j in range(self.size)]
        boxes = [self.box(br, bc)
                for br in range(0, self.size, self.box_rows)
                for bc in range(0, self.size, self.box_cols)]
        return rows + cols + boxes
 
    def is_valid(self) -> bool:
        """No duplicate non-zero values in any row, column, or box."""
        for unit in self.units():
            seen = set()
            for cell in unit:
                if cell.is_empty:
                    continue
                if cell.value in seen:
                    return False
                seen.add(cell.value)
        return True
 
    def is_solved(self) -> bool:
        """Every cell is filled and the board is valid."""
        return all(cell != 0 for row in self.grid for cell in row) and self.is_valid(self.grid)

 
    # ---------- Utilities ----------
 
    def copy(self) -> "Board":
        """Deep-enough copy: solvers can mutate freely."""
        # TODO:
        #   Create a new Board with the same size and box dimensions:
        #       new_board = Board(size=self.size, box_rows=self.box_rows, box_cols=self.box_cols)
        #   Then for each (r, c), copy over value, is_given, and candidates.copy().
        raise NotImplementedError
 
    def __str__(self) -> str:
        """Pretty-print with separators aligned to box dimensions.
        Empty cells appear as '.'. Cells are padded to fit the largest value.
        """
        # TODO:
        #   - cell_width = len(str(self.size))  (e.g., 1 for 9x9, 2 for 16x16)
        #   - For each row r in range(self.size):
        #       - If r > 0 and r % self.box_rows == 0: emit a horizontal separator.
        #       - Build the row as cells padded to cell_width, with "| " inserted
        #         after every box_cols columns.
        raise NotImplementedError