# This is the rock paper scissors game.
import cowsay
import sys
import pyfiglet

#Initiate game
print(pyfiglet.figlet_format("RockPaperScissors"))
game_continue=True
cowsay.cow("Hello, I am Daisy, your game buddy!")
start_game=input("Type Yes if you would like to begin the game\n").lower()
timesplayed=0
player_wins=0
Daisy_wins=0

#Define function to play game
def game():
    if start_game =='yes':
        playerchoice=int(input("Please enter:\n1 for Rock✊\n2 for Scissors✌️\n3 for Paper✋\n"))
        #while loop to prompt player to enter valid input 
        while playerchoice != 1 and playerchoice!=2 and playerchoice !=3:
            playerchoice=int(input("You have entered an invalid value. Please try again.\nPlease enter:\n1 for Rock✊\n2 for Scissors✌️\n3 for Paper✋\n"))
    #Daisy chooses a random choice
        import random
        choice_list=[1,2,3]
        Daisy_choice=random.choice(choice_list)
        global timesplayed
        timesplayed+=1
    else:
        sys.exit(cowsay.cow("Come and play with Daisy next time!"))
#Determinining who won. 
# Rock (1) wins scissors (2) but lose to paper (3)
# Scissors (2) wins paper (3)
    choices={1:"Rock", 2:"Scissors", 3:"Paper"}
    global player_wins
    print(f"You chose {choices[playerchoice]}\nDaisy chose {choices[Daisy_choice]}")
    if playerchoice==Daisy_choice:
        print("There is a tie🙌")
    elif playerchoice ==1 and Daisy_choice==2:
        print("You win!😁")
        player_wins+=1
    elif playerchoice ==2 and Daisy_choice==3:
        print("You win!😁")
        player_wins+=1
    elif playerchoice ==3 and Daisy_choice==1:
        print("You win!😁")
        player_wins+=1
    else:
        print("You lose!😭")
        Daisy_wins+=1
    print(f"You have won {player_wins} time(s) out of {timesplayed} round(s).")
    
#While loop to continue playing game
while True: 
    game()  
    start_game=input("Would you like to play another round? Please enter Yes or No.\n").lower()
    if start_game=="yes":
        continue
    else:
        print(pyfiglet.figlet_format("GAMEOVER"))
        if player_wins>Daisy_wins:
            print(pyfiglet.figlet_format("You WIN"))
        elif Daisy_wins>player_wins:
            print(pyfiglet.figlet_format("You LOSE"))
        else:
            print(pyfiglet.figlet_format("You TIED with Daisy"))
        cowsay.cow("Thank you for playing with Daisy!")
        break



