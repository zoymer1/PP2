import pygame
import random
import sys

pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

#Шрифт для текста
font = pygame.font.SysFont("Arial", 24)

#Таймер
clock = pygame.time.Clock()

# Начальное позиция змейки
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)

#Переменные
score = 0
level = 1
foods_to_next_level = 3
speed = 10
food = None

#Генерация еды
def generate_food():
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            return pos

#Змея и еда
def draw_snake_and_food():
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0] * CELL_SIZE, block[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#Столкновение
def check_collision():
    head = snake[0]
    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
        return True
    if head in snake[1:]:
        return True
    return False

# Счёт и уровень
def draw_score_level():
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 130, 10))

# Генерация начальной еды
food = generate_food()

# Главный игровой цикл
running = True
while running:
    screen.fill(BLACK)
    draw_score_level()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Перемещение змеи
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = generate_food()
        if score % foods_to_next_level == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    if check_collision():
        pygame.quit()
        sys.exit()

    draw_snake_and_food()
    pygame.display.flip()
    clock.tick(speed)