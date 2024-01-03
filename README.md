# Python_Game01
A rock paper scissors game created to learn and practice python. In this game, players can choose a computer character that they would like to play the game with and play multiple rounds of the game. The choices of both the player and character will be shown for each round and the game winning statistics will be be displayed. Players have the choice of changing the character they will be playing against after each round and the scores can be reset if they wish to. 

This project consists of 2 versions of code:
1) Rock_Paper_Scissors_Game.py (Original version, refer to description above)
2) Pygame_RockPaperScissors.py (Created using pygame, based on the first version. Players can rechoose their opponents by clicking on the back button and reset the scores by clicking on reset button. However, scores are automatically reset if characters are changed.) 

The orginal version consists of 2 files:
1) Rock_Paper_Scissors_Game.py which consists of the main game code
2) RockPaperScissors_ASCII.py which contains the rock, paper, scissors ASCII art

The Pygame version consists of:
1) Pygame_RockPaperScissors.py
2) font folder
3) graphics folder

Brief details on the orginal version:
Additional features included to personalise this game:
1) Use of ASCII art for game aesthetics 
2) Use of cowsay package animals as game characters. Users can choose which game character they would like to play with
3) Use of emoji

My train of thought while creating the game flow:
1) To create a list of characters that players can choose to play with, using the cowsay package
2) To display ASCII art to initiate the game.
3) To enable users to choose if they would like to play the game and which character they would like to play with
4) To get input from the users on their choice of rock, paper or scissors
5) To generate a random choice for the character
6) To display the choices of both player and character
7) To determine and let player know who won the round
8) To allow players to continue playing if they wish to.
9) To allow players to change their opponent and reset the scores.
10) To print out overall game statistics at the end of the game.

Screenshots of the game:

<img width="427" alt="image" src="https://github.com/JiaRong00/01-Rock-Paper-Scissors-Game/assets/149306287/2a8d9e86-6ca3-4157-ae6a-a22717b7595e">
<img width="806" alt="image" src="https://github.com/JiaRong00/01-Rock-Paper-Scissors-Game/assets/149306287/8dc684d2-d0cc-4327-95eb-281f64334810">
<img width="324" alt="image" src="https://github.com/JiaRong00/01-Rock-Paper-Scissors-Game/assets/149306287/46504862-f72a-4fab-9771-f94b5ddf5618">

The code makes use of:
1) IF statements
2) While loop (continue & break)
3) Defining functions (gloabl & local scope)
4) Match-case statements
5) Dictionaries
6) Random
7) input function
8) f-string
9) sys.exit()
10) ASCII art
11) cowsay package
12) Try and Except

Screenshots for pygame version:

<img width="450" alt="image" src="https://github.com/JiaRong00/01-Rock-Paper-Scissors-Game/assets/149306287/2277a1f2-8b40-4d3c-89d2-97f8b39a66cd">
<img width="446" alt="image" src="https://github.com/JiaRong00/01-Rock-Paper-Scissors-Game/assets/149306287/448c0bed-3cb9-4e47-9fac-c3af8739421f">

