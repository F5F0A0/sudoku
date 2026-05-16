class Cell2:
    def __init__(
        self, value: int = 0, is_given: bool = False, candidates: set | None = None
    ):
        self.value = value
        self.is_given = is_given
        self.candidates = candidates if candidates is not None else set()
