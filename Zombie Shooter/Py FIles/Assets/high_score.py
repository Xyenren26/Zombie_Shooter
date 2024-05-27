import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_FPS = 60

# Load background image and resize it to match the screen size
background_image = pygame.image.load("hardcore/background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('High scores')

# Define clock for controlling frame rate
clock = pygame.time.Clock()

# Function to create rectangular buttons
def draw_button(x, y, width, height, color, highlight_color, text, font_size, text_color):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect)
    pygame.draw.rect(screen, highlight_color, button_rect, 3)  # Highlight border
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return button_rect

# Function to load scores from file
def load_scores(file_name):
    scores = []
    try:
        with open(file_name, 'r') as file:
            scores = file.readlines()
    except FileNotFoundError:
        print(f"File '{file_name}' not found")
    return scores

# Function to display scores on the screen
def display_scores(scores, font, x, y, screen):
    score_font = pygame.font.Font(None, font)
    for i, score in enumerate(scores):
        score_text = score_font.render(f"Score {i + 1}: {score.strip()}", True, (255, 255, 255))
        screen.blit(score_text, (x, y + i * 30))

# Variable to store the selected scores and file name
selected_scores = []
selected_file = ""

# Game Loop
running = True
scores_loaded = False
while running:
    screen.blit(background_image, (0, 0))  # Clear the screen with the background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background_image, (0, 0))  # Clear the screen after displaying the info

    # Define button dimensions and colors
    text_color = (255, 255, 255)
    button_width = 90
    button_height = 40
    button_start_y = 20
    button_color = (100, 100, 100)
    button_highlight_color = (150, 150, 150)

    Back_button_x = 20
    Easy_button_x = Back_button_x + button_width + 10  # Add gap for the second button
    Normal_button_x = Easy_button_x + button_width + 10  # Add gap for the Normal button
    Hardcore_button_x = Normal_button_x + button_width + 10  # Add gap for the Hardcore button
    Player2_Easy_button_x = Hardcore_button_x + button_width + 10  # Add gap for Player2 Easy button
    Player2_Normal_button_x = Player2_Easy_button_x + button_width + 10  # Add gap for Player2 Normal button
    Player2_Hardcore_button_x = Player2_Normal_button_x + button_width + 10  # Add gap for Player2 Hardcore button
    Final_button_x = Player2_Hardcore_button_x + button_width + 10  # Add gap for the Final button

    # Drawing buttons with updated positions
    Back_button = draw_button(Back_button_x, button_start_y, button_width, button_height,
        button_color, button_highlight_color, "Back", 18, text_color)
    Easy_button = draw_button(Easy_button_x, button_start_y, button_width, button_height,
        button_color, button_highlight_color, "Easy", 18, text_color)
    Normal_button = draw_button(Normal_button_x, button_start_y, button_width, button_height,
        button_color, button_highlight_color, "Normal", 18, text_color)
    Hardcore_button = draw_button(Hardcore_button_x, button_start_y, button_width, button_height,
        button_color, button_highlight_color, "Hardcore", 18, text_color)
    Player2_Easy_button = draw_button(Player2_Easy_button_x, button_start_y, button_width, button_height,
        button_color, button_highlight_color, "Player2 Easy", 18, text_color)
    Player2_Normal_button = draw_button(Player2_Normal_button_x, button_start_y, button_width, button_height,
        button_color, button_highlight_color, "Player2 Normal", 18, text_color)
    Player2_Hardcore_button = draw_button(Player2_Hardcore_button_x, button_start_y, button_width, button_height,
        button_color, button_highlight_color, "Player2 Hardcore", 18, text_color)
    Final_button = draw_button(Final_button_x, button_start_y, button_width, button_height,
        button_color, button_highlight_color, "Final", 18, text_color)

    # Handle button clicks on the Highscore screen
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
        if Back_button.collidepoint(mouse_x, mouse_y):
            pygame.quit()
            subprocess.run(["python", "zombie shooter.py"])
        elif Easy_button.collidepoint(mouse_x, mouse_y):
            selected_file = 'scores/Easy_scores.txt'
            selected_scores = load_scores(selected_file)
            scores_loaded = True
        elif Normal_button.collidepoint(mouse_x, mouse_y):
            selected_file = 'scores/Normal_scores.txt'
            selected_scores = load_scores(selected_file)
            scores_loaded = True
        elif Hardcore_button.collidepoint(mouse_x, mouse_y):
            selected_file = 'scores/Hardcore_scores.txt'
            selected_scores = load_scores(selected_file)
            scores_loaded = True
        elif Player2_Easy_button.collidepoint(mouse_x, mouse_y):
            selected_file = 'scores/Player2_Easy_scores.txt'
            selected_scores = load_scores(selected_file)
            scores_loaded = True
        elif Player2_Normal_button.collidepoint(mouse_x, mouse_y):
            selected_file = 'scores/Player2_Normal_scores.txt'
            selected_scores = load_scores(selected_file)
            scores_loaded = True
        elif Player2_Hardcore_button.collidepoint(mouse_x, mouse_y):
            selected_file = 'scores/Player2_Hardcore_scores.txt'
            selected_scores = load_scores(selected_file)
            scores_loaded = True
        elif Final_button.collidepoint(mouse_x, mouse_y):
            selected_file = 'scores/Final_scores.txt'
            selected_scores = load_scores(selected_file)
            scores_loaded = True
    # Display the selected scores continuously until a new button is clicked
    if scores_loaded:
        display_scores(selected_scores, 28, 350, 100, screen)

    pygame.display.flip()
    clock.tick(GAME_FPS)

pygame.quit()
sys.exit()
