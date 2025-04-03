import pygame
import random
import sys
import time

pygame.init()

# Параметры экрана и клеток
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

# Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Шрифт
font = pygame.font.SysFont("Arial", 24)

# Таймер
clock = pygame.time.Clock()

# Змейка
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)

# Счёт, уровень и скорость
score = 0
level = 1
foods_to_next_level = 5
speed = 10

# Еда
food = None
food_weight = 1
food_spawn_time = 0
food_lifetime = 5

#Генерация еды с весом и таймером
def generate_food():
    global food_weight, food_spawn_time
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            food_weight = random.randint(1, 5)
            food_spawn_time = time.time() 
            return pos

#Змейка и еда
def draw_snake_and_food():
    # Змейка
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0] * CELL_SIZE, block[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # Еда
    if food:
        color = RED if food_weight <= 2 else ORANGE
        pygame.draw.rect(screen, color, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#Столкновение
def check_collision():
    head = snake[0]
    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
        return True
    if head in snake[1:]:
        return True
    return False

#Счёт и уровень
def draw_score_level():
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 130, 10))

#Генерация еды
food = generate_food()

#Основной цикл
running = True
while running:
    screen.fill(BLACK)
    draw_score_level()

    #исчезновение еды
    if food and (time.time() - food_spawn_time) > food_lifetime:
        food = generate_food()

    #управление
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

    #Движение
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    #Съеденная еду
    if new_head == food:
        score += food_weight
        food = generate_food()

        #Повышение уровня
        if score // foods_to_next_level + 1 > level:
            level += 1
            speed += 2
    else:
        snake.pop()

    #Столкновение
    if check_collision():
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    #Отрисовка
    draw_snake_and_food()
    pygame.display.flip()
    clock.tick(speed)
