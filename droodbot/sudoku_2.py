class Board():

    def __init__(self, sudoku):

        self.board = {
                        "ROW_1": {"COLUMN_1:" None, "COLUMN_2": None, "COLUMN_3":, "COLUMN_4": None, "COLUMN_5": None, "COLUMN_6": None, "COLUMN_7": None, "COLUMN_8": None, "COLUMN_9": None},
                        "ROW_2": {"COLUMN_1:" None, "COLUMN_2": None, "COLUMN_3":, "COLUMN_4": None, "COLUMN_5": None, "COLUMN_6": None, "COLUMN_7": None, "COLUMN_8": None, "COLUMN_9": None},
                        "ROW_3": {"COLUMN_1:" None, "COLUMN_2": None, "COLUMN_3":, "COLUMN_4": None, "COLUMN_5": None, "COLUMN_6": None, "COLUMN_7": None, "COLUMN_8": None, "COLUMN_9": None},
                        "ROW_4": {"COLUMN_1:" None, "COLUMN_2": None, "COLUMN_3":, "COLUMN_4": None, "COLUMN_5": None, "COLUMN_6": None, "COLUMN_7": None, "COLUMN_8": None, "COLUMN_9": None},
                        "ROW_5": {"COLUMN_1:" None, "COLUMN_2": None, "COLUMN_3":, "COLUMN_4": None, "COLUMN_5": None, "COLUMN_6": None, "COLUMN_7": None, "COLUMN_8": None, "COLUMN_9": None},
                        "ROW_6": {"COLUMN_1:" None, "COLUMN_2": None, "COLUMN_3":, "COLUMN_4": None, "COLUMN_5": None, "COLUMN_6": None, "COLUMN_7": None, "COLUMN_8": None, "COLUMN_9": None},
                        "ROW_7": {"COLUMN_1:" None, "COLUMN_2": None, "COLUMN_3":, "COLUMN_4": None, "COLUMN_5": None, "COLUMN_6": None, "COLUMN_7": None, "COLUMN_8": None, "COLUMN_9": None},
                        "ROW_8": {"COLUMN_1:" None, "COLUMN_2": None, "COLUMN_3":, "COLUMN_4": None, "COLUMN_5": None, "COLUMN_6": None, "COLUMN_7": None, "COLUMN_8": None, "COLUMN_9": None},
                        "ROW_9": {"COLUMN_1:" None, "COLUMN_2": None, "COLUMN_3":, "COLUMN_4": None, "COLUMN_5": None, "COLUMN_6": None, "COLUMN_7": None, "COLUMN_8": None, "COLUMN_9": None},
                     }

        self.boxes = {
                        "TOP_LEFT": [], "TOP_MIDDLE": [], "TOP RIGHT":[],
                        "MIDDLE_LEFT": [], "MIDDLE_MIDDLE": [], "MIDDLE_RIGHT":[],
                        "BOTTOM_LEFT": [], "BOTTOM_MIDDLE": [], "BOTTOM_RIGHT":[]
                     }

    def init_boxes(self):

        {
            self.boxes["TOP_LEFT"]      = [
                                           self.board["ROW_1"]["COLUMN_1"], self.board["ROW_1"]["COLUMN_2"], self.board["ROW_1"]["COLUMN_3"],
                                           self.board["ROW_2"]["COLUMN_1"], self.board["ROW_2"]["COLUMN_2"], self.board["ROW_2"]["COLUMN_3"],
                                           self.board["ROW_3"]["COLUMN_1"], self.board["ROW_3"]["COLUMN_2"], self.board["ROW_3"]["COLUMN_3"]
                                          ]

            self.boxes["TOP_MIDDLE"]    = [self.board["ROW_1"]["COLUMN_4"], self.board["ROW_1"]["COLUMN_5"], self.board["ROW_1"]["COLUMN_6"],
                                          [self.board["ROW_2"]["COLUMN_4"], self.board["ROW_2"]["COLUMN_5"], self.board["ROW_2"]["COLUMN_6"],
                                          [self.board["ROW_3"]["COLUMN_4"], self.board["ROW_3"]["COLUMN_5"], self.board["ROW_3"]["COLUMN_6"]
                                          ]

            self.boxes["TOP RIGHT"]     = [self.board["ROW_1"]["COLUMN_7"], self.board["ROW_1"]["COLUMN_8"], self.board["ROW_1"]["COLUMN_9"],
                                          [self.board["ROW_2"]["COLUMN_7"], self.board["ROW_2"]["COLUMN_8"], self.board["ROW_2"]["COLUMN_9"],
                                          [self.board["ROW_3"]["COLUMN_7"], self.board["ROW_3"]["COLUMN_8"], self.board["ROW_3"]["COLUMN_9"],
                                          ]

            self.boxes["MIDDLE_LEFT"]   = [self.board["ROW_4"]["COLUMN_1"], self.board["ROW_4"]["COLUMN_2"], self.board["ROW_4"]["COLUMN_3"],
                                           self.board["ROW_5"]["COLUMN_1"], self.board["ROW_5"]["COLUMN_2"], self.board["ROW_5"]["COLUMN_3"],
                                           self.board["ROW_6"]["COLUMN_1"], self.board["ROW_6"]["COLUMN_2"], self.board["ROW_6"]["COLUMN_3"],
                                          ]

            self.boxes["MIDDLE_MIDDLE"] = [self.board["ROW_4"]["COLUMN_4"], self.board["ROW_4"]["COLUMN_5"], self.board["ROW_4"]["COLUMN_6"],
                                          [self.board["ROW_5"]["COLUMN_4"], self.board["ROW_5"]["COLUMN_5"], self.board["ROW_5"]["COLUMN_6"],
                                          [self.board["ROW_6"]["COLUMN_4"], self.board["ROW_6"]["COLUMN_5"], self.board["ROW_6"]["COLUMN_6"],
                                          ]

            self.boxes["MIDDLE_RIGHT"]  = [self.board["ROW_4"]["COLUMN_7"], self.board["ROW_4"]["COLUMN_8"], self.board["ROW_4"]["COLUMN_9"],
                                          [self.board["ROW_5"]["COLUMN_7"], self.board["ROW_5"]["COLUMN_8"], self.board["ROW_5"]["COLUMN_9"],
                                          [self.board["ROW_6"]["COLUMN_7"], self.board["ROW_6"]["COLUMN_8"], self.board["ROW_6"]["COLUMN_9"],
                                          ]

            self.boxes["BOTTOM_LEFT"]   = [self.board["ROW_7"]["COLUMN_1"], self.board["ROW_7"]["COLUMN_2"], self.board["ROW_7"]["COLUMN_3"],
                                           self.board["ROW_8"]["COLUMN_1"], self.board["ROW_8"]["COLUMN_2"], self.board["ROW_8"]["COLUMN_3"],
                                           self.board["ROW_9"]["COLUMN_1"], self.board["ROW_9"]["COLUMN_2"], self.board["ROW_9"]["COLUMN_3"],
                                          ]

            self.boxes["BOTTOM_MIDDLE"] = [self.board["ROW_7"]["COLUMN_4"], self.board["ROW_7"]["COLUMN_5"], self.board["ROW_7"]["COLUMN_6"],
                                           self.board["ROW_8"]["COLUMN_4"], self.board["ROW_8"]["COLUMN_5"], self.board["ROW_8"]["COLUMN_6"],
                                           self.board["ROW_9"]["COLUMN_4"], self.board["ROW_9"]["COLUMN_5"], self.board["ROW_9"]["COLUMN_6"],
                                          ]

            self.boxes["BOTTOM_RIGHT"]  = [self.board["ROW_7"]["COLUMN_7"], self.board["ROW_7"]["COLUMN_8"], self.board["ROW_7"]["COLUMN_9"],
                                           self.board["ROW_8"]["COLUMN_7"], self.board["ROW_8"]["COLUMN_8"], self.board["ROW_8"]["COLUMN_9"],
                                           self.board["ROW_9"]["COLUMN_7"], self.board["ROW_9"]["COLUMN_8"], self.board["ROW_9"]["COLUMN_9"],
                                          ]
        }


    def solve_naked_singles(self):

        for row in self.board:
            for cell in row:
                if cell.num_candidates == 1:
                    cell.solve()

    def solve_hidden_singles(self):

        for



