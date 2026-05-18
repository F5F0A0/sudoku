"""
BacktrackingSolver: classic recursive backtracking.

Works for any board size, because we delegate to board.candidates() to
get the legal digits at each step rather than hardcoding 1..9.

Algorithm:
  1. Find an empty cell. If none, the board is solved.
  2. For each digit in board.candidates(cell.row, cell.col):
       - Place it.
       - Recurse.
       - If recursion succeeds, return success.
       - Otherwise undo (clear the cell) and try the next digit.
  3. If no digit worked, return failure (let the caller backtrack).
"""

from sudoku.core.board import Board
from sudoku.core.cell import Cell


class BacktrackingSolver:

    def solve(self, board: Board) -> Board | None:
        """Return a solved copy of the board, or None if no solution exists.
        Does NOT mutate the input.
        """
        # TODO:
        #   1. working = board.copy()
        #   2. If self._solve(working): return working
        #   3. Else: return None
        raise NotImplementedError

    def _solve(self, board: Board) -> bool:
        """Recursive workhorse. Mutates `board` in place."""
        cell = board.find_empty()  # find_empty() returns None if the grid is fully solved
        if cell is None:
            return True  # the grid is solved
        for v in board.candidates(cell.row, cell.col):
            cell.value = v
            if self._solve(board):
                return True # found a solution
            cell.value = 0 # undo if this branch failed
        return False # no solution

    def _select_cell(self, board: Board) -> Cell | None:
        """Pick the next empty cell.

        v1: return the first empty cell.
        v2 (MRV heuristic): return the empty cell with the fewest candidates.
            Particularly impactful on larger boards (16x16, 25x25) where the
            search space explodes without good cell selection.
        """
        # TODO
        raise NotImplementedError