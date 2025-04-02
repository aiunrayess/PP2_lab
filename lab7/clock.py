import pygame
import sys
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1200, 800
H_width, H_height = WIDTH // 2, HEIGHT // 2
radius = H_height - 50
# second_arrow = pygame.image.load('second_arrow.png')
# minute_arrow = pygame.image.load('minute_arrow.png')
# hour_arrow = pygame.image.load('hour_arrow.png')
radius_list = {'sec': radius - 30, 'min': radius - 57, 'hour': radius - 102, 'digit': radius - 30}
radius_ark = radius + 8 

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock12 = dict(zip(range(12), range(0, 360, 30))) #for 12 hours
clock60 = dict(zip(range(60), range(0, 360, 6))) #for 60 minutes and seconds


font = pygame.font.SysFont('Times New Roman', 60)
img = pygame.image.load('clocks.png')
img_rect = img.get_rect(center=(H_width, H_height))
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
bg_rect = bg.get_rect(topleft=(0, 0))
# surface.blit(bg, (0, 0))



def clock_position(clock_dict, clock_hand, key):
    x = H_width + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_height + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

while True:
    surface.blit(bg, (0, 0))
    surface.blit(img, img_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    img = pygame.transform.scale(img, (2 * radius, 2 * radius))
    img_rect = img.get_rect(center=(H_width, H_height))
    
    now = datetime.now()
    t = now.strftime('%H:%M:%S')
    hour, minute, second = ((now.hour % 12) * 5 + now.minute // 12) % 60, now.minute, now.second  #map(int, t.split(':'))

#draw clock
    pygame.draw.line(surface, pygame.Color((203, 153, 255)), (H_width, H_height), clock_position(clock60, hour, 'hour'), 15)
    pygame.draw.line(surface, pygame.Color((255, 153, 204)), (H_width, H_height), clock_position(clock60, minute, 'min'), 7)
    pygame.draw.line(surface, pygame.Color('gray'), (H_width, H_height), clock_position(clock60, second, 'sec'), 4)
    pygame.draw.circle(surface, pygame.Color('white'), (H_width, H_height), 8)

#digital clock
    # text = font.render(t, True, pygame.Color('lightblue'), (255, 228, 225))
    # surface.blit(text, (0, 0))

#arc
    sec_angle = -math.radians(clock60[second]) + math.pi / 2
    pygame.draw.arc(surface, pygame.Color((153, 153, 255)), (H_width - radius_ark, H_height - radius_ark, 2 * radius_ark, 2 * radius_ark), math.pi / 2, sec_angle, 8)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
# sys.exit()