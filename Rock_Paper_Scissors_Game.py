# This is the rock paper scissors game.

#Initiate game
game_continue=True
import sys
print("Welcome to the rock paper scissors game!")
start_game=input("Type Yes if you would like to begin the game\n").lower()
timesplayed=0
wincount=0

#Define function to play game
def game():
    if start_game =='yes':
        playerchoice=int(input("Please enter:\n1 for Rock✊\n2 for Scissors✌️\n3 for Paper✋\n"))
        #while loop to prompt player to enter valid input 
        while playerchoice != 1 and playerchoice!=2 and playerchoice !=3:
            playerchoice=int(input("You have entered an invalid value. Please try again.\nPlease enter:\n1 for Rock✊\n2 for Scissors✌️\n3 for Paper✋\n"))
    #Computer chooses a random choice
        import random
        choice_list=[1,2,3]
        computer_choice=random.choice(choice_list)
        global timesplayed
        timesplayed+=1
    else:
        sys.exit("Thank you for your time, please join us next time!")
#Determinining who won. 
# Rock (1) wins scissors (2) but lose to paper (3)
# Scissors (2) wins paper (3)
    choices={1:"Rock", 2:"Scissors", 3:"Paper"}
    global wincount
    print(f"You chose {choices[playerchoice]}\nComputer chose {choices[computer_choice]}")
    if playerchoice==computer_choice:
        print("There is a tie🙌")
    elif playerchoice ==1 and computer_choice==2:
        print("You win!😁")
        wincount+=1
    elif playerchoice ==2 and computer_choice==3:
        print("You win!😁")
        wincount+=1
    elif playerchoice ==3 and computer_choice==1:
        print("You win!😁")
        wincount+=1
    else:
        print("You lose!😭")
    print(f"You have won {wincount} time(s) out of {timesplayed} round(s).")
    
#While loop to continue playing game
while True: 
    game()  
    start_game=input("Would you like to play another round? Please enter Yes or No.\n").lower()
    if start_game=="yes":
        continue
    else:
        print("Thank you for playing!")
        break




