def printBoard(board):
    print(f'''
    -------------
    | {board[0][0]} | {board[0][1]} | {board[0][2]} |
    -------------
    | {board[1][0]} | {board[1][1]} | {board[1][2]} |
    -------------
    | {board[2][0]} | {board[2][1]} | {board[2][2]} |
    -------------
    ''')

def checkRows(board, key):
    for i in range(3):
        isColWinning = True
        for j in range(3):
            if board[i][j] == key:
                continue
            else:
                isColWinning = False
                break
        if isColWinning:
            return True
    return False

def checkCols(board, key):
    for i in range(3):
        isColWinning = True
        for j in range(3):
            if board[j][i] == key:
                continue
            else:
                isColWinning = False
                break
        if isColWinning:
            return True
    return False
        
def checkDiags(board, key, dir): # dir is 1 or -1
    j = 0 if dir == 1 else -1
    isDigWinning = True
    for i in range(3):
        if board[i][j] == key:
            j += dir
            continue
        else:
            isDigWinning = False
            break
    if isDigWinning:
        return True
    return False
    
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

currentPlayer = "X"

while True:
    printBoard(board)
    row = int(input(f"Enter a row for player {currentPlayer}: "))
    col = int(input(f"Enter a column for player {currentPlayer}: "))

    if board[row][col] != " ":
        continue
    board[row][col] = currentPlayer

    isWinner = checkRows(board, currentPlayer) or \
        checkCols(board, currentPlayer) or \
            checkDiags(board, currentPlayer, 1) or \
                checkDiags(board, currentPlayer, -1)
 
    if isWinner:
        printBoard(board)
        print(f"{currentPlayer} player won")
        break
 
    isBoardFull = True
    for row in board:
        for x in row:
            if x == " ":
                isBoardFull = False
    if isBoardFull:
        printBoard(board)
        print(f"Its a draw")
        break
 
    currentPlayer = "O" if currentPlayer == "X" else "X"