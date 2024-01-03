import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock Paper Scissor Game")

#Creating the start game screen
background_image = pygame.image.load('graphics/blue.png').convert()
font = pygame.font.Font('font/SunnyspellsRegular.otf', 40)
play_message = font.render("Welcome to Rock Paper Scissor Game", True, (255, 255, 255))
play_message2 = font.render("Click on the Start Button to begin", True, (255, 255, 255))
score_font = pygame.font.Font('font/SunnyspellsRegular.otf', 35)
start_button=pygame.image.load("graphics/Start.png")
start_rect=start_button.get_rect(topleft=(220,190))

#Create characters
char1=pygame.image.load("graphics/Piglet.png")
char2=pygame.image.load("graphics/Cow.png")
char1_tiny=pygame.image.load("graphics/Piglet_tiny.png")
char2_tiny=pygame.image.load("graphics/Cow_tiny.png")
char1_rect = char1.get_rect(topleft=(350,0))
char2_rect = char2.get_rect(topleft=(370,210))
character_names = {"Charlotte": char1_tiny, "Daisy": char2_tiny}
characters = list(character_names.keys())
font2 = pygame.font.Font('font/SunnyspellsRegular.otf', 80)
char_message = font2.render("Pick your", True, (250, 240, 180))
char_message2 = font2.render("opponent to", True, (250, 240, 180))
char_message3 = font2.render("begin!", True, (250, 240, 180))

#Create buttons to choose rock, paper, scissors
button_rock = pygame.image.load('graphics/button_rock.png')
button_paper = pygame.image.load('graphics/button_paper.png')
button_scissor = pygame.image.load('graphics/button_scissor.png')
rock_rect = button_rock.get_rect(topleft=(35, 290))
paper_rect = button_rock.get_rect(topleft=(240, 290))
scissor_rect = button_rock.get_rect(topleft=(425, 290))

#Images of choice
rock = pygame.image.load('graphics/rock.png')
paper = pygame.image.load('graphics/paper.png')
scissor = pygame.image.load('graphics/scissor.png')
choices = [rock, paper, scissor]

#create back and reset buttons
reset=pygame.image.load("graphics/Reset.png")
back=pygame.image.load("graphics/Back.png")
reset_rect = reset.get_rect(topleft=(470,350))
back_rect = back.get_rect(topleft=(400,350))

#Setting initial conditions
start_game = False
player2 = ""
player2_back=""
user_choice = None
player2_choice = None
show_choice = False
user_score=0
player2_score=0
winner=""
player2_tiny=""

def pick_char(char):
    global player2, player2_tiny, player2_score, user_score
    player2=char
    player2_tiny = character_names[char]
    if player2_back != char:
        player2_score = 0
        user_score = 0

def pick_weapon(choice):
     global user_choice, player2_choice, show_choice, choices, user_score, player2_score, winner
     user_choice = choices[choice]
     show_choice = True
     player2_choice = random.choice(choices)
     if  user_choice == rock and player2_choice==scissor:
        user_score+=1
        winner= "won!"
     elif user_choice ==scissor and player2_choice==paper:
        user_score+=1
        winner= "won!"
     elif user_choice ==paper and player2_choice==rock:
        user_score+=1
        winner= "won!"
     elif user_choice == player2_choice:
        winner= "tied!"
     else:
        player2_score+=1
        winner= "lost!"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                start_game=True
            elif player2=="":
                if char1_rect.collidepoint(event.pos):
                    pick_char("Charlotte")
                elif char2_rect.collidepoint(event.pos):
                    pick_char("Daisy")
            elif rock_rect.collidepoint(event.pos):
                pick_weapon(0)
            elif paper_rect.collidepoint(event.pos):
                pick_weapon(1)
            elif scissor_rect.collidepoint(event.pos):
                pick_weapon(2)
            elif reset_rect.collidepoint(event.pos):
                user_score=0
                player2_score=0
            elif back_rect.collidepoint(event.pos):
                if show_choice:
                    show_choice=False
                    player2_back=player2
                    player2=""
                else:
                    start_game=False
               
            
    screen.blit(background_image, (0, 0))
    user_score_message = score_font.render(f"Your Score {user_score}", True, (255, 255, 255))
    player2_score_message = score_font.render(f"{player2} Score {player2_score}", True, (255, 255, 255))

    if start_game is False:
        screen.blit(play_message, (50, 120))
        screen.blit(play_message2, (70, 160))
        screen.blit(start_button,start_rect) 

    if show_choice:
        screen.blit(user_choice, (20, 70))
        screen.blit(player2_choice, (350, 70))
        screen.blit(user_score_message, (20, 20))
        screen.blit(player2_score_message, (390, 20))
        win_message = font.render(f"You {winner}", True, (250, 240, 180))
        screen.blit(win_message, (230, 130))
        screen.blit(reset, reset_rect)
        screen.blit(character_names[player2], (330,10))
           
    if start_game and player2 == "":
        screen.blit(char1, char1_rect)
        screen.blit(char2, char2_rect)
        screen.blit(char_message, (55, 100))
        screen.blit(char_message2, (20, 170))
        screen.blit(char_message3, (100, 240))

    if start_game and player2 != "":
        screen.blit(button_rock, rock_rect)
        screen.blit(button_paper, paper_rect)
        screen.blit(button_scissor, scissor_rect)
        screen.blit(back, back_rect)
        
    clock.tick(60)
    pygame.display.update()
   
