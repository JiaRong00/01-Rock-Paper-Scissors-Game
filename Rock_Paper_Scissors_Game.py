# This is the rock paper scissors game.

#Initiate game
game_continue=True
import sys
print("Welcome to the rock paper scissors game!")
start_game=input("Type Yes if you would like to begin the game\n").lower()
choices={1:"Rock", 2:"Scissors", 3:"Paper"}
timesplayed=0
losecount=0

#While loop to keep playing the game 
while game_continue:
    if start_game =='yes':
        playerchoice=int(input("Please enter:\n1 for Rock✊\n2 for Scissors✌️\n3 for Paper✋\n"))
        if playerchoice != 1 and playerchoice!=2 and playerchoice !=3:
            playerchoice=input("You have entered an invalid value. Please try again.\nPlease enter:\n1 for Rock✊\n2 for Scissors✌️\n3 for Paper✋\n")
    #Computer chooses a random choice
        import random
        choice_list=[1,2,3]
        computer_choice=random.choice(choice_list)
        timesplayed+=1
    else:
        sys.exit("Thank you for your time, please join us next time!")

#Determinining who won. 
# Rock (1) wins scissors (2) but lose to paper (3)
# Scissors (2) wins paper (3)
    print(f"You chose {choices[playerchoice]}\nComputer chose {choices[computer_choice]}")
    if playerchoice==computer_choice:
        print("There is a tie🙌")
        losecount+=1
    elif playerchoice ==1 and computer_choice==2:
        print("You win!😁")
    elif playerchoice ==2 and computer_choice==3:
        print("You win!😁")
    elif playerchoice ==3 and computer_choice==1:
        print("You win!😁")
    else:
        print("You lose!😭")
        losecount+=1
    print(f"You have won {timesplayed-losecount} time(s) out of {timesplayed} round(s).")
    start_game=input("Would you like to play another round? Please enter Yes or No.\n").lower()
    if start_game=="no":
        game_continue=False
        sys.exit("Thank you for playing!")





