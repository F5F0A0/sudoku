from sudoku.core.board import Board


class BacktrackingSolver:
    def solve(self, b: Board) -> Board | None:
        """Solve the grid in place with backtracking."""
        sol = b.copy()
        if self._solve(sol):
            return sol
        return None

    def _solve(self, b: Board) -> bool:
        cell = b.find_empty()  # find_empty() returns None if the grid is fully solved
        if cell is None:
            return True  # the grid is solved
        for v in b.candidates(cell.row, cell.col):
            cell.value = v
            if self._solve(b):
                return True  # found a solution
            cell.value = 0  # undo if this branch failed
        return False  # no solution
