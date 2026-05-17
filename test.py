if __name__ == "__main__":
    size = 9
    col_index = 0
    for i in range(0, col_index + (size - 1) * size + 1, size):
        print(i)

    for i in range(0, 9):
        print(i % 3)
