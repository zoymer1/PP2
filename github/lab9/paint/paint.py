import pygame
import sys
import math

pygame.init()

# Размер экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Shapes")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLACK

# Инструменты
TOOL_SQUARE = 'square'
TOOL_RIGHT_TRI = 'right_triangle'
TOOL_EQUIL_TRI = 'equilateral_triangle'
TOOL_RHOMBUS = 'rhombus'
tool = TOOL_SQUARE

screen.fill(WHITE)
clock = pygame.time.Clock()

drawing = False
start_pos = None

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #инструмент по клавишам
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = TOOL_SQUARE
            elif event.key == pygame.K_2:
                tool = TOOL_RIGHT_TRI
            elif event.key == pygame.K_3:
                tool = TOOL_EQUIL_TRI
            elif event.key == pygame.K_4:
                tool = TOOL_RHOMBUS

        # Когда нажата кнопка мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and drawing:
            drawing = False
            end_pos = event.pos
            x1, y1 = start_pos
            x2, y2 = end_pos

            # Вычисление ширины и высоты области
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            left = min(x1, x2)
            top = min(y1, y2)

            if tool == TOOL_SQUARE:
                size = min(width, height)
                pygame.draw.rect(screen, current_color, (left, top, size, size), width=2)

            elif tool == TOOL_RIGHT_TRI:
                # Прямоугольный треугольник
                points = [(x1, y1), (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, current_color, points, width=2)

            elif tool == TOOL_EQUIL_TRI:
                # Равносторонний треугольник
                side = min(width, height)
                x_center = (x1 + x2) // 2
                y_top = min(y1, y2)
                h = int((3 ** 0.5 / 2) * side)
                points = [(x_center, y_top), (x_center - side // 2, y_top + h), (x_center + side // 2, y_top + h)]
                pygame.draw.polygon(screen, current_color, points, width=2)

            elif tool == TOOL_RHOMBUS:
                # Ромб
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                points = [(cx, cy - dy), (cx + dx, cy), (cx, cy + dy), (cx - dx, cy)]
                pygame.draw.polygon(screen, current_color, points, width=2)

    # Обновление экрана
    pygame.display.flip()

