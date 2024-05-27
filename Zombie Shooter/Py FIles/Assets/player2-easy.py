import pygame
import sys
import random
import math
import subprocess
import os

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_FPS = 60


# Initialize Pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
high_scores_file = "scores/Player2_Easy_scores.txt"
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
player_image = player_image_left  # Initial player image

# Resize player images
player_image = pygame.transform.scale(player_image, (50, 50))  # Set player size
player_image_right = pygame.transform.scale(player_image_right, (50, 50))  # Set player size
player_image_left = pygame.transform.scale(player_image_left, (50, 50))  # Set player size
player_image_down = pygame.transform.scale(player_image_down, (50, 50))  # Set player size
player_image_up = pygame.transform.scale(player_image_up, (50, 50))  # Set player size
player1_alive = True
PLAYER1_SPEED = 3

player_rect = player_image.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


# Load player image and resize it to the appropriate size
player2_image_right = pygame.image.load("easy/player2_right.png")
player2_image_left = pygame.image.load("easy/player2_left.png")
player2_image_up = pygame.image.load("easy/player2_up.png")
player2_image_down = pygame.image.load("easy/player2_down.png")
player2_image = player_image_right  # Initial player image

# Resize player images
player2_image = pygame.transform.scale(player_image, (50, 50))  # Set player size
player2_image_right = pygame.transform.scale(player_image_right, (50, 50))  # Set player size
player2_image_left = pygame.transform.scale(player_image_left, (50, 50))  # Set player size
player2_image_down = pygame.transform.scale(player_image_down, (50, 50))  # Set player size
player2_image_up = pygame.transform.scale(player_image_up, (50, 50))  # Set player size
player2_alive = True
PLAYER2_SPEED = 3

player2_rect = player_image.get_rect()
player2_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)



# Initialize lists for different direction frames
zombie_frames_right = []
zombie_frames_left = []
zombie_frames_up = []
zombie_frames_down = []

# Load and resize frames for each direction
for i in range(1, 5):
    enemy_image_right = pygame.image.load(f"easy/zombie_frame/zombie_right/zombie_right({i}).png")
    enemy_image_right = pygame.transform.scale(enemy_image_right, (50, 50))
    zombie_frames_right.append(enemy_image_right)

    enemy_image_left = pygame.image.load(f"easy/zombie_frame/zombie_left/zombie_left({i}).png")
    enemy_image_left = pygame.transform.scale(enemy_image_left, (50, 50))
    zombie_frames_left.append(enemy_image_left)

    enemy_image_up = pygame.image.load(f"easy/zombie_frame/zombie_up/zombie_up({i}).png")
    enemy_image_up = pygame.transform.scale(enemy_image_up, (50, 50))
    zombie_frames_up.append(enemy_image_up)

    enemy_image_down = pygame.image.load(f"easy/zombie_frame/zombie_down/zombie_down({i}).png")
    enemy_image_down = pygame.transform.scale(enemy_image_down, (50, 50))
    zombie_frames_down.append(enemy_image_down)

# Initialize variables for animation
enemy_image = enemy_image_right  # Initial player image
current_zombie_image = zombie_frames_right[0]  # Default image (can be any initial frame)
current_frame = 0
frame_counter = 0
frame_duration = 10  # Change this value to adjust the speed of the animation

zombie_alive = True


zombie_rect = player_image.get_rect()
zombie_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)



# Load enemy2 image and resize it to the appropriate size
enemy2_image_right = pygame.image.load("easy/zombie2_right.png")
enemy2_image_left = pygame.image.load("easy/zombie2_left.png")
enemy2_image_up = pygame.image.load("easy/zombie2_up.png")
enemy2_image_down = pygame.image.load("easy/zombie2_down.png")
enemy2_image = enemy2_image_right  # Initial player image

# Resize enemy images
enemy2_image = pygame.transform.scale(enemy2_image, (50, 50))  # Set player size
enemy2_image_right = pygame.transform.scale(enemy2_image_right, (50, 50))  # Set player size
enemy2_image_left = pygame.transform.scale(enemy2_image_left, (50, 50))  # Set player size
enemy2_image_down = pygame.transform.scale(enemy2_image_down, (50, 50))  # Set player size
enemy2_image_up = pygame.transform.scale(enemy2_image_up, (50, 50))  # Set player size
enemy2_alive = True


enemy2_rect = player_image.get_rect()
enemy2_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

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


# Load revive image and resize it to match the screen size
revive_image = pygame.image.load("normal/revive.png")
revive_image = pygame.transform.scale(revive_image, (30, 30))

