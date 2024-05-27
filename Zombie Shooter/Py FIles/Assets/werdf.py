import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Button dimensions and spacing
button_width = 100
button_height = 25
button_spacing = 20

# Calculate total width needed for buttons
total_button_width = (button_width + button_spacing) * 7  # 7 buttons in total

# Starting position for buttons to be centered horizontally
start_x = (screen_width - total_button_width) // 2
start_y = screen_height // 2 - button_height // 2

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Example")

# Function to create buttons
def create_button(x, y, width, height, color, text, action=None):
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font(None, 18)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    screen.blit(text_surface, text_rect)

    # Get mouse position and click
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Button functionality
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, black, (x, y, width, height), 3)
        if click[0] == 1 and action is not None:
            if action == "Easy":
                print("Easy mode selected")
            elif action == "Normal":
                print("Normal mode selected")
            elif action == "Hardcore":
                print("Hardcore mode selected")
            elif action == "Easy Player 2":
                print("Easy mode for Player 2 selected")
            elif action == "Normal Player 2":
                print("Normal mode for Player 2 selected")
            elif action == "Hardcore Player 2":
                print("Hardcore mode for Player 2 selected")
            elif action == "Final":
                print("Final mode selected")
                
running = True
while running:
    screen.fill(white)

    # Create buttons
    create_button(start_x, start_y, button_width, button_height, blue, "Easy", action="Easy")
    create_button(start_x + button_width + button_spacing, start_y, button_width, button_height, green, "Normal", action="Normal")
    create_button(start_x + (button_width + button_spacing) * 2, start_y, button_width, button_height, red, "Hardcore", action="Hardcore")
    create_button(start_x + (button_width + button_spacing) * 3, start_y, button_width, button_height, blue, "Easy Player 2", action="Easy Player 2")
    create_button(start_x + (button_width + button_spacing) * 4, start_y, button_width, button_height, green, "Normal Player 2", action="Normal Player 2")
    create_button(start_x + (button_width + button_spacing) * 5, start_y, button_width, button_height, red, "Hardcore Player 2", action="Hardcore Player 2")
    create_button(start_x + (button_width + button_spacing) * 6, start_y, button_width, button_height, black, "Final", action="Final")

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()
