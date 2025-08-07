# FOUR-IN-A-ROW

## board.py

### `init_board() -> None`

Initializes the 6x7 grid

### `show_board() -> None`

Prints the grid

### `deter_bottom(col: int) -> int`

Determines the bottom of the columns from up to down (It would be more efficient in reverse but I'm too lazy to do that)

Returns the bottom index of column `col`

### `place(col: int, turn: string) -> bool`

Places on `col`, `1` if `turn` is equal to `Player 1`, 2 otherwise

Returns `True` if successfully placed, `False` otherwise

### `check_win(side: int, n: int) -> bool`

`side` could be either `1` for `Player 1` or `2` for `Player 2`

`n` is the win condition (so how many in a row to win)

Supports horizontal, vertical, top left to bottom right and top right to bottom left

Returns `True` if `side` is winning, `False` otherwise

### `bot_place(n: int) -> int`

Makes the decisions for the bot

If it is possible to win in the next step, it returns that step

Otherwise it returns a random column index

## main.py

Handles the main game logic

Loops until either side of the `check_win()` function returns `True`

## utils.py

### `clear_screen() -> None`

Clears the terminal screen

### `rand_int(a: int, b: int) -> int`

Returns a random integer between numbers `a` and `b` using the `random` package (inclusive)
