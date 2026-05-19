from sudoku.core.grid import Grid


class BacktrackingSolver:
    def solve(self, b: Grid) -> Grid | None:
        """Solve the grid in place with backtracking."""
        sol = b.copy_grid()
        if self._solve(sol):
            return sol
        return None

    def _solve(self, b: Grid) -> bool:
        cell = (
            b.find_first_empty_cell()
        )  # find_empty() returns None if the grid is fully solved
        if cell is None:
            return True  # the grid is solved
        for v in b.get_cell_candidates(cell.row, cell.col):
            cell.value = v
            if self._solve(b):
                return True  # found a solution
            cell.value = 0  # undo if this branch failed
        return False  # no solution
