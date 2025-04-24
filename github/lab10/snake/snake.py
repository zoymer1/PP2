import pygame
import random
import sys
import time
import mysql.connector

def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Oitel.arni2004",
        database="Snake_DB"
    )

def get_or_create_user(username):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        conn.commit()
        user_id = cursor.lastrowid
    else:
        user_id = user[0]
    conn.close()
    return user_id

def save_game(user_id, score, level, snake, direction):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM user_score WHERE user_id = %s", (user_id,))
    exists = cursor.fetchone()
    snake_str = str(snake)
    direction_str = str(direction)
    if exists:
        cursor.execute("UPDATE user_score SET score=%s, level=%s, snake=%s, direction=%s WHERE user_id=%s",
                       (score, level, snake_str, direction_str, user_id))
    else:
        cursor.execute("INSERT INTO user_score (user_id, score, level, snake, direction) VALUES (%s, %s, %s, %s, %s)",
                       (user_id, score, level, snake_str, direction_str))
    conn.commit()
    conn.close()

def load_game(user_id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT score, level, snake, direction FROM user_score WHERE user_id=%s", (user_id,))
    data = cursor.fetchone()
    conn.close()
    if data:
        return data[0], data[1], eval(data[2]), eval(data[3])
    return 0, 1, [(5, 5), (4, 5), (3, 5)], (1, 0)

pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

username = input("Enter your username: ")
user_id = get_or_create_user(username)
score, level, snake, direction = load_game(user_id)

foods_to_next_level = 5
speed = 10 + (level - 1) * 2
food = None
food_weight = 1
food_spawn_time = 0
food_lifetime = 5

def generate_food():
    global food_weight, food_spawn_time
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            food_weight = random.randint(1, 5)
            food_spawn_time = time.time()
            return pos

def draw_snake_and_food():
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0] * CELL_SIZE, block[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if food:
        color = RED if food_weight <= 2 else ORANGE
        pygame.draw.rect(screen, color, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def check_collision():
    head = snake[0]
    return head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT or head in snake[1:]

def draw_score_level():
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 130, 10))

food = generate_food()
running = True
while running:
    screen.fill(BLACK)
    draw_score_level()

    if food and (time.time() - food_spawn_time) > food_lifetime:
        food = generate_food()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game(user_id, score, level, snake, direction)
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
            elif event.key == pygame.K_p:
                paused = True
                while paused:
                    for pe in pygame.event.get():
                        if pe.type == pygame.QUIT:
                            save_game(user_id, score, level, snake, direction)
                            pygame.quit()
                            sys.exit()
                        elif pe.type == pygame.KEYDOWN and pe.key == pygame.K_p:
                            paused = False

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    if new_head == food:
        score += food_weight
        food = generate_food()
        if score // foods_to_next_level + 1 > level:
            level += 1
            speed += 2
    else:
        snake.pop()

    if check_collision():
        save_game(user_id, score, level, snake, direction)
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    draw_snake_and_food()
    pygame.display.flip()
    clock.tick(speed)
