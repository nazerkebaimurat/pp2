import pygame
from pygame.locals import *
import random
import sys

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font_small = pygame.font.SysFont("Verdana", 20)
game_over = pygame.font.SysFont("Verdana", 40).render("Game Over", True, BLACK)

background = pygame.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\pp2\cars\road.png")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

class Red(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\pp2\cars\red.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Blue(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\pp2\cars\blue.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.coins_collected = 0
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        self.collect_coins()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def collect_coins(self):
        collided_coins = pygame.sprite.spritecollide(self, coins_group, True)
        for coin in collided_coins:
            self.coins_collected += 1

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\pp2\cars\coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  
        self.rect.y = random.randint(-100, -50)
        self.speedy = random.randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)
            self.speedy = random.randint(5, 10)


P1 = Blue()
E1 = Red()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins_group = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)

game_over_flag = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if not game_over_flag:
        if random.randint(0, 100) < 10:  
            new_coin = Coin()
            coins_group.add(new_coin)
            all_sprites.add(new_coin)

        screen.blit(background, (0, 0))
        scores = font_small.render(f"Coins: {P1.coins_collected}", True, BLACK)
        screen.blit(scores, (SCREEN_WIDTH - 120, 10))

        for entity in all_sprites:
            if isinstance(entity, Red):
                entity.move()
            screen.blit(entity.image, entity.rect)

        if pygame.sprite.spritecollideany(P1, enemies):
            screen.fill(RED)
            screen.blit(game_over, (30, 250))
            game_over_flag = True

        P1.update()

    pygame.display.flip()
    FramePerSec.tick(FPS)

    if game_over_flag:
        pygame.time.wait()  
        pygame.quit()
        sys.exit()
