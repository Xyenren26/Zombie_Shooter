import pygame
import sys
import random
import math
import subprocess
import os

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_FPS = 90


# Initialize Pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
high_scores_file = "scores/Easy_scores.txt"
# Function to load high scores from a file
def load_high_scores():
    if os.path.exists(high_scores_file):
        with open(high_scores_file, "r") as file:
            lines = file.readlines()
            high_scores = [int(score.strip()) for score in lines]
            high_scores.sort(reverse=True)
            return high_scores
    else:
        return []
# Function to save high scores to a file
def save_high_scores():
    high_scores = load_high_scores()
    high_scores.append(high_score)
    high_scores.sort(reverse=True)
    with open(high_scores_file, "w") as file:
        for score in high_scores[:5]:  # Save only the top 5 scores
            file.write(f"{score}\n")
# Sounds:
SHOT_SOUND = pygame.mixer.Sound("sound/shot_sound.wav")
DIE_SOUND = pygame.mixer.Sound("sound/player_dead.mp3")
GAMEPLAY_SOUND = pygame.mixer.Sound("sound/gameplay_sound.wav")
GAMEPLAY_SOUND.set_volume(0.5)  # Set the volume of the sound
KILL_SOUND = pygame.mixer.Sound("sound/kill_sound.mp3")
RELOAD_SOUND = pygame.mixer.Sound("sound/reload_sound.wav")

