import pygame
import sys
import random, time
from pygame.locals import *

pygame.init()

# Set frame rate
FPS = pygame.time.Clock()

# Screen info
width = 597
height = 540
speed = 5
score = 0
coins_counter = 0
coin_speed = 2

# Set up the colors
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the game window
pygame.display.set_caption("Voom voom")
displaysurf = pygame.display.set_mode((width, height))
displaysurf.fill((255, 255, 255))

# Set up the font
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render("Game Over", True, white)

background = pygame.image.load("download12.jpg")
background = pygame.transform.scale(background, (width, height))  # Scale to screen dimensions

# Load crash sound
crash_sound = pygame.mixer.Sound("crash.wav")

# Setting enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car3.png")
        self.image = pygame.transform.scale(self.image, (50, 100))  # Resize to 50x100 pixels
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, width - 30), 0)


# Setting player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.tiff")
        self.image = pygame.transform.scale(self.image, (80, 100))  # Resize to 50x100 pixels
        self.rect = self.image.get_rect()
        self.rect.center = ((width / 2) - 40, height - 80)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Setting coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)
        self.value = random.choice([1, 2, 3])

    def move(self):
        self.rect.move_ip(0, coin_speed)
        if self.rect.top > height:
            self.kill()

# Initialize player and enemy
P1 = Player()
E1 = Enemy()

# Creating sprites groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Increase speed every second

# Add a new user event for spawning coins
SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 2000)  # Spawn a coin every 2 seconds


def game_over():
    # Play crash sound
    crash_sound.play()
    
    displaysurf.fill(black)
    font = pygame.font.SysFont('FreeSansBold', 40)
    text = font.render("Game Over", True, white)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    displaysurf.blit(text, text_rect)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == SPAWN_COIN:
            # Create a new coin and add it to the coins_group and all_sprites
            new_coin = Coin()
            coins_group.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurf.blit(background, (0, 0))
    scores = font_small.render("Score: " + str(score), True, black)    
    enemy_speed = font_small.render("Speed: " + str(speed), True, black)
    displaysurf.blit(enemy_speed, (10, 40))

    coins = font_small.render("Collected coins: " + str(coins_counter), True, black)
    displaysurf.blit(coins, (370, 10))

    displaysurf.blit(scores, (10, 10))

    # Move and redraw player and enemy
    for entity in all_sprites:
        displaysurf.blit(entity.image, entity.rect)
        entity.move()
    
    # Check for coins
    for coin in coins_group:
        displaysurf.blit(coin.image, coin.rect)
        coin.move()
    
    if pygame.sprite.spritecollideany(P1, coins_group):
        collected_coin = pygame.sprite.spritecollideany(P1, coins_group)
        coins_counter += collected_coin.value
        collected_coin.kill()
        if coins_counter % 10 == 0:
            speed += 1
    
    # Check for collision
    if pygame.sprite.spritecollideany(P1, enemies):
        game_over()
    pygame.display.update()
    FPS.tick(60)


