import pygame
from pygame.locals import *
import random
import sys
import time

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

SPEED_INCREASE_THRESHOLD = 10

COIN_GENERATION_WEIGHTS = {
    "gold": 10,
    "silver": 20,
    "bronze": 30
}

font_small = pygame.font.SysFont("Verdana", 20)
game_over = pygame.font.SysFont("Verdana", 40).render("Game Over", True, BLACK)

background = pygame.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\pp2\cars\road.png")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

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
            if self.coins_collected % SPEED_INCREASE_THRESHOLD == 0:
                for enemy in enemies:
                    enemy.speedy += 1

class Red(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\pp2\cars\red.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speedy = SPEED

    def move(self):
        self.rect.move_ip(0, self.speedy)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_type):
        super().__init__()
        self.coin_type = coin_type
        if self.coin_type == "gold":
            self.image = pygame.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\pp2\cars\gold.png")
        elif self.coin_type == "silver":
            self.image = pygame.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\pp2\cars\silver.png")
        elif self.coin_type == "bronze":
            self.image = pygame.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\pp2\cars\bronze.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -50)
        self.speedy = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def reset(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -50)
        self.speedy = random.randint(5, 10)

coins_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Blue()
E1 = Red()
enemies.add(E1)
all_sprites.add(E1)
all_sprites.add(P1)

def display_game_over(score):
    game_over_surface = game_over.render('Your Score is : ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

game_over_flag = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if not game_over_flag:
        if len(coins_group) < 5:
            random_coin = random.choices(list(COIN_GENERATION_WEIGHTS.keys()), weights=list(COIN_GENERATION_WEIGHTS.values()))[0]
            new_coin = Coin(random_coin)
            coins_group.add(new_coin)
            all_sprites.add(new_coin)

        for coin in coins_group:
            coin.update()  
        screen.blit(background, (0, 0))
        scores = font_small.render(f"Coins: {P1.coins_collected}", True, BLACK)
        screen.blit(scores, (SCREEN_WIDTH - 120, 10))
        all_sprites.draw(screen)
        for entity in all_sprites:
            if isinstance(entity, Red):
                entity.move()
        if pygame.sprite.spritecollideany(P1, enemies):
            screen.fill(RED)
            screen.blit(game_over, (30, 250))
            game_over_flag = True
        P1.update()
        if pygame.sprite.spritecollideany(P1, enemies):
            screen.fill(WHITE)
            display_game_over(P1.coins_collected)
    pygame.display.flip()
    FramePerSec.tick(FPS)

    if game_over_flag:
        pygame.time.wait(2000)  
        pygame.quit()
        sys.exit()
