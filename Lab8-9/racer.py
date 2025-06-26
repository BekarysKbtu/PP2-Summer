import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

# Размеры и настройки
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Экран
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Загрузка и масштабирование изображений
player_img = pygame.transform.scale(pygame.image.load("/Users/bekaryssherman/Desktop/PP2-Summer/Lab8-9/Images/player.png"), (40, 60))
enemy_img = pygame.transform.scale(pygame.image.load("/Users/bekaryssherman/Desktop/PP2-Summer/Lab8-9/Images/enemy.png"), (40, 60))
coin_img = pygame.transform.scale(pygame.image.load("/Users/bekaryssherman/Desktop/PP2-Summer/Lab8-9/Images/coin.png"), (30, 30))
background = pygame.transform.scale(pygame.image.load("/Users/bekaryssherman/Desktop/PP2-Summer/Lab8-9/Images/AnimatedStreet.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

P1 = Player()  # Сначала создаём игрока

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        while True:
            x = random.randint(40, SCREEN_WIDTH - 40)
            y = random.randint(-300, -100)
            temp_rect = self.image.get_rect(center=(x, y))
            if not temp_rect.colliderect(P1.rect):
                self.rect = temp_rect
                break

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -100)

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -200)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -200)

# Объекты
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    # Очки
    score_text = font_small.render(f"Enemies: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (300, 10))

    # Движение и отрисовка
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        try:
            pygame.mixer.Sound("/Users/bekaryssherman/Desktop/PP2-Summer/Lab8-9/Images/crash.wav").play()
        except:
            pass  # если нет файла — пропустить
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Подбор монеты
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -200)

    pygame.display.update()
    FramePerSec.tick(FPS)
