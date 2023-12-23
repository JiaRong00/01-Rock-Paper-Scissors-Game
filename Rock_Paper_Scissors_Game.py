# This is the rock paper scissors game.
import cowsay
import sys
import pyfiglet
from RockPaperScissors_ASCII import rock, paper, scissors

#Game characters
characters={
    "cow": "Daisy",
    "dragon": "Stryker",
    "fox":"Kumi",
    "meow":"Simba",
    "pig":"Charlotte", 
    "stegosaurus":"Stanley",
    "trex":"Rex", 
    "turtle": "Flash"}
character_names=characters.values()
def character_profile():
    cowsay.cow("Hi, I am Daisy")
    cowsay.dragon("Hi, I am Stryker")
    
    cowsay.fox("Hi, I am Kumi")
    cowsay.meow("Hi, I am Simba")
    cowsay.pig("Hi, I am Charlotte")
    cowsay.stegosaurus("Hi, I am Stanley")
    cowsay.trex("Hi, I am Rex")
    cowsay.turtle("Hi, I am Flash")
    
#Match character with character function
def character_function(character, string):
    if character=="Daisy":
        cowsay.cow(string)
    elif character=="Stryker":
        cowsay.dragon(string)
    elif character=="Kumi":
        cowsay.fox(string)
    elif character=="Simba":
        cowsay.meow(string)
    elif character=="Charlotte":
        cowsay.pig(string)
    elif character=="Stanley":
        cowsay.stegosaurus(string)
    elif character=="Rex":
        cowsay.trex(string)
    elif character=="Flash":
        cowsay.turtle(string)
        

#Initiate game
print(pyfiglet.figlet_format("RockPaperScissors"))
game_continue=True
start_game=input("Type Yes if you would like to begin the game\n").strip().lower()

#define function to choose character
chosen_character=""
def select_character():
  character_profile()
  global chosen_character
  while True:
    print('''
        Character Name:      Character Avatar:
        Daisy                Cow
        Stryker              Dragon
        Kumi                 Fox
        Simba                Lion
        Charlotte            Pig
        Stanley              Stegosaurus
        Rex                  Trex
        Flash                Turtle''')
    chosen_character=input("Which character would you like to play with? Enter the character name\n").strip().title()
    if chosen_character in character_names:
        break
    else:
        chosen_character=input("You have keyed in an invalid character. Which character would you like to play with?").strip().title()
    
      
if start_game =='yes':
    select_character()
else:
        sys.exit(cowsay.cow("Do join for a game next time!"))

timesplayed=0
player_wins=0
Character_wins=0


#Define function to play game
def game():
    if start_game =='yes':
        playerchoice=int(input("Please enter:\n1 for Rock✊\n2 for Scissors✌️\n3 for Paper✋\n"))
        #while loop to prompt player to enter valid input 
        while playerchoice != 1 and playerchoice!=2 and playerchoice !=3:
            playerchoice=int(input("You have entered an invalid value. Please try again.\nPlease enter:\n1 for Rock✊\n2 for Scissors✌️\n3 for Paper✋\n"))
    #Character chooses a random choice
        import random
        choice_list=[1,2,3]
        Character_choice=random.choice(choice_list)
        global timesplayed
        timesplayed+=1
#determine who won
    choices={1:"Rock", 2:"Scissors", 3:"Paper"}
    global player_wins, Character_wins, chosen_character, characters
    print("You chose")
    match playerchoice:
        case 1:
            rock()
        case 2:
            scissors()
        case 3:
            paper()
    character_function(chosen_character, f"I choose {choices[Character_choice]}")
    if playerchoice==Character_choice:
        print("There is a tie🙌")
    elif playerchoice ==1 and Character_choice==2:
        print("You win!😁")
        player_wins+=1
    elif playerchoice ==2 and Character_choice==3:
        print("You win!😁")
        player_wins+=1
    elif playerchoice ==3 and Character_choice==1:
        print("You win!😁")
        player_wins+=1
    else:
        print("You lose!😭")
        Character_wins+=1
    print(f"You have won {player_wins} time(s) out of {timesplayed} round(s).")
    
#While loop to continue playing game
while True: 
    game()
    start_game=input("Would you like to play another round? Please enter Yes or No. If you would like to play with a different character, please enter Back\n").strip().lower()
    if start_game=="yes":
        continue
    elif start_game=="back": #Allow players to choose a different opponent and reset scores
      select_character()
      restart=input("Would you like to reset your score? Please enter Yes or No\n").strip().lower()
      if restart=="yes":
        player_wins=0
        Character_wins=0
        timesplayed=0
      start_game="yes"
    else:
        print(pyfiglet.figlet_format("GAMEOVER"))
        if player_wins>Character_wins:
            print(pyfiglet.figlet_format("You WIN"))
        elif Character_wins>player_wins:
            print(pyfiglet.figlet_format("You LOSE"))
        else:
            print(pyfiglet.figlet_format(f"You TIED with {chosen_character}"))
        character_function(chosen_character, f"Thank you for playing with {chosen_character}!")
        break