# Load background image and resize it to match the screen size
background_image = pygame.image.load("easy/background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load player image and resize it to the appropriate size
player_image_right = pygame.image.load("easy/player_right.png")
player_image_left = pygame.image.load("easy/player_left.png")
player_image_up = pygame.image.load("easy/player_up.png")
player_image_down = pygame.image.load("easy/player_down.png")
player_image = player_image_right  # Initial player image

# Resize player images
player_image = pygame.transform.scale(player_image, (50, 50))  # Set player size
player_image_right = pygame.transform.scale(player_image_right, (50, 50))  # Set player size
player_image_left = pygame.transform.scale(player_image_left, (50, 50))  # Set player size
player_image_down = pygame.transform.scale(player_image_down, (50, 50))  # Set player size
player_image_up = pygame.transform.scale(player_image_up, (50, 50))  # Set player size
player_alive = True
PLAYER_SPEED = 3

player_rect = player_image.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Assuming you have images for zombie movements in different directions: zombie_left, zombie_right, zombie_up, zombie_down

# Initialize lists for different direction frames
zombie_frames_right = []
zombie_frames_left = []
zombie_frames_up = []
zombie_frames_down = []

# Load and resize frames for each direction
for i in range(1, 5):
    zombie_image_right = pygame.image.load(f"easy/zombie_frame/zombie_right/zombie_right({i}).png")
    zombie_image_right = pygame.transform.scale(zombie_image_right, (50, 50))
    zombie_frames_right.append(zombie_image_right)

    zombie_image_left = pygame.image.load(f"easy/zombie_frame/zombie_left/zombie_left({i}).png")
    zombie_image_left = pygame.transform.scale(zombie_image_left, (50, 50))
    zombie_frames_left.append(zombie_image_left)

    zombie_image_up = pygame.image.load(f"easy/zombie_frame/zombie_up/zombie_up({i}).png")
    zombie_image_up = pygame.transform.scale(zombie_image_up, (50, 50))
    zombie_frames_up.append(zombie_image_up)

    zombie_image_down = pygame.image.load(f"easy/zombie_frame/zombie_down/zombie_down({i}).png")
    zombie_image_down = pygame.transform.scale(zombie_image_down, (50, 50))
    zombie_frames_down.append(zombie_image_down)

# Initialize variables for animation
zombie_image = zombie_image_right  # Initial player image
current_zombie_image = zombie_frames_right[0]  # Default image (can be any initial frame)
current_frame = 0
frame_counter = 0
frame_duration = 10  # Change this value to adjust the speed of the animation

zombie_alive = True


zombie_rect = player_image.get_rect()
zombie_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


# Load zombie2 image and resize it to the appropriate size
zombie2_image_right = pygame.image.load("easy/zombie2_right.png")
zombie2_image_left = pygame.image.load("easy/zombie2_left.png")
zombie2_image_up = pygame.image.load("easy/zombie2_up.png")
zombie2_image_down = pygame.image.load("easy/zombie2_down.png")
zombie2_image = zombie2_image_right  # Initial player image

# Resize zombie images
zombie2_image = pygame.transform.scale(zombie2_image, (50, 50))  # Set player size
zombie2_image_right = pygame.transform.scale(zombie2_image_right, (50, 50))  # Set player size
zombie2_image_left = pygame.transform.scale(zombie2_image_left, (50, 50))  # Set player size
zombie2_image_down = pygame.transform.scale(zombie2_image_down, (50, 50))  # Set player size
zombie2_image_up = pygame.transform.scale(zombie2_image_up, (50, 50))  # Set player size
zombie2_alive = True


zombie2_rect = player_image.get_rect()
zombie2_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Load blood frames and resize them
blood_frames = []
for i in range(1, 12):  # Assuming the blood frames are named blood1.png to blood6.png
    blood_frame = pygame.image.load(f"easy/blood_frame/blood ({i}).png")
    blood_frame = pygame.transform.scale(blood_frame, (100, 100))  # Resize the frames
    blood_frames.append(blood_frame)

# Initialize variables for animation
frame_blood_duration = 100  # Change this value to adjust the speed of the animation
blood_animation_duration = 5  # Adjust this value as needed
blood_animation_timer = 0
current_blood_frame_index = 0
blood_display = False

# Load bullet image and resize it to the appropriate size
bullet_image = pygame.image.load("easy/bullet.png")
bullet_image = pygame.transform.scale(bullet_image, (10, 10))  # Set bullet size

# Load ammo box image and resize it
ammo_box_image = pygame.image.load("easy/ammo.png")
ammo_box_image = pygame.transform.scale(ammo_box_image, (30, 30))  # Set ammo box size

# Load bush frames and resize them
bush_frames = []
for i in range(1, 5):  # Assuming the bush frames are named bush1.png to bush6.png
    bush_frame = pygame.image.load(f"easy/bush_frame/bush{i}.png")
    bush_frame = pygame.transform.scale(bush_frame, (50, 50))  # Resize the frames
    bush_frames.append(bush_frame)

# Initialize variables for animation
current_frame_bush = 0
frame_bush_counter = 0
frame_bush_duration = 50  # Change this value to adjust the speed of the animation


# Generate random bush positions
bush_positions = []
for _ in range(25):
    bush_x, bush_y = 0, 0
    
    # Ensure bush do not spawn too close to the player or other bush
    while True:
        bush_x = random.randint(0, SCREEN_WIDTH - 50)
        bush_y = random.randint(0, SCREEN_HEIGHT - 50)
        
        # Check if the bush is too close to the player
        distance_to_player = math.sqrt((bush_x - player_rect.centerx) ** 2 + (bush_y - player_rect.centery) ** 2)
        if distance_to_player > 100:  # Adjust the distance threshold as needed
            # Check if the bush is too close to existing bush
            bush_far_from_others = all(
                math.sqrt((bush_x - bx) ** 2 + (bush_y - by) ** 2) > 50 for bx, by in bush_positions
            )
            if bush_far_from_others:
                break

    bush_positions.append((bush_x, bush_y))


class Zombie:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 25), random.randint(0, SCREEN_HEIGHT - 25), 25, 25)
        self.image = zombie_image_right  # Initial zombie image

    def update(self):
        if not paused:
            global zombie_image  # Ensure this is the global variable defined outside the class

            # Movement logic for the zombie
            # Here's a simple movement where the zombie moves towards the player's position
            if self.rect.x < player_rect.x:
                self.direction = "RIGHT"
                self.rect.x += 1  # Adjust the zombie's speed here
                zombie_image = zombie_image_right  # Update the zombie's image to face right
            elif self.rect.x > player_rect.x:
                self.direction = "LEFT"
                self.rect.x -= 1  # Adjust the zombie's speed here
                zombie_image = zombie_image_left  # Update the zombie's image to face left
            if self.rect.y < player_rect.y:
                self.direction = "DOWN"
                self.rect.y += 1  # Adjust the zombie's speed here
                zombie_image = zombie_image_down  # Update the zombie's image to face down
            elif self.rect.y > player_rect.y:
                self.direction = "UP"
                self.rect.y -= 1  # Adjust the zombie's speed here
                zombie_image = zombie_image_up  # Update the zombie's image to face up

            
