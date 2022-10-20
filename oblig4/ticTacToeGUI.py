from tkinter import *
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

class Cell():
    def __init__(self, ctx, txt, game):
        self.button = Button(ctx, text=txt, width=10, height=5, command=lambda:self.make_move())
        self.ctx = ctx
        self.game = game

    def draw(self, x, y):
        self.button.grid(row=x, column=y, sticky="NSEW")

    def make_move(self):
        x = self.button.grid_info()['row']
        y = self.button.grid_info()['column']
        result = self.game.set_board_pice(x, y)
        if result == None:
            return
        self.button.config(text=result)
        self.game.check_game()



class Game:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.current_player = "X"

    def set_board_pice(self,x, y):
        if self.board[x][y] != " ":
            return None
        self.board[x][y] = self.current_player
        return self.current_player
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        return self.current_player

    def is_winner(self):
        return self.check_rows(self.current_player) or \
             self.check_cols(self.current_player) or \
                self.check_diags(self.current_player, 1) or \
                    self.check_diags(self.current_player, -1)

    def is_board_full(self):
        isBoardFull = True
        for row in self.board:
           for x in row:
               if x == " ":
                   isBoardFull = False
        return isBoardFull

    def check_game(self):

        if self.is_winner():
           print(f"{self.current_player} player won")
           return

        if self.is_board_full():
           print(f"Its a draw")
           return
        printBoard(self.board)
        self.switch_player()
    
    def check_rows(self, key):
        for i in range(3):
            is_col_winning = True
            for j in range(3):
                if self.board[i][j] == key:
                    continue
                else:
                    is_col_winning = False
                    break
            if is_col_winning:
                return True
        return False


    def check_cols(self, key):
        for i in range(3):
            is_col_winning = True
            for j in range(3):
                if self.board[j][i] == key:
                    continue
                else:
                    is_col_winning = False
                    break
            if is_col_winning:
                return True
        return False


    def check_diags(self, key, dir): # dir is 1 or -1
        j = 0 if dir == 1 else -1
        is_dig_winning = True
        for i in range(3):
            if self.board[i][j] == key:
                j += dir
                continue
            else:
                is_dig_winning = False
                break
        if is_dig_winning:
            return True
        return False



def main():
    window = Tk()
    window.resizable(0,0)
    window.geometry("240x350")

    grid = Frame(window)
    grid.place(height=300, width=300)
    buttons = []
    game = Game()
    for i, row in enumerate(game.board):
        for j, cell in enumerate(row):
            buttons.append((Cell(grid, cell, game), i, j))
            
    for button, x, y in buttons:
        button.draw(x, y)

    window.mainloop()


if __name__ == "__main__":
    main()
