import random 

def start_message():
    """"
    create the start message for the Battleships playground
    """
    print("~" * 27)
    print("WELCOME TO BATTLESHIPS\n")
    print("There is a battleship hidden awaiting for you. come and try to sink it!")
    print("~" * 27)

start_message()

def set_board(size):
    """
    Create the square playground for the Battleship game
    """
    return[['.' for count in range(size)] for count in range(size)]

set_board

def print_board(board):
    for b in board:
        print(*b)

board = set_board(4)
print_board(board)