import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = {
    '1': (255, 0, 0),    # Red
    '2': (0, 255, 0),    # Green
    '3': (0, 0, 255),    # Blue
    '4': (255, 255, 0),  # Yellow
    '5': (0, 0, 0),      # Black
}
current_color = BLACK
bg_color = WHITE

# Tools
TOOL_BRUSH = 'brush'
TOOL_RECT = 'rectangle'
TOOL_CIRCLE = 'circle'
TOOL_ERASER = 'eraser'
tool = TOOL_BRUSH
radius = 5

clock = pygame.time.Clock()
screen.fill(bg_color)

drawing = False
start_pos = None

def draw_ui():
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 30))
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Tool: {tool.capitalize()} | Press 1-5 to change color | E: Eraser | B: Brush | R: Rect | C: Circle", True, BLACK)
    screen.blit(text, (10, 5))

while True:
    clock.tick(60)
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Tool selection
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = TOOL_BRUSH
            elif event.key == pygame.K_r:
                tool = TOOL_RECT
            elif event.key == pygame.K_c:
                tool = TOOL_CIRCLE
            elif event.key == pygame.K_e:
                tool = TOOL_ERASER
            elif event.unicode in colors:
                current_color = colors[event.unicode]

        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            if tool == TOOL_BRUSH or tool == TOOL_ERASER:
                color = bg_color if tool == TOOL_ERASER else current_color
                pygame.draw.circle(screen, color, event.pos, radius)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == TOOL_BRUSH or tool == TOOL_ERASER:
                color = bg_color if tool == TOOL_ERASER else current_color
                pygame.draw.circle(screen, color, event.pos, radius)

        elif event.type == pygame.MOUSEBUTTONUP and drawing:
            drawing = False
            end_pos = event.pos
            if tool == TOOL_RECT:
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, width=2)
            elif tool == TOOL_CIRCLE:
                center = ((start_pos[0]+end_pos[0])//2, (start_pos[1]+end_pos[1])//2)
                radius_circ = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5 / 2)
                pygame.draw.circle(screen, current_color, center, radius_circ, width=2)

    pygame.display.flip()
