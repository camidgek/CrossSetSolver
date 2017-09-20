import Cell


class Board:
    rows = 0
    cols = 0
    board = []

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.CreateBoard()

    def CreateBoard(self):
        for i in range(0, self.rows):
            self.board.append([])
            for j in range(0, self.cols):
                cell = Cell.Cell(row=i, col=j)
                self.board[i].append(cell)

    def IsComplete(self):
        for row in self.board:
            for cell in row:
                if len(cell.choices) > 1:
                    return 0
        return 1

# ROW OPERATIONS
    def CheckRows(self):
        self.CheckRowsSingle()
        self.CheckRowsOnly()

    def CheckRowsSingle(self):
        for idx, row in enumerate(self.board):
            for cell in row:
                if len(cell.choices) == 1:
                    self.RemoveFromRow(cell, cell.choices[0])

    def CheckRowsOnly(self):
        # Loop through each row
        for idx, row in enumerate(self.board):
            # Loop through each possible value
            for value in range(0, self.rows):
                temp = []
                # Check if value appears in any cell; if so, append to temp[]
                for cell in row:
                    if value in cell.choices:
                        temp.append(cell)
                # If only one cell has that value, remove all other choices
                if len(temp) == 1:
                    temp[0].choices = [value]

# COL OPERATIONS
    def CheckCols(self):
        self.CheckColsSingle()
        self.CheckColsOnly()

    def CheckColsSingle(self):
        for idx in range(0, self.cols):
            for row in self.board:
                if len(row[idx].choices) == 1:
                        self.RemoveFromCol(row[idx], row[idx].choices[0])

    def CheckColsOnly(self):
        # Loop through each column index
        for idx in range(0, self.cols):
            # Loop through each possible value
            for value in range(0, self.cols):
                temp = []
                # Check if value appears in any cell; if so, append to temp[]
                for row in self.board:
                    if value in row[idx].choices:
                        temp.append(row[idx])
                # If only one cell has that value, remove all other choices
                if len(temp) == 1:
                    temp[0].choices = [value]

# REMOVE OPERATIONS
    def RemoveFromRow(self, input_cell, value):
        for cell in self.board[input_cell.row]:
            if len(cell.choices) > 1 and cell != input_cell:
                self.RemoveChoiceFromCell(cell.row, cell.col, value)

    def RemoveFromCol(self, input_cell, value):
        for row in self.board:
            if len(row[input_cell.col].choices) > 1 and row[input_cell.col] != input_cell:
                self.RemoveChoiceFromCell(row[input_cell.col].row, row[input_cell.col].col, value)

    def RemoveChoiceFromCell(self, row, col, value):
        if value in self.board[row][col].choices:
            self.board[row][col].choices.remove(value)

# PRINT OPERATIONS
    def PrintChoices(self):
        for idx, row in enumerate(self.board):
            print("\t Row: " + str(idx))
            for cell in row:
                print(str(cell.row) + " " + str(cell.col) + ": " + str(cell.choices))