import utils

# Constants for readability
ROWS = 6
COLS = 7

class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    def show_board(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    print(" ", end=' ')
                else:
                    print(self.grid[i][j], end=' ')
            print()
        print('-------------\n1 2 3 4 5 6 7')
    def deter_bottom(self, col): # Determines the bottom of the columns
        tmp = 0
        i = 0
        if self.grid[0][col] != 0:
            return -1
        while tmp == 0:
            if i < ROWS:
                tmp = self.grid[i][col]
                i += 1
            else:
                return ROWS - 1
        return i-2
    def place(self, col, turn):
        if self.deter_bottom(col) == -1:
            return False
        if turn == "Player 1":
            self.grid[self.deter_bottom(col)][col] = 1
        else:
            self.grid[self.deter_bottom(col)][col] = 2
        return True
    def check_win(self, side, n):
        for row in range(ROWS): # Horizontal
            for col in range(COLS-n+1):
                for i in range(n):
                    if self.grid[row][col+i] != side:
                        break
                else:
                    return True
        for row in range(ROWS-n+1): # Vertical 
            for col in range(COLS):
                for i in range(n):
                    if self.grid[row+i][col] != side:
                        break
                else:
                    return True
        for row in range(ROWS-n+1): # Top-left to bottom-right
            for col in range(COLS-n+1):
                for i in range(n):
                    if self.grid[row+i][col+i] != side:
                        break
                else:
                    return True
        for row in range(ROWS-n+1): # Top-right to bottom-left
            for col in range(COLS-n, COLS):
                for i in range(n):
                    if self.grid[row+i][col-i] != side:
                        break
                else:
                    return True
        return False
    def bot_place(self, n):
        for i in range(COLS): # Place if possible to win in 1 step
            if self.deter_bottom(i) != -1: # Temporarily place bot's piece
                row = self.deter_bottom(i)
                self.grid[row][i] = 2
                if self.check_win(2, n):
                    self.grid[row][i] = 0
                    return i
                self.grid[row][i] = 0
        return utils.rand_int(0, 6) # Fallback to random integer