import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock Paper Scissor Game")

background_image = pygame.image.load('graphics/blue.png').convert()
font = pygame.font.Font('font/SunnyspellsRegular.otf', 40)
play_message = font.render("Welcome to Rock Paper Scissor Game", True, (255, 255, 255))
play_message2 = font.render("Click on the Start Button to begin", True, (255, 255, 255))
score_font = pygame.font.Font('font/SunnyspellsRegular.otf', 35)
start_button=pygame.image.load("graphics/Start.png")
start_rect=start_button.get_rect(topleft=(220,190))

button_rock = pygame.image.load('graphics/button_rock.png')
button_paper = pygame.image.load('graphics/button_paper.png')
button_scissor = pygame.image.load('graphics/button_scissor.png')
rock_rect = button_rock.get_rect(topleft=(35, 290))
paper_rect = button_rock.get_rect(topleft=(240, 290))
scissor_rect = button_rock.get_rect(topleft=(425, 290))

rock = pygame.image.load('graphics/rock.png')
paper = pygame.image.load('graphics/paper.png')
scissor = pygame.image.load('graphics/scissor.png')
choices = [rock, paper, scissor]

reset=pygame.image.load("graphics/Reset.png")
back=pygame.image.load("graphics/Back.png")
reset_rect = reset.get_rect(topleft=(470,350))
back_rect = back.get_rect(topleft=(400,350))

start_game = False
player2 = ""
user_choice = None
player2_choice = None
show_choice = False
user_score=0
player2_score=0
winner=""

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
            if rock_rect.collidepoint(event.pos):
                pick_weapon(0)
                print("rock")
            elif paper_rect.collidepoint(event.pos):
                pick_weapon(1)
                print('paper')
            elif scissor_rect.collidepoint(event.pos):
                pick_weapon(2)
                print("scissor")
            elif reset_rect.collidepoint(event.pos):
                user_score=0
                player2_score=0
            elif back_rect.collidepoint(event.pos):
                if show_choice:
                    show_choice=False
                else:
                    start_game=False
               
            
    screen.blit(background_image, (0, 0))
    user_score_message = score_font.render(f"Your Score {user_score}", True, (255, 255, 255))
    player2_score_message = score_font.render(f"Player 2 Score {player2_score}", True, (255, 255, 255))

    if start_game is False:
        screen.blit(play_message, (50, 120))
        screen.blit(play_message2, (70, 160))
        screen.blit(start_button,start_rect) 

    if show_choice:
        screen.blit(user_choice, (60, 70))
        screen.blit(player2_choice, (350, 70))
        screen.blit(user_score_message, (20, 20))
        screen.blit(player2_score_message, (390, 20))
        win_message = score_font.render(f"You {winner}", True, (250, 240, 180))
        screen.blit(win_message, (250, 130))
        screen.blit(reset, reset_rect)
           
    if start_game:
        screen.blit(button_rock, rock_rect)
        screen.blit(button_paper, paper_rect)
        screen.blit(button_scissor, scissor_rect)
        screen.blit(back, back_rect)

    pygame.display.update()
    clock.tick(10)
