from math import isqrt


def parse(
    s: str, box_row_size: int | None = None, box_col_size: int | None = None
) -> list[list[int]]:
    """Parse a puzzle string into a grid of ints (0 for empty). Pass in a perfect square or specify box_row_size and box_col_size."""
    size = 0
    if box_row_size is None and box_col_size is None:
        root = isqrt(len(s))
        if root * root != len(s):
            raise ValueError(
                f"Size {len(s)} is not a perfect square. Please pass in box_row_size and box_col_size."
            )
        size = root
    elif box_row_size is not None and box_col_size is not None:
        size = box_row_size * box_col_size
        if len(s) != size * size:
            raise ValueError(
                "passed in box_row_size and box_col_size do not match passed in string length"
            )
    else:
        raise ValueError("Must pass both box_row_size and box_col_size, or neither.")
    if size == 0:
        raise ValueError("size == 0")
    valid = {str(d) for d in range(size + 1)}
    valid.add(".")
    grid = []
    print(size)
    for i in range(size):
        row = []
        for j in range(size):
            index = i * size + j
            if s[index] not in valid:
                raise ValueError(f"Values must be 0-{size} or .")
            if s[index] == ".":
                row.append(0)
            else:
                row.append(int(s[index]))
        grid.append(row)
    return grid


def display(grid) -> None:
    """Print a 9x9 sudoku grid to stdout. Empty cells (value 0 or .) are left blank."""
    for i in range(9):
        if i in {0, 3, 6}:
            print("---------------------------------------")
        s = ""
        for j in range(9):
            value = str(grid[i][j])
            if value == "0":
                value = " "
            if j in {0}:
                s += "| "
                s += value
            elif j in {8}:
                s += " | "
                s += value
                s += " |"
            elif j in {3, 6}:
                s += " || "
                s += value
            else:
                s += " | "
                s += value
        print(s)
    print("---------------------------------------")

    # prints the following image:
    # print("---------------------------------------")
    # print("| x | x | x || x | x | x || x | x | x |")
    # print("| x | x | x || x | x | x || x | x | x |")
    # print("| x | x | x || x | x | x || x | x | x |")
    # print("---------------------------------------")
    # print("| x | x | x || x | x | x || x | x | x |")
    # print("| x | x | x || x | x | x || x | x | x |")
    # print("| x | x | x || x | x | x || x | x | x |")
    # print("---------------------------------------")
    # print("| x | x | x || x | x | x || x | x | x |")
    # print("| x | x | x || x | x | x || x | x | x |")
    # print("| x | x | x || x | x | x || x | x | x |")
    # print("---------------------------------------")


def is_valid(grid: list[list[int]]) -> bool:
    """Return True if no row, column, or box contains a duplicate nonzero value.

    Does not check completeness; an empty grid is valid by this definition.
    """
    for unit in units():
        value_set = set()
        for cell_coord in unit:
            i, j = cell_coord
            cell_value = grid[i][j]
            if cell_value == 0:
                continue
            if cell_value in value_set:
                return False
            value_set.add(cell_value)
    return True


def units() -> list[list[tuple[int, int]]]:
    """
    Return a list of the 27 sudoku units (9 rows, 9 columns, and 9 boxes). Each unit
    contains the list of cells that inhabit it. The cells are represented as (i,j)
    tuple coordinates.

    Each cell is a member of exactly one row, column, and box.
    """
    # create 3 empty lists that hold the 9 rows, columns, and boxes
    rows = [[] for _ in range(9)]
    cols = [[] for _ in range(9)]
    boxes = [[] for _ in range(9)]
    # for each cell, calculate which row, column, and box it belongs to
    # each cell is added to the appropriate row based on its i coordinate
    # each cell is added to the appropriate col based on its j coordinate
    # to calculate which box a cell belongs to, the formula is (i//3) * 3 + j
    # this is because we can label the boxes:
    # 0 1 2          (0,0) (0,1) (0,2)
    # 3 4 5   <==>   (1,0) (1,1) (1,2)
    # 6 7 8          (2,0) (2,1) (2,2)
    # and to map this new coordinate system on the right back to the original 0-8,
    # the formula becomes (i//3) * 3 + j
    for i in range(9):
        for j in range(9):
            rows[i].append((i, j))
            cols[j].append((i, j))
            boxes[(i // 3) * 3 + j // 3].append((i, j))
    return rows + cols + boxes


def peers() -> dict[tuple[int, int], set[tuple[int, int]]]:
    pass


def is_solved(grid: list[list[int]]) -> bool:
    """Return True iff the grid is fully filled and has no rule violations."""
    return all(cell != 0 for row in grid for cell in row) and is_valid(grid)


def find_empty(grid: list[list[int]]) -> tuple[int, int] | None:
    """
    Return the (i, j) coordinate of the first cell containing 0 or None if the grid
    is full. Iterates from left to right, top to bottom.
    """
    for i in range(9):
        for j in range(9):
            cell_value = grid[i][j]
            if cell_value == 0:
                return (i, j)
    return None


def solve(grid: list[list[int]]) -> bool:
    """
    Solve the grid in place with backtracking. Return True if solved, False if no
    solution exists.
    """

    cell = find_empty(grid)  # find_empty() returns None if the grid is fully solved
    if cell is None:
        return True  # the grid is solved
    i, j = cell  # unpack the tuple (i, j) coordinates from the returned cell
    for v in range(1, 10):
        grid[i][j] = v
        if is_valid(grid) and solve(grid):
            return True  # found a solution
        grid[i][j] = 0  # undo if this branch failed
    return False  # no solution


def main():
    import time

    easy = parse(
        "53..7...."
        "6..195..."
        ".98....6."
        "8...6...3"
        "4..8.3..1"
        "7...2...6"
        ".6....28."
        "...419..5"
        "....8..79"
    )
    inkala = parse(
        "8........"
        "..36....."
        ".7..9.2.."
        ".5...7..."
        "....457.."
        "...1...3."
        "..1....68"
        "..85...1."
        ".9....4.."
    )

    for name, puzzle in [("easy", easy), ("inkala", inkala)]:
        print(f"\n{name}:")
        display(puzzle)
        t0 = time.time()
        solved = solve(puzzle)
        elapsed = time.time() - t0
        print(f"\nSolved: {solved} in {elapsed:.3f}s")
        display(puzzle)


if __name__ == "__main__":
    main()
