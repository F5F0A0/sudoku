class Cell:
    def __init__(
        self, value: int = 0, is_given: bool = False, candidates: set[int] | None = None
    ):
        self.value = value
        self.is_given = is_given
        self.candidates = candidates if candidates is not None else set()

    def __repr__(self):
        return f"Cell(value={self.value}, given={self.given})"

    def __eq__(self, value):
        return self.value == value
