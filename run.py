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

def set_ship(size):
    """
    Add the coordinates for the ship of the game
    """
    num_ship = random.randint(2, size)
    aim = random.randint(0, 1)
    if aim == 0:
        row_ship = [random.randint(0,size - 1)] * num_ship
        col = random.randint(0, size - num_ship)
        col_ship = list(range(col, col + num_ship))
        coords = tuple(zip(row_ship, col_ship))
    else:
        col_ship = [random.randint(0, size -1)] * num_ship
        row = random.randint(0, dims - num_ship)
        row_ship = list(range(row, row + num-ship))
    return list(coords)

ship = set_board(2); ship

def make_guess():
    """
    Convert all strings values into integers
    """
    row = int(input('row: ')) 
    col = int(input('col: '))
    return (row, col)
value = make_guess(); value