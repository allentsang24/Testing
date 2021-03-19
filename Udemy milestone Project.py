import random
from IPython.display import clear_output


def display_board(board):  # funtion to print board
    clear_output()

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''

    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Do you want to be X or O? ").upper()

        if not (marker == "X" or marker == "O"):
            clear_output()
            print("Sorry, input not vaild, please in put X or O")

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):

    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    player_list = ['Player 1', 'Player 2']
    first_player = player_list[random.randint(0, 1)]

    return first_player 


def space_check(board, position):

    return (board[position] == " ")


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def next_position(board):
    position = 0

    # double check the range functino
    while position not in [*range(1, 10)] or not space_check(board, position):
        position = int(input("Please input your next position: "))
    return position


def replay():

    decision = ""

    while (decision != "Y" or decision != "N"):
        decision = input("Do you want to play again? (Y or N) ").upper
        if decision == "Y":
            return True
        else:
            return False

print("Welcome to Tic Tac Toe!")

player_input()

choose_first()

