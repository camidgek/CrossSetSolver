import Board

flag = 0
rows = temp = cols = 7

gameBoard = Board.Board(rows, cols)

for row in gameBoard.board:
    print("Inputs for row: " + str(temp-rows))
    rows = rows - 1
    for cell in row:
        input_raw = input("Enter values: ")
        cell.choices = ([int(d) for d in input_raw])

while gameBoard.IsComplete() == 0:
    gameBoard.CheckCols()
    gameBoard.CheckRows()

print("Solution:")
gameBoard.PrintChoices()
print(flag)
