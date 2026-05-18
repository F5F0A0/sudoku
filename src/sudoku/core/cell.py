from dataclasses import dataclass, field


@dataclass
class Cell:
    row: int
    col: int
    value: int = 0
    is_given: bool = False
    size: int = 9
    candidates: set[int] = field(default_factory=set)

    def __post_init__(self):
        if self.value != 0:
            self.candidates = set()
        else:
            self.candidates = set(range(1, self.size + 1))

    def set_value(self, value: int) -> None:
        if self.is_given:
            raise ValueError("Cannot change the value of a given cell.")
        if 0 <= value <= self.size:
            self.value = value
            self.candidates = set(range(1, self.size + 1)) if value == 0 else set()
        else:
            raise ValueError(f"Value {value} out of range [0, {self.size}].")

    @property
    def is_empty(self) -> bool:
        return self.value == 0

    def __hash__(self) -> int:
        return hash((self.row, self.col))


if __name__ == "__main__":
    c1 = Cell(row=0, col=0)  # empty
    c2 = Cell(row=0, col=0, value=5)  # filled
    c3 = Cell(row=0, col=0, value=5, is_given=True)  # given
    print(c1.candidates)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(c2.candidates)  # set()
    print(c3.candidates)  # set()
