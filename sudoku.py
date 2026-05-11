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


def is_valid(grid) -> bool:
    pass


def main():
    myString = "8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4.."
    print(len(myString))
    myGrid = parse(myString)
    print(myGrid)
    print(len(myGrid))
    print(len(myGrid[0]))
    display(myGrid)


main()
