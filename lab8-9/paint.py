import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Tool")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Drawing variables
drawing = False
last_pos = (0, 0)
color = BLACK
brush_size = 5
current_tool = "pen"
screen.fill(WHITE)

# Tools
RECTANGLE = "rectangle"
CIRCLE = "circle"
ERASER = "eraser"
SQUARE = "square"
RIGHT_TRIANGLE = "right_triangle"
EQUILATERAL_TRIANGLE = "equilateral_triangle"
RHOMBUS = "rhombus"

def draw_rect(start, end):
    pygame.draw.rect(screen, color, (start[0], start[1], end[0]-start[0], end[1]-start[1]), brush_size)

def draw_circle(start, end):
    radius = int(math.hypot(end[0]-start[0], end[1]-start[1]))
    pygame.draw.circle(screen, color, start, radius, brush_size)

def draw_square(start, end):
    side = max(abs(end[0]-start[0]), abs(end[1]-start[1]))
    pygame.draw.rect(screen, color, (start[0], start[1], side, side), brush_size)

def draw_right_triangle(start, end):
    points = [start, (end[0], start[1]), (start[0], end[1])]
    pygame.draw.polygon(screen, color, points, brush_size)

def draw_equilateral_triangle(start, end):
    side = math.hypot(end[0]-start[0], end[1]-start[1])
    height = side * math.sqrt(3) / 2
    points = [start, end, (start[0] + (end[0]-start[0])/2, start[1] - height)]
    pygame.draw.polygon(screen, color, points, brush_size)

def draw_rhombus(start, end):
    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2
    points = [
        (mid_x, start[1]),
        (end[0], mid_y),
        (mid_x, end[1]),
        (start[0], mid_y)
    ]
    pygame.draw.polygon(screen, color, points, brush_size)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        
        if event.type == pygame.MOUSEMOTION and drawing:
            if current_tool == ERASER:
                pygame.draw.circle(screen, WHITE, event.pos, brush_size*2)
        
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            
            if current_tool == RECTANGLE:
                draw_rect(last_pos, end_pos)
            elif current_tool == CIRCLE:
                draw_circle(last_pos, end_pos)
            elif current_tool == SQUARE:
                draw_square(last_pos, end_pos)
            elif current_tool == RIGHT_TRIANGLE:
                draw_right_triangle(last_pos, end_pos)
            elif current_tool == EQUILATERAL_TRIANGLE:
                draw_equilateral_triangle(last_pos, end_pos)
            elif current_tool == RHOMBUS:
                draw_rhombus(last_pos, end_pos)
        
        if event.type == pygame.KEYDOWN:
            # Tool selection
            if event.key == pygame.K_r:
                current_tool = RECTANGLE
            elif event.key == pygame.K_c:
                current_tool = CIRCLE
            elif event.key == pygame.K_e:
                current_tool = ERASER
            elif event.key == pygame.K_s:
                current_tool = SQUARE
            elif event.key == pygame.K_t:
                current_tool = RIGHT_TRIANGLE
            elif event.key == pygame.K_q:
                current_tool = EQUILATERAL_TRIANGLE
            elif event.key == pygame.K_h:
                current_tool = RHOMBUS
            
            # Color selection
            if event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE
            elif event.key == pygame.K_5:
                color = YELLOW
    
    # Draw color palette
    color_box_size = 40
    pygame.draw.rect(screen, BLACK, (0, HEIGHT-50, color_box_size, 50))
    pygame.draw.rect(screen, RED, (color_box_size, HEIGHT-50, color_box_size, 50))
    pygame.draw.rect(screen, GREEN, (color_box_size*2, HEIGHT-50, color_box_size, 50))
    pygame.draw.rect(screen, BLUE, (color_box_size*3, HEIGHT-50, color_box_size, 50))
    pygame.draw.rect(screen, YELLOW, (color_box_size*4, HEIGHT-50, color_box_size, 50))
    
    pygame.display.flip()

pygame.quit()