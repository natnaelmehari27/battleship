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

def get_board_size():
    """
    Prompt the user to enter the board size.
    The size must be an integer between 4 and 10 inclusive.
    """
    while True:
        size_input = input("Enter board size (integer between 4 and 10, default 4): ").strip()
        if not size_input:
            print("Using default board size of 4.")
            return 4
        try:
            size = int(size_input)
            if 4 <= size <= 10:
                return size
            else:
                print("Error: Board size must be between 4 and 10.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer between 4 and 10.")

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


def ask_play_again():
    """
    Prompt the user if they want to play again.
    Returns True if yes, False if no.
    """
    while True:
        choice = input("Would you like to play again? (1 for Yes, 2 for No): ").strip()
        if choice == "1":
            print("Starting a new game!")
            print("~" * 27)
            return True
        elif choice == "2":
            print("Thanks for playing Battleships! Goodbye!")
            print("~" * 27)
            return False
        else:
            print("Invalid input. Please enter 1 (Yes) or 2 (No).")


def play_game():
    """
    Main game loop. Initializes the board and ship,
    manages user guesses and updates until ship is sunk.
    """
    size = 4  # default board size
    board = create_board(size)
    ship_coords = place_ship(size)
    previous_guesses = set()

    while ship_coords:
        print_board(board)
        guess = prompt_guess(size)
        result = update_board_with_guess(guess, board, ship_coords, previous_guesses)

        # If repeated guess, no need to check for win since no progress
        if result is None:
            continue  # ask for another guess

    print_board(board)
    print("~" * 27)
    print("Congratulations! You sunk the battleship!")
    print("~" * 27)


def main():
    """
    Entry point of the application,
    manages game lifecycle and replay.
    """
    start_message()
    while True:
        play_game()
        if not ask_play_again():
            break


if __name__ == "__main__":
    main() 