import pygame
import sys
import time
import math


WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BALL_RADIUS = 25

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab 7 - Clock with Center Image")
clock = pygame.time.Clock()

clock_img = pygame.image.load("mickey_clock.jpg")
clock_img = pygame.transform.scale(clock_img, (300, 300))

center_img = pygame.image.load("mickey_face.png")
center_img = pygame.transform.scale(center_img, (100, 100))

clock_center = (WIDTH // 2, HEIGHT // 3)

music_files = ["track1.mp3", "track2.mp3"]
music_index = 0
pygame.mixer.init()

def load_and_play(index):
    if 0 <= index < len(music_files):
        pygame.mixer.music.load(music_files[index])
        pygame.mixer.music.play()

def draw_hand(center, angle_deg, length, color, width):
    angle_rad = math.radians(angle_deg)
    end_x = center[0] + length * math.sin(angle_rad)
    end_y = center[1] - length * math.cos(angle_rad)
    pygame.draw.line(screen, color, center, (end_x, end_y), width)
    pygame.draw.circle(screen, color, (int(end_x), int(end_y)), width + 2)

def draw_clock_with_hands():
    clock_rect = clock_img.get_rect(center=clock_center)
    screen.blit(clock_img, clock_rect)

    center_rect = center_img.get_rect(center=clock_center)
    screen.blit(center_img, center_rect)

    now = time.localtime()
    minutes = now.tm_min
    seconds = now.tm_sec

    draw_hand(clock_center, minutes * 6, 55, BLACK, 6)
    draw_hand(clock_center, seconds * 6, 70, RED, 3)

ball_x, ball_y = WIDTH // 2, HEIGHT - 100

running = True
load_and_play(music_index)

while running:
    screen.fill(WHITE)
    draw_clock_with_hands()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_n:
                music_index = (music_index + 1) % len(music_files)
                load_and_play(music_index)
            elif event.key == pygame.K_b:
                music_index = (music_index - 1) % len(music_files)
                load_and_play(music_index)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x - BALL_RADIUS - 10 > 0:
        ball_x -= 10
    if keys[pygame.K_RIGHT] and ball_x + BALL_RADIUS + 10 < WIDTH:
        ball_x += 10
    if keys[pygame.K_UP] and ball_y - BALL_RADIUS - 10 > 0:
        ball_y -= 10
    if keys[pygame.K_DOWN] and ball_y + BALL_RADIUS + 10 < HEIGHT:
        ball_y += 10

    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()