# revive-up attributes
revive = None  
revive_DURATION = 5000  # Duration of the revive-up in milliseconds
revive_time = pygame.time.get_ticks()  # Track the time when the revive-up appeared
revive_effect_time = None  # Track the time when the revive-up effect starts
display_revive_message = False

def revive_players(player_rect, other_player_rect, revive):
    global player1_alive, player2_alive
    remove_revive = False
    if revive and player_rect.colliderect(revive) or player2_rect.colliderect(revive):
        if not player1_alive:
            player1_alive = True
            display_revive_message = True
            remove_revive = True  # Set to True to indicate removal of the revive-up

        if not player2_alive:
            player2_alive = True
            display_revive_message = True
            remove_revive = True  # Set to True to indicate removal of the revive-up

    return remove_revive  # Return the status to remove the revive-up


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
bush_position = []
for _ in range(25):
    bush_x, bush_y = 0, 0
    bush_size = random.randint(50, 50)
    
    # Ensure bush do not spawn too close to the player or other bush
    while True:
        bush_x = random.randint(0, SCREEN_WIDTH - 50)
        bush_y = random.randint(0, SCREEN_HEIGHT - 50)
        
        # Check if the bush is too close to the players
        distance_to_player = math.sqrt((bush_x - player_rect.centerx) ** 2 + (bush_y - player_rect.centery) ** 2)
        distance_to_player2 = math.sqrt((bush_x - player_rect.centerx) ** 2 + (bush_y - player_rect.centery) ** 2)

        if distance_to_player > 100 and distance_to_player2 > 100:  # Adjust the distance threshold as needed
            # Check if the bush is too close to existing bushes
            bush_far_from_others = all(
                math.sqrt((bush_x - bx) ** 2 + (bush_y - by) ** 2) > 50 for bx, by in bush_positions
            )
            if bush_far_from_others:
                break

    bush_positions.append((bush_x, bush_y))
    bush_position.append((bush_x, bush_y, bush_size))  # Store the bush position and size


    


class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 25), random.randint(0, SCREEN_HEIGHT - 25), 25, 25)
        self.image = enemy_image_right  # Initial enemy image
        self.speed = 1  # Adjust the speed of this enemy

    def update(self):
        if not paused:
            global enemy_image  # Ensure this is the global variable defined outside the class

            # Check if players are alive
            if player1_alive or player2_alive:
                # Calculate distances between the enemy and players
                distance_to_player1 = math.sqrt((self.rect.x - player_rect.x)**2 + (self.rect.y - player_rect.y)**2)
                distance_to_player2 = math.sqrt((self.rect.x - player2_rect.x)**2 + (self.rect.y - player2_rect.y)**2)

                # Choose the nearest alive player
                if player1_alive and player2_alive:
                    nearest_player = player_rect if distance_to_player1 < distance_to_player2 else player2_rect
                elif player1_alive:
                    nearest_player = player_rect
                else:
                    nearest_player = player2_rect

                # Movement logic for the enemy towards the nearest player
                if self.rect.x < nearest_player.x:
                    self.direction = "RIGHT"
                    self.rect.x += self.speed  
                    enemy_image = enemy_image_right  # Update the enemy's image to face right
                elif self.rect.x > nearest_player.x:
                    self.direction = "LEFT"
                    self.rect.x -= self.speed  
                    enemy_image = enemy_image_left  # Update the enemy's image to face left
                if self.rect.y < nearest_player.y:
                    self.direction = "DOWN"
                    self.rect.y += self.speed 
                    enemy_image = enemy_image_down  # Update the enemy's image to face down
                elif self.rect.y > nearest_player.y:
                    self.direction = "UP"
                    self.rect.y -= self.speed
                    enemy_image = enemy_image_up  # Update the enemy's image to face up


