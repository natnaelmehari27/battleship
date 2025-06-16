# Battleships

Battleships is a Python terminal game played in Code Institute's mock terminal on Heroku.

In this game, you try to find and sink a hidden battleship placed randomly by the computer on a 4x4 grid. You enter guesses for grid coordinates to try and hit the ship before it is sunk.

[Live version of the project](https://battleshipss-33d29b297183.herokuapp.com/)

![all-devices-white](https://github.com/natnaelmehari27/battleship/assets/159337397/f38189d9-8544-46aa-a922-ce011ea9255d)

## How to play 

Battleships is based on the classic pen-and-paper game where players attempt to sink their opponent's fleet by guessing coordinate positions on a grid.

In this single-player version, the computer hides a battleship of length 2 to 4 squares randomly on a 4x4 board. You enter guesses by specifying row and column numbers from 1 to 4. Hits are marked with '¤', misses with 'X', and your goal is to sink the entire battleship.

You cannot see the computer's ships, only the results of your guesses.

you can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).


### Features 

#### Existing Features 

__Random board generation__
- Ships are randomly placed on player's board.
- The player cannot see where the computer's ships are

  <img width="533" alt="Skärmbild 2024-06-22 092306" src="https://github.com/natnaelmehari27/battleship/assets/159337397/acb7a725-a1b3-43fe-aea8-3abfa8ca0931">

- Plays against the computer
- Accepts user input
- Maintains Scores

  <img width="533" alt="Skärmbild 2024-06-22 093150" src="https://github.com/natnaelmehari27/battleship/assets/159337397/bbffa1b1-eb5c-4ae9-8ecb-1e77eb9f8c51">

- Input validation and error-checking
  - You must enter numbers
  - You cannot enter the same guess twice

  <img width="532" alt="Skärmbild 2024-06-22 102036" src="https://github.com/natnaelmehari27/battleship/assets/159337397/e982f3cb-c13c-42d2-bc7e-2b6fbc070ac6">

  __Future Features__
  - Allow players to play against other players
  - Allow the computer to play with the player

#### Data Model 

I decided to use a Board class model as my model. The game creates a board class to hold the player's ship and the computer's ship. The baord class stores the board size, the number of ships, the position of the ships, the guesses against that board, and the details such as the type.

##### Testing 

- Used a PEP8 linter to fix style and formatting issues.
- Manually tested input validation by entering blank inputs, invalid characters, and out-of-range numbers to ensure the game does not crash.
- Verified repeated guesses do not affect game flow and produce proper warnings.
- Tested game functionality locally and on Code Institute's Heroku mock terminal environment.
  
##### Bugs 

__Remaining bugs__
- The final commit i used when i was fixing bugs according to the CI python linter, it didn't push because apparently i had opened many tabs on my pc of the same workspace and accidently tried to commit it using the old workspace but it would not push because it says i have another opened locally opened terminal.
- At the last minute i ruined everything i think because, i could push or pull my commits. commits on github like update READ.ME is not going to gitpod or the pitpod commit are not pushing to github. it's less than 30 mintues before submission and i don't think i have time to start another one.

__Validator Testing__
- PEP8
  - Errors found have been fixed from PEP8online.com. it was mostly a lot of whitespace or less of whitespace between functions
 
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
  
  




