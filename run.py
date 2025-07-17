import random


def start_message():
    """
    Display the start message for the Battleships playground
    """
    print("~" * 27)
    print("WELCOME TO BATTLESHIPS\n")
    print("There is a battleship hidden on the grid.")
    print("Try to sink it by guessing its coordinates!\n")
    print("Hits are shown as '¤' and misses as 'X'.")
    print("~" * 27)

    while True:
        name = input("Please enter your name here: \n").strip()
        if name:
            print(f"Welcome, {name}!")
            print("~" * 27)
            return
        print("Error: Name cannot be blank. Please enter your name.")


def get_board_size():
    """
    Prompt the user to enter the board size.
    """
    while True:
        size_input = input("Choose your grid size (3-10):").strip()
        if not size_input:
            print("Error: Grid size cannot be blank.")
            continue
        try:
            size = int(size_input)
            if 3 <= size <= 10:
                return size
            print("Please enter a number between 3 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")


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
    print("\n  " + " ".join(str(i + 1) for i in range(size)))
    for idx, row in enumerate(board, 1):
        print(f"{idx:<2} " + " ".join(row))
    print()


def place_ship(size):
    """
    Randomly place a battleship on the board either horizontally or vertically.
    """
    ship_length = random.randint(2, size)
    horizontal = random.choice([True, False])

    if horizontal:
        row = random.randint(0, size - 1)
        col_start = random.randint(0, size - ship_length)
        return [
            (row, col)
            for col in range(col_start, col_start + ship_length)
        ]
    else:
        col = random.randint(0, size - 1)
        row_start = random.randint(0, size - ship_length)
        return [
            (row, col)
            for row in range(row_start, row_start + ship_length)
        ]


def prompt_guess(size):
    """
    Prompt the user to enter a valid guess within the board range.
    """
    while True:
        try:
            print(f"Enter coordinates (1 to {size}):")
            row_input = input("Row: ").strip()
            col_input = input("Column: ").strip()

            if not row_input or not col_input:
                print("Error: Input cannot be blank. Please enter numbers.")
                continue

            row = int(row_input)
            col = int(col_input)

            if 1 <= row <= size and 1 <= col <= size:
                return row - 1, col - 1
            print(f"Error: Coordinates must be between 1 and {size}.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric integers only.")


def update_board_with_guess(guess, board, ship_coords, previous_guesses):
    """
    Update the board for the given guess.
    Marks hits with '¤' and misses with 'X'.
    Handles repeated guesses gracefully.
    """
    if guess in previous_guesses:
        print("~" * 27)
        print("You already guessed that position. Try again.")
        print("~" * 27)
        return None  # Indicate repeated guess, no changes made

    previous_guesses.add(guess)

    if guess in ship_coords:
        board[guess[0]][guess[1]] = "¤"
        ship_coords.remove(guess)
        print("~" * 27)
        print("Bravo! You hit the battleship!")
        print("~" * 27)
        return True
    else:
        board[guess[0]][guess[1]] = "X"
        print("~" * 27)
        print("Oops! You missed.")
        print("~" * 27)
        return False


def ask_play_again():
    """
    Prompt the user if they want to play again.
    Returns True if yes, False if no.
    """
    while True:
        choice = input("Play again? (1 = Yes, 2 = No): ").strip()
        if not choice:
            print("Input cannot be blank. Please enter 1 or 2.")
        elif choice == "1":
            print("\nStarting a new game...")
            print("~" * 27)
            return True
        elif choice == "2":
            print("Thanks for playing! Goodbye.")
            print("~" * 27)
            return False
        else:
            print("Invalid choice. Enter 1 for Yes or 2 for No.")


def play_game(size):
    """
    Main game loop. Initializes the board and ship,
    manages user guesses and updates until ship is sunk.
    """
    board = create_board(size)
    ship_coords = place_ship(size)
    previous_guesses = set()

    while ship_coords:
        print_board(board)
        guess = prompt_guess(size)
        result = update_board_with_guess(
            guess, board, ship_coords, previous_guesses
        )

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
        size = get_board_size()
        play_game(size)
        if not ask_play_again():
            break


if __name__ == "__main__":
    main()