class Zombie2:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 25), random.randint(0, SCREEN_HEIGHT - 25), 25, 25)
        self.hits_remaining = 2  # Number of hits required to defeat this zombie
        self.speed = 1  # Adjust the speed of this zombie
        self.image = zombie2_image_right  # Initial zombie image

    def update(self):
        if not paused:
            global zombie2_image  # Ensure this is the global variable defined outside the class

            # Movement logic for the zombie
            # Here's a simple movement where the zombie moves towards the player's position
            if self.rect.x < player_rect.x:
                self.rect.x += self.speed  
                zombie2_image = zombie2_image_right  # Update the zombie's image to face right
            elif self.rect.x > player_rect.x:
                self.rect.x -= self.speed  
                zombie2_image = zombie2_image_left  # Update the zombie's image to face left
            if self.rect.y < player_rect.y:
                self.rect.y += self.speed 
                zombie2_image = zombie2_image_down  # Update the zombie's image to face down
            elif self.rect.y > player_rect.y:
                self.rect.y -= self.speed
                zombie2_image = zombie2_image_up  # Update the zombie's image to face up



enemies = []
zombie2 = None  # Initialize zombie2 as None initially
zombie_RESPAWN_AMOUNT = 2  # Number of enemies to respawn when an zombie is killed

            
def spawn_enemies():
    global enemies
    enemies = []

    # Count existing enemies to determine how many more to spawn
    existing_enemies = len(enemies)
    if existing_enemies < 11:  # Check if there are fewer than 11 enemies
        enemies_to_spawn = min(zombie_RESPAWN_AMOUNT, 11 - existing_enemies)  # Calculate how many enemies to spawn without exceeding the limit
        for _ in range(enemies_to_spawn):
            new_zombie = Zombie()
            while True:
                new_zombie.rect.x = random.randint(0, SCREEN_WIDTH - 50)
                new_zombie.rect.y = random.randint(0, SCREEN_HEIGHT - 50)

                distance_to_player = math.sqrt((new_zombie.rect.x - player_rect.centerx) ** 2 + (new_zombie.rect.y - player_rect.centery) ** 2)

                # Ensure enemies do not spawn too close to the player
                if distance_to_player > 150:
                    enemies.append(new_zombie)
                    break

class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, BULLET_SIZE, BULLET_SIZE)
        self.direction = direction  # Direction of the bullet
        self.speed = BULLET_SPEED  # Speed of the bullet

    def update(self):
        # Move the bullet in the specified direction
        if self.direction == "UP":
            self.rect.y -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "RIGHT":
            self.rect.x += self.speed
            
class AmmoBox:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 30), random.randint(0, SCREEN_HEIGHT - 30), 30, 30)
        self.appeared_time = pygame.time.get_ticks()  # Track the time when the ammo box appeared




# Initialize bullets, ammo, zombie and player state
bullets = []
BULLET_SPEED = 10
BULLET_SIZE = 10
MAX_AMMO = 70
ammo_count = MAX_AMMO
RELOAD_TIME = 2000  # Time in milliseconds to reload (2 seconds in this case)
reloading = False
reload_text = False
# Add a flag to track if the player is slowed by a bush
slowed_by_bush = False
die_sound_played = False
last_shot_time = 0
paused = False
player_direction = "UP"
next_level = False

