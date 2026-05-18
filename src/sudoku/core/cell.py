"""
Cell: a single square on a Sudoku board of any size.
 
A cell knows:
- Its position (row, col)
- The board size it belongs to (so candidates default to {1..size})
- Its current value (0 means empty)
- Whether it was part of the original puzzle (a "given")
- Its current candidate digits
"""

from dataclasses import dataclass, field


@dataclass
class Cell:
    row: int
    col: int
    size: int = 9
    value: int = 0
    is_given: bool = False
    candidates: set[int] = field(default_factory=set)

    def __post_init__(self):
        # If no candidates were provided, default to all digits valid for this size.
        if not self.candidates:
            self.candidates = set(range(1, self.size + 1))

    @property
    def is_empty(self) -> bool:
        """Return True if this cell has no value set."""
        return self.value == 0

    def set_value(self, value: int) -> None:
        """Set this cell's value. Should refuse to modify a given cell.
        Should also clear candidates once a value is set (the cell is decided).
        """
        if not 0 <= value <= self.size:
            raise ValueError(f"value {value} out of range for size {self.size}")
        if self.is_given:
            raise ValueError(f"Cell ({self.row}, {self.col}) with value {self.value} is given.")
        self.value = value
        self.candidates = set()

    def clear_self(self) -> None:
        """Reset this cell to empty. Should refuse if it's a given.
        After clearing, candidates should be restored to {1..9} (Board can
        narrow them again based on peers).
        """
        if self.is_given:
            raise ValueError(f"Cell ({self.row}, {self.col}) with value {self.value} is given.")
        self.value = 0
        self.candidates = set(range(1, self.size + 1))

    def __hash__(self) -> int:
        # Cells need to be hashable so Board.peers() can return a set of them.
        # Position uniquely identifies a cell within a board.
        return hash((self.row, self.col))
    
    def __str__(self) -> str:
        return str(self.value) if self.value else "."
