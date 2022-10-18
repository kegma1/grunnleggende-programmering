from tkinter import *

def draw_board(ctx, board):
    pass

def check_rows(board, key):
    for i in range(3):
        is_col_winning = True
        for j in range(3):
            if board[i][j] == key:
                continue
            else:
                is_col_winning = False
                break
        if is_col_winning:
            return True
        return False

def check_cols(board, key):
    for i in range(3):
        is_col_winning = True
        for j in range(3):
            if board[j][i] == key:
                continue
            else:
                is_col_winning = False
                break
        if is_col_winning:
            return True
        return False

def check_diags(board, key, dir): # dir is 1 or -1
    j = 0 if dir == 1 else -1
    is_dig_winning = True
    for i in range(3):
        if board[i][j] == key:
            j += dir
            continue
        else:
            is_dig_winning = False
            break
    if is_dig_winning:
        return True
    return False

initial_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

current_player = "X"

def main():
    window = Tk()
    window.resizable(0,0)
    window.geometry("300x400")
    draw_board(window, initial_board)
    window.mainloop()

if __name__ == "__main__":
    main()