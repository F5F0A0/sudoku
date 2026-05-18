class Cell():

    def __init__(self, CELL_INDEX):

        self.INDEX = {"ROW":CELL_INDEX["ROW"], "COLUMNN": CELL_INDEX["COLUMN"]}
        self.candidates = {1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True}

