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

    Each cell is a member of exactly one of the 9 rows, columns, and boxes.
    """
    # each cell is a member of exactly one row, column, and box
    # each cell needs to be added to the correct
    # row, column, and box that it belongs to
    # the row it gets added to corresponds to it's i, 0 to 8
    # the column it gets added to corresponds to it's j, 0 to 8
    # the box it gets added to corresponds to it's i and j,
    # box 0: 0 <= i <= 2, 0 <= j <= 2
    # box 1: 0 <= i <= 2, 3 <= j <= 5
    # box 2: 0 <= i <= 2, 6 <= j <= 8
    # box 3: 3 <= i <= 5, 0 <= j <= 2
    # box 4: 3 <= i <= 5, 3 <= j <= 5
    # box 5: 3 <= i <= 5, 6 <= j <= 8
    # box 6: 6 <= i <= 8, 0 <= j <= 2
    # box 7: 6 <= i <= 8, 3 <= j <= 5
    # box 8: 6 <= i <= 8, 6 <= j <= 8
    # to calculate which 3x3 box a cell belongs to,
    # we label the boxes:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    # and the cells are represented by (row,col) coordinates
    # ranging from (0,0) to (8,8)
    # we can represent the box labels as (i,j) coordinates themselves,
    # (0,0) (0,1) (0,2)
    # (1,0) (1,1) (1,2)
    # (2,0) (2,1) (2,2)
    # to translate the box-coordinate system back to the original
    # labels, we calculate i*3 + j
    # now to map each cell to the new set of coordinates,
    # we calculate i//3 and j//3 to sort it to the correct box
    # the formula becomes i//3 * 3 + j//3
    rows = [[] for _ in range(9)]  # create a list of 9 empty lists
    cols = [[] for _ in range(9)]  # create a list of 9 empty lists
    boxes = [[] for _ in range(9)]  # create a list of 9 empty lists
    # calculate which row, col, and box the cell belongs in
    for i in range(9):
        for j in range(9):
            rows[i].append((i, j))  # add it to the row list
            cols[j].append((i, j))  # add it to the col list
            boxes[(i // 3) * 3 + j // 3].append((i, j))  # add to the box list
    return (
        rows + cols + boxes
    )  # returns a list of lists that represent each row, column, and box,
    # for a row, column, box total of 27


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
