import pygame
import random

pygame.init()

#Размеры окна
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

#Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Частота обновления экрана
FPS = 60
clock = pygame.time.Clock()

#Загрузка изображений
road = pygame.image.load("road.png")
road = pygame.transform.scale(road, (WIDTH, HEIGHT))

player_car = pygame.image.load("car.png")
player_car = pygame.transform.scale(player_car, (80, 160))

coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))

#Начальная позиция игрока
player_x = WIDTH // 2 - 40
player_y = HEIGHT - 180
player_speed = 5

#Монеты
class Coin:
    def __init__(self):
        self.x = random.randint(40, WIDTH - 40)
        self.y = -30
        self.speed = 5

    def draw(self, surface):
        surface.blit(coin_img, (self.x, self.y))

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > HEIGHT

    def collide(self, rect):
        coin_rect = pygame.Rect(self.x, self.y, 30, 30)
        return coin_rect.colliderect(rect)

#Монеты и счёт
coins = []
coin_timer = 0
collected_coins = 0

#Очки
font = pygame.font.SysFont("Arial", 24)

#Игровой цикл
running = True
while running:
    clock.tick(FPS)
    
    win.blit(road, (0, 0))

    #События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 80:  # учёт новой ширины
        player_x += player_speed

    #Прямоугольник игрока
    player_rect = pygame.Rect(player_x, player_y, 80, 160)

    #Монеты — движение и столкновение
    for coin in coins[:]:
        coin.move()
        if coin.collide(player_rect):
            coins.remove(coin)
            collected_coins += 1
        elif coin.off_screen():
            coins.remove(coin)

    #Добавление монет
    coin_timer += 1
    if coin_timer >= 60:
        coins.append(Coin())
        coin_timer = 0

    #Отображение игрока
    win.blit(player_car, (player_x, player_y))

    #Отображение монет
    for coin in coins:
        coin.draw(win)

    #Счётчик
    text = font.render(f"Coins: {collected_coins}", True, BLACK)
    win.blit(text, (WIDTH - 130, 10))

    pygame.display.update()

pygame.quit()