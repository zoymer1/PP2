import pygame
import random

pygame.init()

# Размер окна
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Precise Collision")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

# Загрузка изображений
road = pygame.image.load("road.png")
road = pygame.transform.scale(road, (WIDTH, HEIGHT))

player_car = pygame.image.load("car.png")
player_car = pygame.transform.scale(player_car, (80, 160))

enemy_car = pygame.image.load("enemy.png")
enemy_car = pygame.transform.scale(enemy_car, (80, 160))

coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Позиция игрока
player_x = WIDTH // 2 - 40
player_y = HEIGHT - 180
player_speed = 5

# Настройки
COIN_VALUES = [1, 3, 5]
COINS_FOR_SPEED_UP = 10

font_small = pygame.font.SysFont("Arial", 18)
font = pygame.font.SysFont("Arial", 24)
font_big = pygame.font.SysFont("Arial", 48)

# Класс монеты
class Coin:
    def __init__(self):
        self.x = random.randint(40, WIDTH - 40)
        self.y = -30
        self.speed = 5
        self.value = random.choice(COIN_VALUES)

    def draw(self, surface):
        surface.blit(coin_img, (self.x, self.y))
        value_text = font_small.render(str(self.value), True, BLACK)
        surface.blit(value_text, (self.x + 8, self.y + 5))

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > HEIGHT

    def collide(self, rect):
        coin_rect = pygame.Rect(self.x, self.y, 30, 30)
        return coin_rect.colliderect(rect)

#Враг
class Enemy:
    def __init__(self):
        self.x = random.randint(40, WIDTH - 80)
        self.y = -160
        self.speed = 5

    def draw(self, surface):
        surface.blit(enemy_car, (self.x, self.y))

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = -160
            self.x = random.randint(40, WIDTH - 80)

    def increase_speed(self):
        self.speed += 1

    def get_rect(self):
        rect = enemy_car.get_rect(topleft=(self.x, self.y))
        rect.inflate_ip(-45, -80)
        return rect

# Инициализация
coins = []
coin_timer = 0
collected_coins = 0
enemy = Enemy()
game_over = False

# Игровой цикл
running = True
while running:
    clock.tick(FPS)
    win.blit(road, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Управление игроком
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 80:
            player_x += player_speed

        player_rect = player_car.get_rect(topleft=(player_x, player_y))
        player_rect.inflate_ip(-45, -80)

        # Монеты
        for coin in coins[:]:
            coin.move()
            if coin.collide(player_rect):
                collected_coins += coin.value
                coins.remove(coin)
                if collected_coins % COINS_FOR_SPEED_UP == 0:
                    enemy.increase_speed()
            elif coin.off_screen():
                coins.remove(coin)

        #Создание новых монет
        coin_timer += 1
        if coin_timer >= 60:
            coins.append(Coin())
            coin_timer = 0

        #Движение врага
        enemy.move()
        if player_rect.colliderect(enemy.get_rect()):
            game_over = True

        #Отрисовка объектов
        enemy.draw(win)
        win.blit(player_car, (player_x, player_y))
        for coin in coins:
            coin.draw(win)

        #Счёт
        score_text = font.render(f"Coins: {collected_coins}", True, BLACK)
        win.blit(score_text, (WIDTH - 150, 10))

    else:
        #End
        over_text = font_big.render("GAME OVER", True, (200, 0, 0))
        win.blit(over_text, (WIDTH // 2 - 140, HEIGHT // 2 - 40))

    pygame.display.update()

    # Завершение
    if game_over:
        pygame.time.delay(2000)
        running = False

pygame.quit()