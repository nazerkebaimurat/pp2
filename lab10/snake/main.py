import psycopg2
from config import host, user, password, db_name, port
import pygame
import time
import random

pygame.init()

snake_speed = 15

screen_x = 600
screen_y = 400

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((screen_x, screen_y))

fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_position = [random.randrange(1, (screen_x//10)) * 10,
                  random.randrange(1, (screen_y//10)) * 10]

fruit_spawn = True
direction = 'RIGHT'
change_to = direction

score = 0

def create_tables():
    """Create User and User_Score tables"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_score (
            score_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            level INTEGER NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        """
    )
conn = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name,
    port = port
)
conn.autocommit = True
cursor = conn.cursor()

def get_username(screen):
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(200, 200, 140, 32)
    color_inactive = pygame.Color('red')
    color_active = pygame.Color('blue')
    color = color_inactive
    active = False
    username = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return username
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(username, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        pygame.time.Clock().tick(30)

def show_score(choice, color, font, size):
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

def main():
    create_tables()
    username = get_username(screen)
    print("Username entered:", username)
if __name__ == "__main__":
        main()

def save_state(username, score):
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    cursor = conn.cursor()

    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user_id = cursor.fetchone()
    if user_id:
        user_id = user_id[0]
        cursor.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, 1, score))
        print("Score saved successfully!")
    else:
        print("User does not exist in the database.")

    cursor.close()
    conn.commit()
    conn.close()
while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_p:
                    save_state(user, score)

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))

        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [(random.randrange(1, screen_x//10)) * 10, 
                              (random.randrange(1, screen_y//10)) * 10]
        fruit_spawn = True
        screen.fill(black)

        for pos in snake_body:
            pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(screen, green, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > screen_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > screen_y - 10:
            game_over()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        pygame.display.update()
        show_score(white, 'times new roman', 20)
        fps.tick(snake_speed)

def save_state(username, score):
    conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port = port
        )
    cursor = conn.cursor()

    cursor.execute("SELECT user_id FROM users WHERE username = %s", (user,))
    user_id = cursor.fetchone()
    if user_id:
            user_id = user_id[0]
            cursor.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, 1, score))
            print("Score saved successfully!")
    else:
            print("User does not exist in the database.")

    cursor.close()
    conn.commit()
    conn.close()