class Enemy2:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 25), random.randint(0, SCREEN_HEIGHT - 25), 25, 25)
        self.hits_remaining = 2  # Number of hits required to defeat this enemy
        self.speed = 1  # Adjust the speed of this enemy
        self.image = enemy2_image_right  # Initial enemy image

    def update(self):
        if not paused:
            global enemy2_image  # Ensure this is the global variable defined outside the class

            # Check if players are alive
            if player1_alive or player2_alive:
                # Calculate distances between the enemy and players
                distance_to_player1 = math.sqrt((self.rect.x - player_rect.x)**2 + (self.rect.y - player_rect.y)**2)
                distance_to_player2 = math.sqrt((self.rect.x - player2_rect.x)**2 + (self.rect.y - player2_rect.y)**2)

                # Choose the nearest alive player
                if player1_alive and player2_alive:
                    nearest_player = player_rect if distance_to_player1 < distance_to_player2 else player2_rect
                elif player1_alive:
                    nearest_player = player_rect
                else:
                    nearest_player = player2_rect

                # Movement logic for the enemy towards the nearest player
                if self.rect.x < nearest_player.x:
                    self.rect.x += self.speed  
                    enemy2_image = enemy2_image_right  # Update the enemy's image to face right
                elif self.rect.x > nearest_player.x:
                    self.rect.x -= self.speed  
                    enemy2_image = enemy2_image_left  # Update the enemy's image to face left
                if self.rect.y < nearest_player.y:
                    self.rect.y += self.speed 
                    enemy2_image = enemy2_image_down  # Update the enemy's image to face down
                elif self.rect.y > nearest_player.y:
                    self.rect.y -= self.speed
                    enemy2_image = enemy2_image_up  # Update the enemy's image to face up


enemies = []
enemy2 = None  # Initialize enemy2 as None initially
ENEMY_RESPAWN_AMOUNT = 2  # Number of enemies to respawn when an enemy is killed

            
def spawn_enemies():
    global enemies
    enemies = []

    # Count existing enemies to determine how many more to spawn
    existing_enemies = len(enemies)
    if existing_enemies < 11:  # Check if there are fewer than 11 enemies
        enemies_to_spawn = min(ENEMY_RESPAWN_AMOUNT, 11 - existing_enemies)  # Calculate how many enemies to spawn without exceeding the limit
        for _ in range(enemies_to_spawn):
            new_enemy = Enemy()
            while True:
                new_enemy.rect.x = random.randint(0, SCREEN_WIDTH - 50)
                new_enemy.rect.y = random.randint(0, SCREEN_HEIGHT - 50)

                distance_to_player = math.sqrt((new_enemy.rect.x - player_rect.centerx) ** 2 + (new_enemy.rect.y - player_rect.centery) ** 2)
                distance_to_player2 = math.sqrt((new_enemy.rect.x - player_rect.centerx) ** 2 + (new_enemy.rect.y - player_rect.centery) ** 2)

                
                # Ensure enemies do not spawn too close to the player
                if distance_to_player > 150 and distance_to_player2 > 150:
                    enemies.append(new_enemy)
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






# Initialize bullets, ammo, enemy and player state
bullets = []
BULLET_SPEED = 10
BULLET_SIZE = 10

MAX_AMMO = 70
ammo_count = MAX_AMMO
ammo2_count = MAX_AMMO
RELOAD_TIME = 2000  # Time in milliseconds to reload (2 seconds in this case)
reloading = False
reloading2 = False
reload_text = False
# Add a flag to track if the player is slowed by a bush
slowed_by_bush = False
die_sound_played = False
last_shot_time = 0
last2_shot_time = 0
paused = False
next_level = False
player1_direction = "LEFT"
player2_direction = "RIGHT"
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
pygame.display.set_icon(enemy_image)


