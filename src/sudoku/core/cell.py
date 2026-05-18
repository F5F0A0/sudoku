"""
A Cell in Sudoku.
"""

from dataclasses import dataclass, field


@dataclass
class Cell:
    row: int
    col: int
    value: int = 0
    is_given: bool = False
    size: int = 9
    candidates: set[int] = field(default_factory=set())

    def __post_init__(self):
        if not self.candidates:
            self.candidates = set(range(1, self.size + 1))
