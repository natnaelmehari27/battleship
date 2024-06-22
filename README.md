# Battleships

Battle is a Python terminal game, which runs in the Code Institiute's mock terminal on Heroku.

Players can try to beat the computer by finding the battleships hidden my the computer. Each battleship occupies one square on the board.

[Here is the live version of the project](https://battleshipss-33d29b297183.herokuapp.com/)

![all-devices-white](https://github.com/natnaelmehari27/battleship/assets/159337397/f38189d9-8544-46aa-a922-ce011ea9255d)

## How to play 

Battleships is based on the classic pen-and-paper game. you can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)). It is played on ruled grids (paper or board) on which each player's fleet of warships are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet. 

In this version, the player first enters their name and is then asked to place a row and column to hide the player's ship from the computer. the player knows where their ships are but cannot see where the computer's ships are located. Hits are indicated by ¤.

when the player sinks all of their opponenet's battleship, the player is declared victory.

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

I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there is no problems.
- Given invalid inputs: strings when numbers are excepted, out of bounds inputs
- Tested in my local terminal and the code insititute Heroku terminal.

##### Bugs 

__Remaining bugs__
- The final commit i used when i was fixing bugs according to the CI python linter, it didn't push because apparently i had opened many tabs on my pc of the same workspace and accidently tried to commit it using the old workspace but it would not push because it says i have another opened locally opened terminal.

__Validator Testing__
- PEP8
  - Errors found have been fixed from PEP8online.com. it was mostly a lot of whitespace or less of whitespace between functions
 
##### Deployment

This project was deployued using Code Institiute's mock terminal for Heroku.
- Steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildbakcs to python and Node75 in that order
  - Link the Heroku appto the repository
  - click on Deploy
 
##### Credits 
- Code institiute for the deployment terminal
- Wikipedia for the details of the battleship game
- For the project submisson course video for helping me understand more about how i can do this. 
  
  




