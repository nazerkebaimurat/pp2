import pygame 
import sys
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
PINK = (255, 255, 255)
WHITE = (255, 0, 0)
circle_radius = 25
circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT // 2

screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("ball")
clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)
    pygame.draw.circle(screen, PINK, circle_radius, (circle_x, circle_y))

for event in pygame.event.get():
    if event.type == pygame.QUITE:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            circle_y = max(circle_y - 20, circle_radius)
        elif event.key == pygame.K_DOWN:
            circle_y = min(circle_y + 20, SCREEN_HEIGHT - circle_radius)
        elif event.key == pygame.K_LEFT:
            circle_x = max(circle_x - 20, circle_radius)
        elif event.key == pygame.K_RIGHT:
            circle_x = min(circle_x + 20, SCREEN_WIDTH - circle_radius)
pygame.display.flip()
clock.tick(30)
    

