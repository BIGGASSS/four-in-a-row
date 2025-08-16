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
    def _check_direction(self, row, col, side, n, row_delta, col_delta):
        """Check if there are n consecutive pieces in a specific direction."""
        for i in range(n):
            new_row = row + i * row_delta
            new_col = col + i * col_delta
            if (new_row < 0 or new_row >= ROWS or
                new_col < 0 or new_col >= COLS or
                self.grid[new_row][new_col] != side):
                return False
        return True
    def check_win(self, side, n):
        """Check if the given side has n consecutive pieces in any direction."""
        # Define the four directions: horizontal, vertical, diagonal down-right, diagonal down-left
        directions = [
            (0, 1),   # Horizontal: right
            (1, 0),   # Vertical: down
            (1, 1),   # Diagonal: down-right
            (1, -1)   # Diagonal: down-left
        ]
        for row in range(ROWS):
            for col in range(COLS):
                for row_delta, col_delta in directions:
                    if self._check_direction(row, col, side, n, row_delta, col_delta):
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
