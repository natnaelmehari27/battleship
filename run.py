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
        row_ship = [random.randint(0, size - 1)] * num_ship
        col = random.randint(0, size - num_ship)
        col_ship = list(range(col, col + num_ship))
        coords = tuple(zip(row_ship, col_ship))
    else:
        col_ship = [random.randint(0, size -1)] * num_ship
        row = random.randint(0, size - num_ship)
        row_ship = list(range(row, row + num_ship))
        coords = tuple(zip(row_ship, col_ship))
    return list(coords)

ship = set_ship(2); ship

def make_guess():
    """
    Convert all strings values into integers
    """
    row = int(input('row: ')) - 1
    col = int(input('col: ')) - 1
    return (row, col)
value = make_guess(); value

def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print("You already guessed that!\n")
        return board
    guesses.append(guess)
    if guess in ship:
        print("Bravo! You have hit my battleship.")
        board[guess[0]][guess[1]] = "¤"
        ship.remove(guess)
    else:
        print("Opps! You have missed.")
    return board

guesses = []
our_guess = make_guess()
board = update_board(our_guess, board, ship, guesses)
print_board(board)

def main():
    board = set_board(4)
    ship = set_ship(2)
    guesses = []
    while len(ship) > 0:
        board = update_board(make_guess(), board, ship, guesses)
        print_board(board)
    print('You sunk my battleship!')
    return 

main()