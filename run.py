import random 


def start_message():
    """
    Display the start message for the Battleships playground
    """
    print("~" * 27)
    print("WELCOME TO BATTLESHIPS\n")
    print("There is a Battleship hidden awaiting for you. Come and try to sink it!")
    print("~" * 27)
    while True:
        name = input("Please enter your name here: \n").strip()
        if name:
            print(f"Welcome, {name}!")
            print("~" * 27)
            return name
        print("Error: Name cannot be blank. Please enter your name.")

    
def set_board(size):
    """
    Create the square playground for the Battleship game
    """
    print("Hi, first start by hiding your battleship")
    return[['.' for count in range(size)] for count in range(size)]

def print_board(board):
    for b in board:
        print(*b)

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
   

def make_guess():
    """
    Convert all strings values into integers
    """
    print("~" * 27)
    row = int(input('row: ')) - 1
    col = int(input('col: ')) - 1
    return (row, col)

def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print("~" * 27)
        print("You already guessed that!")
        print("~" * 27)
        return board
    guesses.append(guess)
    if guess in ship:
        print("~" * 27)
        print("Bravo! You have hit my battleship.")
        print("~" * 27)
        board[guess[0]][guess[1]] = "¤"
        ship.remove(guess)
    else:
        print("~" * 27)
        print("Opps! You have missed.")
        print("~" * 27)
    return board

def play_again():
    """
    To ask the player if they want to play again.
    """
    print("Choose an option:\n1 - yes\n2 - no")
    while(True):
        try:
            answer = int(
                input("Play again?"))
            if(answer == 1):
                main()
                return False 
            elif (answer == 2):
                print("~" * 27)
                print("Thanks for playing!")
                print("~" * 27)
                return False
            else:
                print("Not a valid choice, choose 1 or 2.")
        except ValueError:
            print("Not an integer, please try again")

def main():
    start_message()
    board = set_board(4)
    print_board(board)
    ship = set_ship(2)
    value = make_guess(); value
    guesses = []
    while len(ship) > 0:
        board = update_board(make_guess(), board, ship, guesses)
        print_board(board)
    print("~" * 27)
    print('You sunk my battleship!')
    print("~" * 27)
    play_again()
    guesses = []
    our_guess = make_guess()
    board = update_board(our_guess, board, ship, guesses)
    print_board(board)

main()