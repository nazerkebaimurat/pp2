import pygame
import time
import random

pygame.init()

snake_speed = 15
screen_x = 600
screen_y = 400
block_size = 10  
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
orange = pygame.Color(255, 165, 0)
yellow = pygame.Color(255, 255, 0)

fruit_colors = {
    'apple': green,
    'banana': yellow,
    'orange': orange
}
food_weights = {
    'apple': 10,
    'banana': 20,
    'orange': 30
}

pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((screen_x, screen_y))
fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
foods = []

score = 0

class Food(pygame.sprite.Sprite):
    def __init__(self, food_type):
        super().__init__()
        self.food_type = food_type
        self.image = pygame.Surface((block_size, block_size))
        self.image.fill(fruit_colors[self.food_type])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_x - self.rect.width)
        self.rect.y = random.randint(0, screen_y - self.rect.height)
    def reset_position(self):
        self.rect.x = random.randint(0, screen_x - self.rect.width)
        self.rect.y = random.randint(0, screen_y - self.rect.height)

def show_score(color, font, size):
    score_font = pygame.font.Font(None, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    screen.blit(score_surface, (10, 10))

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_x / 2, screen_y / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def generate_food():
    food_type = random.choices(list(food_weights.keys()), weights=list(food_weights.values()))[0]
    return Food(food_type)
def draw_food():
    for food in foods:
        screen.blit(food.image, food.rect)
direction = 'RIGHT'

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'

    if direction == 'UP':
        snake_position[1] -= block_size
    if direction == 'DOWN':
        snake_position[1] += block_size
    if direction == 'LEFT':
        snake_position[0] -= block_size
    if direction == 'RIGHT':
        snake_position[0] += block_size

    snake_rect = pygame.Rect(snake_position[0], snake_position[1], block_size, block_size)

    for food in foods:
        if snake_rect.colliderect(food.rect):
            score += food_weights[food.food_type]
            food.reset_position()
            snake_body.append(list(snake_body[-1]))  
            break 

    snake_body.insert(0, list(snake_position))
    snake_body.pop()

    if len(foods) < 3:
        foods.append(generate_food())

    screen.fill(black)

    for pos in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], block_size, block_size))

    draw_food()

    if snake_position[0] < 0 or snake_position[0] >= screen_x:
        game_over()
    if snake_position[1] < 0 or snake_position[1] >= screen_y:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(white, 'times new roman', 20)
    pygame.display.update()

    fps.tick(snake_speed)
