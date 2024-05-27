import pygame
import sys
import subprocess
import os

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load background image
background_image = pygame.image.load("menu/background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load background2 image
background2_image = pygame.image.load("hardcore/background.png")
background2_image = pygame.transform.scale(background2_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define button rectangles
quit_button_rect = pygame.Rect(20, SCREEN_HEIGHT - 60, 100, 40)
highscore_button_rect = pygame.Rect(670, SCREEN_HEIGHT - 60, 100, 40)
about_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 150, 100, 40)
one_player_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 100, 40)
two_players_button_rect = pygame.Rect(SCREEN_WIDTH // 2 + 20, SCREEN_HEIGHT // 2 + 50, 100, 40)

# Set up texts and buttons
font = pygame.font.Font(None, 50)

quit_font = pygame.font.Font(None, 30)
quit_text = quit_font.render("Quit", True, (255, 255, 255))
highscore_text = quit_font.render("Highscore", True, (255, 255, 255))
about_text = quit_font.render("About", True, (255, 255, 255))

player_font = pygame.font.Font(None, 30)
one_player_text = player_font.render("1 Player", True, (255, 255, 255))
two_players_text = player_font.render("2 Players", True, (255, 255, 255))

def read_all_scores():
    with open(high_scores.txt, 'r') as file:
        scores = [int(score.strip()) for score in file.readlines()]
    return scores

# Function to display scores on the screen
def display_scores(scores):
    y_position = 100  # Initial y position to display scores
    for score in scores:
        score_text_surface = your_font.render(f"Score: {score}", True, (255, 255, 255))  # Change (255, 255, 255) to your text color
        screen.blit(score_text_surface, (x_position, y_position))  # Replace x_position with desired x coordinate
        y_position += 30  # Increment y position for the next score


def start_menu():
    difficulty_menu = False
    show_difficulty_menu = False
    difficulty_menu2 = False
    show_difficulty_menu2 = False

    while True:
        screen.blit(background_image, (0, 0))


        pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)
        pygame.draw.rect(screen, (255, 0, 0), highscore_button_rect)
        pygame.draw.rect(screen, (0, 255, 0), about_button_rect)
        pygame.draw.rect(screen, (0, 0, 255), one_player_button_rect)
        pygame.draw.rect(screen, (255, 255, 0), two_players_button_rect)

         # Adjusting text rendering positions within the buttons
        screen.blit(quit_text, quit_text.get_rect(center=quit_button_rect.center))
        screen.blit(highscore_text, highscore_text.get_rect(center=highscore_button_rect.center))
        screen.blit(about_text, about_text.get_rect(center=about_button_rect.center))
        screen.blit(one_player_text, one_player_text.get_rect(center=one_player_button_rect.center))
        screen.blit(two_players_text, two_players_text.get_rect(center=two_players_button_rect.center))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                elif highscore_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    subprocess.run(["python", "high_score.py"])
                elif about_button_rect.collidepoint(mouse_pos):
        
                    screen.blit(background2_image, (0, 0))  # Clear the screen after displaying the info

                    about_font = pygame.font.Font(None, 35)
                    about_content = about_font.render("This game is developed by the CEIT-37-502A students:", True, (255, 255, 255))
                    about_content2 = about_font.render("Tavera, Jericho", True, (255, 255, 255))
                    about_content3 = about_font.render("Ballesteros Rolando", True, (255, 255, 255))
                    about_content4 = about_font.render("Salem Stephanie", True, (255, 255, 255))
                    about_content5 = about_font.render("Controls for Player 1:", True, (255, 255, 255))
                    about_content6 = about_font.render("ARROW KEYS for movement, SPACE BAR for FIRING", True, (255, 255, 255))
                    about_content7 = about_font.render("Controls for Player 2:", True, (255, 255, 255))
                    about_content8 = about_font.render("W for UP, A for LEFT, S for DOWN, D for RIGHT, Z for FIRING", True, (255, 255, 255))

                    about_rect = about_content.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
                    about_rect2 = about_content2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120))
                    about_rect3 = about_content3.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 90))
                    about_rect4 = about_content4.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
                    about_rect5 = about_content5.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                    about_rect6 = about_content6.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
                    about_rect7 = about_content7.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
                    about_rect8 = about_content8.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130))

                    screen.blit(about_content, about_rect)
                    screen.blit(about_content2, about_rect2)
                    screen.blit(about_content3, about_rect3)
                    screen.blit(about_content4, about_rect4)
                    screen.blit(about_content5, about_rect5)
                    screen.blit(about_content6, about_rect6)
                    screen.blit(about_content7, about_rect7)
                    screen.blit(about_content8, about_rect8)

                    pygame.display.flip()
                    pygame.time.wait(7000)  # Display the about info for 7 seconds
                    screen.blit(background2_image, (0, 0))  # Clear the screen after displaying the info


                elif one_player_button_rect.collidepoint(mouse_pos):
                    difficulty_menu = True
                elif two_players_button_rect.collidepoint(mouse_pos):
                    difficulty_menu2 = True

        if difficulty_menu and not show_difficulty_menu:
            show_difficulty_menu = True
            difficulty_menu_screen()
        if difficulty_menu2 and not show_difficulty_menu2:
            show_difficulty_menu2 = True
            difficulty_menu_screen2()

        clock.tick(GAME_FPS)

