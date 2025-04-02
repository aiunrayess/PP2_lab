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
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Initialize player and enemy
P1 = Player()
E1 = Enemy()

#Creating sprites groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Increase speed every second


def game_over():
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
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurf.blit(background, (0, 0))
    scores = font_small.render("Score: " + str(score), True, black)    
    enemy_speed = font_small.render("Speed: " + str(speed), True, black)
    displaysurf.blit(enemy_speed, (10, 40))
    displaysurf.blit(scores, (10, 10))


    #Move and redraw player and enemy
    for entity in all_sprites:
        displaysurf.blit(entity.image, entity.rect)
        entity.move()
    
    #Check for collision
    if pygame.sprite.spritecollideany(P1, enemies):
        game_over()
    pygame.display.update()
    FPS.tick(60)


