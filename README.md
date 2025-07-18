# Battleships

Battleships is a Python terminal game played in Code Institute's mock terminal on Heroku.

In this game, you try to find and sink a hidden battleship randomly placed on a grid by the computer. You enter guesses by typing row and column coordinates. The game includes input validation, error handling, and replayability.

[Live version of the project](https://battleshipss-33d29b297183.herokuapp.com/)

![all-devices-white](https://github.com/natnaelmehari27/battleship/assets/159337397/f38189d9-8544-46aa-a922-ce011ea9255d)

## How to play 

Battleships is based on the classic pen-and-paper game where players attempt to sink their opponent's fleet by guessing coordinate positions on a grid.

- At the start, enter your name and choose a board size (3x3 to 10x10).
- The computer will randomly hide a battleship of random length (2 to grid size).
- You guess by entering the row and column (e.g., 2 and 3).
- Hits are shown as `'¤'`, misses as `'X'`.
- When you sink the whole ship, you win!
- After the game ends, you’re asked if you want to play again.

you can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).


### Features 

#### Existing Features 

- **Custom Grid Size**: Players can choose the grid size (from 3x3 to 10x10).
- **Random Ship Placement**: Battleship is hidden randomly, with random orientation.
- **Clear Instructions**: Players are guided through each step.
- **User Input Validation**: All user inputs are validated to prevent crashes.
  
  <img width="533" alt="Skärmbild 2024-06-22 092306" src="https://github.com/natnaelmehari27/battleship/assets/159337397/acb7a725-a1b3-43fe-aea8-3abfa8ca0931">

- **Input Feedback**:
  - Error shown for out-of-range, blank, or non-numeric input.
  - Warning shown for repeated guesses.
- **Replay Functionality**: Option to play again after each game.
- **Stylized Terminal Output**: Separators (`~`), line formatting, and result banners improve UX.

  <img width="533" alt="Skärmbild 2024-06-22 093150" src="https://github.com/natnaelmehari27/battleship/assets/159337397/bbffa1b1-eb5c-4ae9-8ecb-1e77eb9f8c51">


  <img width="532" alt="Skärmbild 2024-06-22 102036" src="https://github.com/natnaelmehari27/battleship/assets/159337397/e982f3cb-c13c-42d2-bc7e-2b6fbc070ac6">

  __Future Features__

 - AI opponent that guesses against player
- Multiplayer option (pass-and-play or networked)
- Score tracker and difficulty levels
  
#### Data Model 

I decided to use a Board class model as my model. The game creates a board class to hold the player's ship and the computer's ship. The baord class stores the board size, the number of ships, the position of the ships, the guesses against that board, and the details such as the type.

##### Testing 

### ✅ Manual Testing Summary

| Feature Tested             | Input              | Expected Output                      | Actual Output          | Pass |
|---------------------------|--------------------|--------------------------------------|------------------------|------|
| Start Game - Blank Name   | `""`               | Error message                        | Error message shown    | ✅   |
| Start Game - Valid Name   | `"Nat"`           | Welcome message                      | Welcome shown          | ✅   |
| Grid Size - Invalid       | `"abc"` / `2` / `22` | Error message                        | Error shown            | ✅   |
| Guess - Valid             | `2`, `3`           | Accepted and evaluated               | Works as expected      | ✅   |
| Guess - Blank             | `""`, `""`         | Error message                        | Error shown            | ✅   |
| Guess - Out of Range      | `0`, `99`          | Error message                        | Error shown            | ✅   |
| Guess - Non-numeric       | `"a"`, `"*"`       | Error message                        | Error shown            | ✅   |
| Guess - Repeated          | Same as last guess | Warning shown                        | Warning shown          | ✅   |
| Replay - Blank or Wrong   | `""`, `"maybe"`    | Error message                        | Error shown            | ✅   |
| Replay - Valid            | `1` / `2`          | Game restarts or ends                | Works as expected      | ✅   |

  
##### Bugs 

- No known bugs at the time of final testing.
- All flake8 and PEP8 validation issues resolved.

### Resolved Bugs

- W292 (missing newline at EOF)
- Crashing on blank/invalid input
- Repeated guesses not handled
- Input outside grid bounds causing game to crash

  
__Validator Testing__
- PEP8
  - Errors found have been fixed from PEP8online.com. it was mostly a lot of whitespace or less of whitespace between functions
<img width="960" height="475" alt="pep8" src="https://github.com/user-attachments/assets/adaed5ca-601b-4d7b-bcf3-813f8ead1f87" />


 
##### Deployment

This project was deployed via Code Institute's Heroku mock terminal.

Deployment steps:

1. Fork or clone this repository.
2. Create a new Heroku app on the Heroku dashboard.
3. Set the buildpacks in this order:
   - Python
   - Node.js
4. Link the Heroku app to the GitHub repository.
5. Deploy the app through the Heroku interface.
   
##### Credits 
- Code Institute for providing the mock terminal and deployment tutorials.
- Wikipedia for background information on Battleship gameplay.
- The project submission course videos for instructions and guidance. 
  
  




