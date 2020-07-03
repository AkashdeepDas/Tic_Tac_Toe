import numpy as np
import enum


class PlayerName(enum.Enum):
    _ = 0
    X = 1
    O = 2


def create_board():
    return np.zeros((3, 3))


def grid_not_filled(board):
    return count_total_moves(board) < 9


def count_total_moves(board):
    return np.count_nonzero(board)


def player_input(board, player_name):
    try:
        x, y = map(lambda var: int(var) - 1, input("Enter Player {0}: ".format(player_name)).split(maxsplit=1))
        if board[x][y] != 0:
            print("Can't Place Move Here!")
            player_input(board, player_name)
        elif player_name == 'X':
            board[x][y] = 1
        elif player_name == 'O':
            board[x][y] = 2

    except ValueError:
        print("Can you just input two numbers, PLEASE!?")
        print("Restarting.")
        start_game()
    except IndexError:
        print("Index Out of Bounds!")
        print("Restarting.\n\n")
        start_game()


def diagonal_win(board, player):
    win = True
    for row_number in range(len(board)):
        if board[row_number][row_number] != player:
            win = False
            break
    if win:
        return win

    win = True
    for row_number in range(len(board)):
        column_number = len(board) - row_number - 1
        if board[row_number][column_number] != player:
            win = False
            break
    return win


def row_win(board, player):
    for row_number in range(len(board)):
        win = True
        for column_number in range(len(board)):
            if board[row_number][column_number] != player:
                win = False
                break
        if win:
            return win
    return False


def column_win(board, player):
    for row_number in range(len(board)):
        win = True
        for column_number in range(len(board)):
            if board[column_number][row_number] != player:
                win = False
                break
        if win:
            return win
    return False


def check_win(board, player):
    if diagonal_win(board, player) or column_win(board, player) or row_win(board, player):
        return True
    return False


def print_board(board):
    print('\n'.join(' '.join(PlayerName(x).name for x in row) for row in board))


def check_restart_game():
    choice = input("\nWanna play again? (y/n) ")
    if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
        start_game()


def start_game():
    board = create_board()
    print("\n\n\tWELCOME TO TIC TAC TOE!\n")
    print("RULES: Only input number between 1-3 and only two number at a time!")
    print("~Player X gets first move~\n")
    while True:

        for player in [1, 2]:
            player_input(board, PlayerName(player).name)
            print("Board State-")
            print_board(board)
            win = check_win(board, player)

            if win:
                print("Winner is: {0}".format(PlayerName(player).name))
                check_restart_game()
                break
            elif not grid_not_filled(board):
                print("\nDRAW!")
                check_restart_game()
                break

        if win or not grid_not_filled(board):
            break

start_game()
