def parse(s: str) -> list[list[int]]:
    if len(s) != 81:
        raise ValueError("Input length must be 81")
    valid = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
    rows, cols = 9, 9
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            index = i * 9 + j
            if s[index] not in valid:
                raise ValueError("Values must be 0-9 or .")
            if s[index] == ".":
                row.append(0)
            else:
                row.append(int(s[index]))
        grid.append(row)
    return grid


def display(grid) -> None:
    # need a dim check?
    # if len(grid) != 9:
    #     return ValueError("Grid must be 9x9")
    # for row in grid:
    #     if len(row) != 9:
    #         return ValueError("Grid must be 9x9")

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

    pass


def units() -> list[list[tuple[int, int]]]:
    """Return a list of the 27 sudoku units (rows, columns, and boxes). Each
    unit contains the list of cells that inhabit it. The cells are represented as (i,j)
    tuple coordinates.

    Each cell is a member of exactly one rows, column, and box.
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
    # 0 1 2
    # 3 4 5
    # 6 7 8
    # or,
    # (0,0) (0,1) (0,2)
    # (1,0) (1,1) (1,2)
    # (2,0) (2,1) (2,2)
    # and to map this new coordinate system back to the original 0-8,
    # the formula becomes (i//3) * 3 + j
    for i in range(9):
        for j in range(9):
            rows[i].append((i, j))
            cols[j].append((i, j))
            boxes[(i // 3) * 3 + j // 3].append((i, j))
    return rows + cols + boxes


def peers() -> dict[tuple[int, int], set[tuple[int, int]]]:
    pass


def main():
    myString = "8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4.."
    print(len(myString))
    myGrid = parse(myString)
    print(myGrid)
    print(len(myGrid))
    print(len(myGrid[0]))
    display(myGrid)
    # units()
    rows = [[] for _ in range(9)]
    print(len(rows))
    for i in range(9):
        print(i)
    units()


main()
