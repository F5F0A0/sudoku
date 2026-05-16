class Board2:
    def __init__(self, puzzle, box_size=3):
        self.box_size = box_size
        self.size = box_size ** 2
        this.puzzle = puzzle
        self.board = []

    def _index(row, col):
        return row * self.size + col
    
    def get(row, col):
        return self.board[_index(row,col)]

    def set(row, col, value):
        self.board[_index(row,col)] = value

    def get_row(row_index):
        start = row_index * 9
        stop = start + 8
        return self.board[start:stop]

    def get_col(col_index):
        pass

    def get_box(box_index):
        pass