# Game Loop
running = True
game_over = False  # Flag to indicate if the game is over
player_score = 0 # Initialize player score
high_score = 0
picked_ammo_box = False #set ammo pick up to false
picked_ammo_box2 = False

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
            player_rect.x -= PLAYER1_SPEED
            player_image = player_image_left
            player1_direction = "LEFT"
        if keys[pygame.K_RIGHT]:
            player_rect.x += PLAYER1_SPEED
            player_image = player_image_right
            player1_direction = "RIGHT"
        if keys[pygame.K_UP]:
            player_rect.y -= PLAYER1_SPEED
            player_image = player_image_up
            player1_direction = "UP"
        if keys[pygame.K_DOWN]:
            player_rect.y += PLAYER1_SPEED
            player_image = player_image_down
            player1_direction = "DOWN"

        keys = pygame.key.get_pressed()
        player_prev_x, player_prev_y = player2_rect.x, player2_rect.y  # Store previous player position
        if keys[pygame.K_a]:
            player2_rect.x -= PLAYER2_SPEED
            player2_image = player2_image_left
            player2_direction = "LEFT"
        if keys[pygame.K_d]:
            player2_rect.x += PLAYER2_SPEED
            player2_image = player2_image_right
            player2_direction = "RIGHT"
        if keys[pygame.K_w]:
            player2_rect.y -= PLAYER2_SPEED
            player2_image = player2_image_up
            player2_direction = "UP"
        if keys[pygame.K_s]:
            player2_rect.y += PLAYER2_SPEED
            player2_image = player2_image_down
            player2_direction = "DOWN"

        # Ensure the player remains within the screen boundaries
        player_rect.x = max(0, min(player_rect.x, SCREEN_WIDTH - player_rect.width))
        player_rect.y = max(0, min(player_rect.y, SCREEN_HEIGHT - player_rect.height))
        # Ensure the player remains within the screen boundaries
        player2_rect.x = max(0, min(player2_rect.x, SCREEN_WIDTH - player2_rect.width))
        player2_rect.y = max(0, min(player2_rect.y, SCREEN_HEIGHT - player2_rect.height))

    # Handling bullet firing using keys obtained above and ammo count
    if keys[pygame.K_SPACE] and player1_alive and not reloading:  # Check if SPACE key is pressed and not reloading
        if ammo_count > 0:  # Check if there is ammo available
            current_time = pygame.time.get_ticks()  # Get the current time again
            if current_time - last_shot_time > 200:  # Limit shooting speed (200 milliseconds between shots)
                SHOT_SOUND.play()
                if player1_direction == "UP":
                    bullets.append(Bullet(player_rect.centerx - (BULLET_SIZE // 2),
                                          player_rect.centery - BULLET_SIZE, "UP"))
                elif player1_direction == "DOWN":
                    bullets.append(Bullet(player_rect.centerx - (BULLET_SIZE // 2),
                                          player_rect.centery, "DOWN"))
                elif player1_direction == "LEFT":
                    bullets.append(Bullet(player_rect.centerx - BULLET_SIZE,
                                          player_rect.centery - (BULLET_SIZE // 2), "LEFT"))
                elif player1_direction == "RIGHT":
                    bullets.append(Bullet(player_rect.centerx, player_rect.centery - (BULLET_SIZE // 2), "RIGHT"))
                ammo_count -= 1
                last_shot_time = current_time

   # Handling bullet firing using keys obtained above and ammo count
    if keys[pygame.K_z] and player2_alive and not reloading2:  # Check if z key is pressed and not reloading
        if ammo2_count > 0:  # Check if there is ammo available
            current_time = pygame.time.get_ticks()  # Get the current time again
            if current_time - last2_shot_time > 200:  # Limit shooting speed (200 milliseconds between shots)
                SHOT_SOUND.play()
                if player2_direction == "UP":
                    bullets.append(Bullet(player2_rect.centerx - (BULLET_SIZE // 2),
                                          player2_rect.centery - BULLET_SIZE, "UP"))
                elif player2_direction == "DOWN":
                    bullets.append(Bullet(player2_rect.centerx - (BULLET_SIZE // 2),
                                          player2_rect.centery, "DOWN"))
                elif player2_direction == "LEFT":
                    bullets.append(Bullet(player2_rect.centerx - BULLET_SIZE,
                                          player2_rect.centery - (BULLET_SIZE // 2), "LEFT"))
                elif player2_direction == "RIGHT":
                    bullets.append(Bullet(player2_rect.centerx, player2_rect.centery - (BULLET_SIZE // 2), "RIGHT"))
                ammo2_count -= 1
                last2_shot_time = current_time

    # Check collision between player and ammo boxes
    for ammo_box in ammo_boxes:
        if player_rect.colliderect(ammo_box.rect):
            picked_ammo_box = True
            RELOAD_SOUND.play()
            ammo_boxes.remove(ammo_box)  # Remove the picked-up ammo box
            break  # Break out after picking up one ammo box
    # Check collision between player2 and ammo boxes
    for ammo_box in ammo_boxes:
        if player2_rect.colliderect(ammo_box.rect):
            picked_ammo_box2 = True
            RELOAD_SOUND.play()
            ammo_boxes.remove(ammo_box)  # Remove the picked-up ammo box
            break  # Break out after picking up one ammo box
    
    # Reloading if ammo count reaches 0
    if ammo_count <= 69 and not reloading and picked_ammo_box:
        reloading = True
        start_reload_time = pygame.time.get_ticks()
    # Reloading if ammo2 count reaches 0
    if ammo2_count <= 69 and not reloading2 and picked_ammo_box2:
        reloading2 = True
        start_reload_time2 = pygame.time.get_ticks()

    # Reload after specified time if reloading
    if reloading:
        current_time = pygame.time.get_ticks()
        if current_time - start_reload_time > RELOAD_TIME:
            ammo_count = min(MAX_AMMO, ammo_count + 70)  # Reload 60 bullets
            reloading = False
            picked_ammo_box = False  # Reset the flag after reloading
        else:
            reload_text = True
            
    # Reload after specified time if reloading player2
    if reloading2:
        current_time = pygame.time.get_ticks()
        if current_time - start_reload_time2 > RELOAD_TIME:
            ammo2_count = min(MAX_AMMO, ammo2_count + 70)  # Reload 60 bullets
            reloading2 = False
            picked_ammo_box2 = False  # Reset the flag after reloading
        else:
            reload_text = True
    
    # Spawn an ammo box every 20 seconds (20,000 milliseconds)
    current_time = pygame.time.get_ticks()
    if current_time - spawn_ammo_box_time > 20000:  # Check if 1 minute has passed
        ammo_boxes.append(AmmoBox())  # Spawn an ammo box
        spawn_ammo_box_time = current_time  # Reset the timer for the next ammo box spawn
        
    #check collision to revive
    if revive:
        if revive_players(player_rect, player2_rect, revive):
            revive = None  # Remove the revive-up if indicated by the function
    
   # Generate a revive-up randomly, avoiding spawning near obstacles
    if not revive and current_time - revive_time > 60000:
        while True:
            # Randomly generate a potential revive-up position
            revive_candidate = revive_image.get_rect(center=(random.randint(50, SCREEN_WIDTH - 50),
                                                                random.randint(50, SCREEN_HEIGHT - 50)))
            # Check if the revive-up collides with any obstacle (bush)
            collides_with_bush = False
            for bush_pos in bush_position:
                bush_x, bush_y, bush_size = bush_pos
                bush_rect = pygame.Rect(bush_x, bush_y, bush_size, bush_size)
                if revive_candidate.colliderect(bush_rect):
                    collides_with_bush = True
                    break
            
            # If the potential revive-up position doesn't collide with any obstacle, set it as the revive-up position
            if not collides_with_bush:
                revive = revive_candidate
                revive_time = current_time  # Reset the timer for the next revive-up appearance
                break  # Exit the loop if a valid revive-up position is found

    # Then, in your game loop, after drawing the other game elements:
    # Draw the revive-up if it exists
    if revive:
        screen.blit(revive_image, revive)
    
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

    for enemy in enemies:
        enemy.update()
        if enemy.direction == 'RIGHT':
            current_zombie_image = zombie_frames_right[current_frame]
        elif enemy.direction == 'LEFT':
            current_zombie_image = zombie_frames_left[current_frame]
        elif enemy.direction == 'UP':
            current_zombie_image = zombie_frames_up[current_frame]
        elif enemy.direction == 'DOWN':
            current_zombie_image = zombie_frames_down[current_frame]

        screen.blit(current_zombie_image, enemy.rect)

    # Check collision between player and enemies
    for enemy in enemies:
        # Check collision between player1 and enemies
        if player_rect.colliderect(enemy.rect) and player1_alive:
            DIE_SOUND.play()
            player1_alive = False

        # Check collision between player2 and enemies
        if player2_rect.colliderect(enemy.rect) and player2_alive:
            DIE_SOUND.play()
            player2_alive = False

    if enemy2 and player_rect.colliderect(enemy2.rect) and player1_alive:
        # Player dies if colliding with an enemy
        if not die_sound_played:
            DIE_SOUND.play()
            die_sound_played = True  # Set the flag to True after playing the sound
        player1_alive = False

    if enemy2 and player2_rect.colliderect(enemy2.rect)and player2_alive:
        # Player dies if colliding with an enemy
        if not die_sound_played:
            DIE_SOUND.play()
            die_sound_played = True  # Set the flag to True after playing the sound
        player2_alive = False
        game_over = True  # Set the game over flag

    # Check collision between bullet and enemies
    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                # Bullet hits an enemy, the enemy dies
                KILL_SOUND.play()
                blood_pos = enemy.rect
                blood_display = True  # Trigger blood display
                blood_animation_timer = blood_animation_duration  # Set blood animation duration

                enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)  # Remove the bullet from the original list
                player_score += 10  # Increment player score by 10 when an enemy is killed
                if player_score <= 1000:
                    ENEMY_RESPAWN_AMOUNT = 1
                else:
                    ENEMY_RESPAWN_AMOUNT = 2
                # Respawn more enemies if an enemy is killed
                for _ in range(ENEMY_RESPAWN_AMOUNT):
                    enemies.append(Enemy())
    if high_score >= 200:
        next_level = True
        
        # Check collision with enemy2
    if enemy2 and bullet.rect.colliderect(enemy2.rect):
        enemy2.hits_remaining -= 1
        KILL_SOUND.play()  # Play sound for hitting enemy2
        if bullet in bullets:
            bullets.remove(bullet)  # Remove the bullet from the original list
        if enemy2.hits_remaining <= 0:
            KILL_SOUND.play()  # Play sound for defeating enemy2
            blood_pos = enemy2.rect
            blood_display = True  # Trigger blood display
            blood_animation_timer = blood_animation_duration  # Set blood animation duration

            enemy2 = None  # Remove enemy2 after it's defeated
            player_score += 50  # Increment player score for defeating enemy2
            
    # Additional actions when the player score exceeds 100
    if player_score > 100 and not enemy2:
        enemy2 = Enemy2()  # Spawn enemy2 when the player score is above 100

    if enemy2:
        enemy2.update()
        screen.blit(enemy2_image, enemy2.rect)
    
    # Check for collision between player and bush
    for bush_pos in bush_positions:
        bush_rect = pygame.Rect(bush_pos[0], bush_pos[1], 50, 50)  # Assuming bush size is 50x50
        if player_rect.colliderect(bush_rect) and player1_alive:
            slowed_by_bush = True
            
    # Check for collision between player2 and bush
    for bush_pos in bush_positions:
        bush_rect = pygame.Rect(bush_pos[0], bush_pos[1], 50, 50)  # Assuming bush size is 50x50
        if player2_rect.colliderect(bush_rect) and player2_alive:
            slowed_by_bush = True


    # Draw the player image onto the screen after the background
    if player1_alive:
        screen.blit(player_image, player_rect)

    # Draw the player image onto the screen after the background
    if player2_alive:
        screen.blit(player2_image, player2_rect)
        
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
    if display_revive_message:
        current_time = pygame.time.get_ticks()
        if current_time - revive_message_time < revive_DURATION:
            font = pygame.font.Font(None, 36)
            text = font.render("Reviving the Other Player", True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
            screen.blit(text, text_rect)
        else:
            display_revive_message = False  # Hide the message after the power-up duration


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

    
    # Display ammo count for player 1
    font = pygame.font.Font(None, 36)
    ammo_text = font.render(f"Ammo: {ammo_count}/{MAX_AMMO}", True, (255, 255, 255))
    screen.blit(ammo_text, (10, 10))

    # Display ammo count for player 2 on the right side
    font = pygame.font.Font(None, 36)
    ammo2_text = font.render(f"Ammo: {ammo2_count}/{MAX_AMMO}", True, (255, 255, 255))

    # Adjust the position to display ammo count for player 2 on the right side
    ammo2_x = SCREEN_WIDTH - ammo2_text.get_width() - 10  # Position from the right side with a margin of 10 pixels
    screen.blit(ammo2_text, (ammo2_x, 10))  # Displaying the ammo count for player 2 aligned to the right


    # Display player score
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(f"Score: {player_score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 50))  # Adjust the position of the score text

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


    # Display text if the player is slowed by a bush
    if slowed_by_bush:
        font = pygame.font.Font(None, 36)
        slow_text = font.render("Slowed by the bush!", True, (104, 33, 33))  # Red color for the text
        text_rect = slow_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(slow_text, text_rect)
        slowed_by_bush = False
          

    # Display reload text
    if reload_text:
        # Display reloading text
            font = pygame.font.Font(None, 36)
            reloading_text = font.render("Reloading...", True, (255, 255, 255))
            text_rect = reloading_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(reloading_text, text_rect)
            reload_text = False
            
    # Check if both players are dead
    if not player1_alive and not player2_alive:
        game_over = True

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
            save_high_scores()
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
            
        # Additional actions upon player's collision with enemy (e.g., game over, reset, etc.)
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
                    player1_alive = True
                    player2_alive = True
                    player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    player2_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    player_score = 0
                    ammo_count = MAX_AMMO
                    ammo2_count = MAX_AMMO
                    enemy2 = None 
                    last_shot_time = 0
                    last2_shot_time = 0
                    ENEMY_RESPAWN_AMOUNT = 2
                    die_sound_played = False
                    spawn_enemies()
                    break

        clock.tick(GAME_FPS)
        continue  # Skip the rest of the game loop if game over but not quitting or restarting
    

    pygame.display.flip()
    clock.tick(GAME_FPS)

pygame.quit()
sys.exit()
