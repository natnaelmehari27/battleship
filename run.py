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


def create_board(size):
    """
    Create a size x size board initialized with '.' indicating empty water.
    """
    return [["." for _ in range(size)] for _ in range(size)]


def print_board(board):
    """
    Display the board with row and column numbers for user reference.
    """
    size = len(board)
    # Print column headers
    print("   " + " ".join(str(i + 1) for i in range(size)))
    for idx, row in enumerate(board, 1):
        print(f"{idx:<2} " + " ".join(row))


def place_ship(size):
    """
    Randomly place a battleship on the board either horizontally or vertically.
    Ship length ranges from 2 up to board size.
    Returns the list of coordinate tuples representing the ship positions.
    """
    ship_length = random.randint(2, size)
    horizontal = random.choice([True, False])
    if horizontal:
        row = random.randint(0, size - 1)
        col_start = random.randint(0, size - ship_length)
        ship_coords = [(row, col) for col in range(col_start, col_start + ship_length)]
    else:
        col = random.randint(0, size - 1)
        row_start = random.randint(0, size - ship_length)
        ship_coords = [(row, col) for row in range(row_start, row_start + ship_length)]
    return ship_coords


def prompt_guess(size):
    """
    Prompt the user to enter a valid guess within the board range.
    Returns zero-based (row, col) tuple.
    """
    while True:
        try:
            print(f"Enter your guess coordinates (row and column) between 1 and {size}.")
            row_input = input("Row: ").strip()
            col_input = input("Column: ").strip()
            if not row_input or not col_input:
                print("Error: Input cannot be blank. Please enter numbers.")
                continue
            row = int(row_input)
            col = int(col_input)
            if 1 <= row <= size and 1 <= col <= size:
                return row - 1, col - 1
            print(f"Error: Coordinates out of bounds. Please enter numbers 1 to {size}.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric integers only.")


def update_board_with_guess(guess, board, ship_coords, previous_guesses):
    """
    Update the board for the given guess.
    Marks hits with '¤' and misses with 'X'.
    Handles repeated guesses gracefully.
    Returns True if hit (and ship coordinate removed), False if miss or repeated.
    """
    if guess in previous_guesses:
        print("~" * 27)
        print("You already guessed that position. Try again.")
        print("~" * 27)
        return None  # Indicate repeated guess, no changes made
    previous_guesses.add(guess)

    if guess in ship_coords:
        print("~" * 27)
        print("Bravo! You hit the battleship!")
        print("~" * 27)
        board[guess[0]][guess[1]] = "¤"
        ship_coords.remove(guess)
        return True
    else:
        print("~" * 27)
        print("Oops! You missed.")
        print("~" * 27)
        board[guess[0]][guess[1]] = "X"
        return False


def play_game():
    # ...
    previous_guesses = set()









