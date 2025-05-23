import pygame
import os

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music Player")

music_directory = "/Users/ainurok/Desktop/pp2_lab/lab7/musics"
os.chdir(music_directory)

music_files = [file for file in os.listdir() if file.endswith(".mp3")]

current_track = 0
paused = False

pygame.mixer.music.load(music_files[current_track])

font = pygame.font.Font(None, 24)

lol = pygame.image.load("IMG_7940.JPG")

lol = pygame.transform.scale(lol, (200, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
    
    screen.fill((255, 255, 255))
    instructions = font.render("Spacebar: Play/Pause, Left Arrow: Previous, Right Arrow: Next", True, (0, 0, 0))
    screen.blit(instructions, (10, 10))

    screen.blit(lol, (150, 100))

    pygame.display.flip()

pygame.quit()