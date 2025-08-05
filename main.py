import utils
from board import Board

def select_gamemode():
    while True:
        is_bot = input("Select game mode(duo/bot)").lower()
        if is_bot == "duo":
            is_bot = False
            return is_bot
        elif is_bot == "bot":
            is_bot = True
            return is_bot
        else:
            print("Not valid!")

def get_col(turn):
    while True:
        col = input(f"{turn}, insert the column you want to fill(1-7)\n")
        if col in ['1', '2', '3', '4', '5', '6', '7']:
            col = int(col) - 1
            return col
        else:
            print("Not valid!")

if __name__ == "__main__":
    utils.clear_screen()

    is_bot = select_gamemode()
    
    board = Board()
    board.init_board()
    board.show_board()

    turn = "Player 1"

    if is_bot == False:
        while board.check_win(1) == False and board.check_win(2) == False:
            col = get_col(turn)
            if board.place(col, turn) == True:
                utils.clear_screen()
                board.show_board()
                if turn == "Player 1":
                    turn = "Player 2"
                else:
                    turn = "Player 1"
            else:
                utils.clear_screen()
                board.show_board()
                print("Invalid input!")

        if board.check_win(1) == True:
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    else:
        while board.check_win(1) == False and board.check_win(2) == False:
            if turn == "Player 1":
                col = get_col(turn)
            else:
                col = board.bot_place()
            if board.place(col, turn) == True:
                utils.clear_screen()
                board.show_board()
                if turn == "Player 1":
                    turn = "Player 2"
                else:
                    turn = "Player 1"
            else:
                utils.clear_screen()
                board.show_board()
                print("Invalid input!")

        if board.check_win(1) == True:
            print("Player 1 won!")
        else:
            print("Player Bot won!")