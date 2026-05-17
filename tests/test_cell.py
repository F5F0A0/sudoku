from sudoku.core.cell import Cell


def test_default_cell_value_zero():
    c = Cell()
    assert c.value == 0


def test_default_cell_is_given_false():
    c = Cell()
    assert c.is_given is False


def test_default_cell_candidates_empty_set():
    c = Cell()
    assert c.candidates == set()