def difficulty_menu_screen():
    difficulty_selected = False

    while not difficulty_selected:
        screen.blit(background2_image, (0, 0))

        difficulty_text = player_font.render("Select Difficulty:", True, (255, 255, 255))
        difficulty_rect = difficulty_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

        easy_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, 100, 40)
        normal_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50, 100, 40)
        hardcore_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 100, 100, 40)

        easy_text = player_font.render("Easy", True, (255, 255, 255))
        normal_text = player_font.render("Normal", True, (255, 255, 255))
        hardcore_text = player_font.render("Hardcore", True, (255, 255, 255))

        pygame.draw.rect(screen, (0, 0, 255), easy_rect)
        pygame.draw.rect(screen, (0, 255, 0), normal_rect)
        pygame.draw.rect(screen, (255, 0, 0), hardcore_rect)

       # Adjusting text rendering positions within the difficulty rectangles
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(easy_text, easy_rect.move((10, 10)))  # Adjust the position to fit inside the rectangle
        screen.blit(normal_text, normal_rect.move((10, 10)))  # Adjust the position to fit inside the rectangle
        screen.blit(hardcore_text, hardcore_rect.move((10, 10)))  # Adjust the position to fit inside the rectangle


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_rect.collidepoint(mouse_pos):
                    difficulty_selected = True
                    subprocess.Popen(["python", "player1-easy.py", "--difficulty", "easy"])
                    pygame.quit()
                    sys.exit()
                elif normal_rect.collidepoint(mouse_pos):
                    difficulty_selected = True
                    subprocess.Popen(["python", "player1-normal.py", "--difficulty", "normal"])
                    pygame.quit()
                    sys.exit()
                elif hardcore_rect.collidepoint(mouse_pos):
                    difficulty_selected = True
                    subprocess.Popen(["python", "player1-hardcore.py", "--difficulty", "hardcore"])
                    pygame.quit()
                    sys.exit()

        clock.tick(GAME_FPS)
def difficulty_menu_screen2():
    difficulty_selected = False

    while not difficulty_selected:
        screen.blit(background2_image, (0, 0))

        difficulty_text = player_font.render("Select Difficulty:", True, (255, 255, 255))
        difficulty_rect = difficulty_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

        easy_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, 100, 40)
        normal_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50, 100, 40)
        hardcore_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 100, 100, 40)

        easy_text = player_font.render("Easy", True, (255, 255, 255))
        normal_text = player_font.render("Normal", True, (255, 255, 255))
        hardcore_text = player_font.render("Hardcore", True, (255, 255, 255))

        pygame.draw.rect(screen, (0, 0, 255), easy_rect)
        pygame.draw.rect(screen, (0, 255, 0), normal_rect)
        pygame.draw.rect(screen, (255, 0, 0), hardcore_rect)

       # Adjusting text rendering positions within the difficulty rectangles
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(easy_text, easy_rect.move((10, 10)))  # Adjust the position to fit inside the rectangle
        screen.blit(normal_text, normal_rect.move((10, 10)))  # Adjust the position to fit inside the rectangle
        screen.blit(hardcore_text, hardcore_rect.move((10, 10)))  # Adjust the position to fit inside the rectangle


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_rect.collidepoint(mouse_pos):
                    difficulty_selected = True
                    subprocess.Popen(["python", "player2-easy.py", "--difficulty", "easy"])
                    pygame.quit()
                    sys.exit()
                elif normal_rect.collidepoint(mouse_pos):
                    difficulty_selected = True
                    subprocess.Popen(["python", "player2-normal.py", "--difficulty", "normal"])
                    pygame.quit()
                    sys.exit()
                elif hardcore_rect.collidepoint(mouse_pos):
                    difficulty_selected = True
                    subprocess.Popen(["python", "player2-hardcore.py", "--difficulty", "hardcore"])
                    pygame.quit()
                    sys.exit()

        clock.tick(GAME_FPS)
    

# Start menu
start_menu()