# Check collision between bullet and enemies
bullets_to_remove = []  # Create a list to store bullets to be removed
enemies_to_remove = []  # Create a list to store enemies to be removed



clock = pygame.time.Clock()
sound_timer = 0

# Initialize the ammo box
ammo_boxes = []
spawn_ammo_box_time = pygame.time.get_ticks()

# Spawn initial enemies
spawn_enemies()

# Set the caption and icon
pygame.display.set_caption("Zombie Shooter")
pygame.display.set_icon(zombie_image)


# Game Loop
running = True
game_over = False  # Flag to indicate if the game is over
player_score = 0 # Initialize player score
high_score = 0
picked_ammo_box = False #set ammo pick up to false

while running:
    screen.blit(background_image, (0, 0))  # Clear the screen with the background

    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds

    if sound_timer % (56 * 100) == 0:  # 56 = Program loops count per second.
        GAMEPLAY_SOUND.play(loops=-1)  # Loop the sound indefinitely
        sound_timer += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if not game_over:  # Only handle events if the game is not over
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # P key to pause/unpause
                    paused = not paused

    if not game_over:  # Check if the game is not over for player movement
        # Player movement
        keys = pygame.key.get_pressed()
        player_prev_x, player_prev_y = player_rect.x, player_rect.y  # Store previous player position
        if keys[pygame.K_LEFT]:
            player_rect.x -= PLAYER_SPEED
            player_image = player_image_left
            player_direction = "LEFT"
        if keys[pygame.K_RIGHT]:
            player_rect.x += PLAYER_SPEED
            player_image = player_image_right
            player_direction = "RIGHT"
        if keys[pygame.K_UP]:
            player_rect.y -= PLAYER_SPEED
            player_image = player_image_up
            player_direction = "UP"
        if keys[pygame.K_DOWN]:
            player_rect.y += PLAYER_SPEED
            player_image = player_image_down
            player_direction = "DOWN"

        # Ensure the player remains within the screen boundaries
        player_rect.x = max(0, min(player_rect.x, SCREEN_WIDTH - player_rect.width))
        player_rect.y = max(0, min(player_rect.y, SCREEN_HEIGHT - player_rect.height))

    # Handling bullet firing using keys obtained above and ammo count
    # Handling bullet firing using keys obtained above and ammo count
    if keys[pygame.K_SPACE] and player_alive and not reloading:  # Check if SPACE key is pressed and not reloading
        if ammo_count > 0:  # Check if there is ammo available
            current_time = pygame.time.get_ticks()  # Get the current time again
            if current_time - last_shot_time > 200:  # Limit shooting speed (200 milliseconds between shots)
                SHOT_SOUND.play()
                if player_direction == "UP":
                    bullets.append(Bullet(player_rect.centerx - (BULLET_SIZE // 2),
                                          player_rect.centery - BULLET_SIZE, "UP"))
                elif player_direction == "DOWN":
                    bullets.append(Bullet(player_rect.centerx - (BULLET_SIZE // 2),
                                          player_rect.centery, "DOWN"))
                elif player_direction == "LEFT":
                    bullets.append(Bullet(player_rect.centerx - BULLET_SIZE,
                                          player_rect.centery - (BULLET_SIZE // 2), "LEFT"))
                elif player_direction == "RIGHT":
                    bullets.append(Bullet(player_rect.centerx, player_rect.centery - (BULLET_SIZE // 2), "RIGHT"))
                ammo_count -= 1
                last_shot_time = current_time
    # Check for collision between player and bush
    for bush_pos in bush_positions:
        bush_rect = pygame.Rect(bush_pos[0], bush_pos[1], 50, 50)  # Assuming bush size is 50x50
        if player_rect.colliderect(bush_rect):
            slowed_by_bush = True
                
            

    # Check collision between player and ammo boxes
    for ammo_box in ammo_boxes:
        if player_rect.colliderect(ammo_box.rect):
            picked_ammo_box = True
            RELOAD_SOUND.play()
            ammo_boxes.remove(ammo_box)  # Remove the picked-up ammo box
            break  # Break out after picking up one ammo box

    # Check collision between player and enemies
    for zombie in enemies:
        if player_rect.colliderect(zombie.rect):
            # Player dies if colliding with an zombie
            if not die_sound_played:
                DIE_SOUND.play()
                die_sound_played = True  # Set the flag to True after playing the sound
            player_alive = False
            game_over = True  # Set the game over flag
    # Check collision between player and zombie2
    if zombie2 and player_rect.colliderect(zombie2.rect):
        # Player dies if colliding with an zombie
        if not die_sound_played:
            DIE_SOUND.play()
            die_sound_played = True  # Set the flag to True after playing the sound
        player_alive = False
        game_over = True  # Set the game over flag
    
    # Reloading if ammo count reaches 0
    if ammo_count <= 69 and not reloading and picked_ammo_box:
        reloading = True
        start_reload_time = pygame.time.get_ticks()

    # Reload after specified time if reloading
    if reloading:
        current_time = pygame.time.get_ticks()
        if current_time - start_reload_time > RELOAD_TIME:
            ammo_count = min(MAX_AMMO, ammo_count + 70)  # Reload 60 bullets
            reloading = False
            picked_ammo_box = False  # Reset the flag after reloading
        else:
            reload_text = True
    
    # Spawn an ammo box every 20 seconds (20,000 milliseconds)
    current_time = pygame.time.get_ticks()
    if current_time - spawn_ammo_box_time > 20000:  # Check if 1 minute has passed
        ammo_boxes.append(AmmoBox())  # Spawn an ammo box
        spawn_ammo_box_time = current_time  # Reset the timer for the next ammo box spawn

    
    # Update and draw bullets
    for bullet in bullets:
        bullet.update()
        screen.blit(bullet_image, bullet.rect)  # Draw updated bullet position

    # Update and draw ammo boxes
    for ammo_box in ammo_boxes:
        screen.blit(ammo_box_image, ammo_box.rect)

    # Update and draw enemies
    frame_counter += 1
    if frame_counter >= frame_duration:
        frame_counter = 0
        current_frame += 1
        if current_frame >= len(zombie_frames_right):
            current_frame = 0

    for zombie in enemies:
        zombie.update()
        if zombie.direction == 'RIGHT':
            current_zombie_image = zombie_frames_right[current_frame]
        elif zombie.direction == 'LEFT':
            current_zombie_image = zombie_frames_left[current_frame]
        elif zombie.direction == 'UP':
            current_zombie_image = zombie_frames_up[current_frame]
        elif zombie.direction == 'DOWN':
            current_zombie_image = zombie_frames_down[current_frame]

        screen.blit(current_zombie_image, zombie.rect)



    

    # Check collision between bullet and enemies
    for bullet in bullets:
        for zombie in enemies:
            if bullet.rect.colliderect(zombie.rect):
                # Bullet hits an zombie, the zombie dies
                KILL_SOUND.play()
                enemies.remove(zombie)
                blood_pos = zombie.rect
                blood_display = True  # Trigger blood display
                blood_animation_timer = blood_animation_duration  # Set blood animation duration

                if bullet in bullets:
                    bullets.remove(bullet)  # Remove the bullet from the original list
                player_score += 10  # Increment player score by 10 when an zombie is killed
                
                if player_score <= 1000:
                    zombie_RESPAWN_AMOUNT = 1
                else:
                    zombie_RESPAWN_AMOUNT = 2
                # Respawn more enemies if an zombie is killed
                for _ in range(zombie_RESPAWN_AMOUNT):
                    enemies.append(Zombie())
                    
    if high_score >= 200:
        next_level = True

        # Check collision with zombie2
    if zombie2 and bullet.rect.colliderect(zombie2.rect):
        zombie2.hits_remaining -= 1
        KILL_SOUND.play()  # Play sound for hitting zombie2
        if bullet in bullets:
            bullets.remove(bullet)  # Remove the bullet from the original list
        if zombie2.hits_remaining <= 0:
            KILL_SOUND.play()  # Play sound for defeating zombie2
            blood_pos = zombie2.rect
            blood_display = True  # Trigger blood display
            blood_animation_timer = blood_animation_duration  # Set blood animation duration
            zombie2 = None  # Remove zombie2 after it's defeated
            player_score += 50  # Increment player score for defeating zombie2
            
    # Additional actions when the player score exceeds 100
    if player_score > 100 and not zombie2:
        zombie2 = Zombie2()  # Spawn zombie2 when the player score is above 100

    if zombie2:
        zombie2.update()
        screen.blit(zombie2_image, zombie2.rect)
    

    # Draw the player image onto the screen after the background
    screen.blit(player_image, player_rect)

    # Update blood animation display
    if blood_display:
        if blood_animation_timer > 0:
            screen.blit(blood_frames[current_blood_frame_index], blood_pos)
            blood_animation_timer -= 1
            current_blood_frame_index += 1
            if current_blood_frame_index >= len(blood_frames):
                current_blood_frame_index = 0
        else:
            blood_display = False

    # Update bush animation
    frame_bush_counter += 1
    if frame_bush_counter >= frame_bush_duration:
        frame_bush_counter = 0
        current_frame_bush += 1
        if current_frame_bush >= len(bush_frames):
            current_frame_bush = 0
    current_bush_frame = bush_frames[current_frame_bush]

    # Draw bush frame onto the screen
    for bush_pos in bush_positions:
        screen.blit(current_bush_frame, bush_pos)

    # Inside your game loop or where the player's score is updated (e.g., upon death or reaching a new high score)
    # Update high score if the player's current score surpasses the high score
    if player_score > high_score:
        high_score = player_score

    # When displaying the game screen, also display the current player score and high score
    # For instance, after rendering the player's score:
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {player_score}", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))

    # Display the score texts on the screen
    # Adjust the positions to display them at the top-middle of the screen
    score_rect = score_text.get_rect(midtop=(SCREEN_WIDTH // 2, 10))
    high_score_rect = high_score_text.get_rect(midtop=(SCREEN_WIDTH // 2, 50))

    # Blit the texts onto the screen
    screen.blit(score_text, score_rect)
    screen.blit(high_score_text, high_score_rect)

    
    # Display ammo count
    font = pygame.font.Font(None, 36)
    ammo_text = font.render(f"Ammo: {ammo_count}/{MAX_AMMO}", True, (255, 255, 255))
    screen.blit(ammo_text, (10, 10))


    # Display text if the player is slowed by a bush
    if slowed_by_bush:
        font = pygame.font.Font(None, 36)
        slow_text = font.render("Slowed by the bush!", True, (104, 33, 33))  # Red color for the text
        text_rect = slow_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(slow_text, text_rect)
        slowed_by_bush = False

    if game_over:   
        if next_level:
            font = pygame.font.Font(None, 36)
            text = font.render("You can now go to the next LEVEL", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.bottomleft = (20, screen.get_height() - 20)

            button_font = pygame.font.Font(None, 24)
            button_text = button_font.render("Next Level", True, (255, 255, 255))
            button_rect = button_text.get_rect()
            button_rect.topleft = (20, screen.get_height() - 60)

            screen.blit(text, text_rect)
            screen.blit(button_text, button_rect)

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if button_rect.collidepoint(mouse_pos) and mouse_click[0] == 1:
                pygame.quit()
                subprocess.run(["python", "player1-normal.py"])
            

            
            
    # Display reload text
    if reload_text:
        # Display reloading text
            font = pygame.font.Font(None, 36)
            reloading_text = font.render("Reloading...", True, (255, 255, 255))
            text_rect = reloading_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(reloading_text, text_rect)
            reload_text = False
    # If the game is paused, display the pause screen
    if paused:  
        screen.blit(background_image, (0, 0))  # Clear the screen with the background

        # Define button dimensions and colors
        button_width = 150
        button_height = 50
        button_color = (100, 100, 100)
        button_highlight_color = (150, 150, 150)
        text_color = (255, 255, 255)

        # Display pause text
        font = pygame.font.Font(None, 50)
        pause_text = font.render("Paused", True, (255, 255, 255))
        text_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(pause_text, text_rect)

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
        # Function to handle the menu button action
        def open_menu():
            save_high_scores()  # Save the updated high scores
            subprocess.Popen(["python", "zombie shooter.py"])  # Replace "zombie_shooter.py" with the actual file name
            pygame.quit()  # Quit the current game
            

        # Calculate button positions for centering horizontally
        button_start_y = SCREEN_HEIGHT // 2 + 50
        resume_button_x = (SCREEN_WIDTH - button_width * 2 - 20) // 2  # Gap of 20 pixels between buttons
        quit_button_x = resume_button_x + button_width + 20  # Add gap for the second button
        # Create a button for the menu
        menu_button_x = (SCREEN_WIDTH - button_width) // 2
        menu_button_y = button_start_y + button_height + 20  # Adding a gap between buttons
        
        # Create buttons for resume and quit
        resume_button = draw_button(resume_button_x, button_start_y, button_width, button_height,
                                    button_color, button_highlight_color, "Resume", 36, text_color)
        quit_button = draw_button(quit_button_x, button_start_y, button_width, button_height,
                                  button_color, button_highlight_color, "Quit", 36, text_color)
        menu_button = draw_button(menu_button_x, menu_button_y, button_width, button_height,
                                      button_color, button_highlight_color, "Menu", 36, text_color)

        # Handle button clicks on the pause screen
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
            if resume_button.collidepoint(mouse_x, mouse_y):
                paused = False  # Resume button clicked
            elif quit_button.collidepoint(mouse_x, mouse_y):
                save_high_scores()
                running = False  # Quit button clicked
            elif menu_button.collidepoint(mouse_x, mouse_y):
                open_menu()  # Menu button clicked

        pygame.display.flip()
        clock.tick(GAME_FPS)
        continue  # Skip the rest of the game loop if paused

    if game_over:
        # Additional actions upon player's collision with zombie (e.g., game over, reset, etc.)
        font = pygame.font.Font(None, 50)
        death_text = font.render("You Died", True, (255, 0, 0))  # Red color for the death text
        text_rect = death_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(death_text, text_rect)
         # Display player's score
        font = pygame.font.Font(None, 36)
        score_text_game_over = font.render(f"Your Score: {player_score}", True, (255, 255, 255))
        text_rect_score = score_text_game_over.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(score_text_game_over, text_rect_score)

        # Display restart/quit instructions
        font = pygame.font.Font(None, 36)
        restart_quit_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        text_rect_restart_quit = restart_quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(restart_quit_text, text_rect_restart_quit)

        pygame.display.flip()

        # Event handling for quitting or restarting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Q key to quit
                    save_high_scores()
                    running = False
                    break
                elif event.key == pygame.K_r:  # R key to restart
                    game_over = False
                    player_alive = True
                    player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    player_score = 0
                    ammo_count = MAX_AMMO
                    zombie2 = None 
                    last_shot_time = 0
                    zombie_RESPAWN_AMOUNT = 2
                    die_sound_played = False
                    spawn_enemies()
                    break

        clock.tick(GAME_FPS)
        continue  # Skip the rest of the game loop if game over but not quitting or restarting
    

    pygame.display.flip()
    clock.tick(GAME_FPS)

pygame.quit()
sys.exit()
