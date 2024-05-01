import pygame as pg
from datetime import datetime as dt
import math

pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Micky Mouse Clock")
clock = pg.time.Clock()

micky = pg.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\clock_assets\mainclock.png")
left = pg.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\clock_assets\leftarm.png")
right = pg.image.load(r"C:\Users\rrro0\OneDrive\Рабочий стол\clock_assets\rightarm.png")

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    current_time = dt.now().time()    
    seconds_angle = -current_time.second * 6  
    minutes_angle = -current_time.minute * 6 

    rotated_left_hand = pg.transform.rotate(left, seconds_angle)
    rotated_right_hand = pg.transform.rotate(right, minutes_angle)

    screen.fill((0, 0, 0))  
    screen.blit(micky, (400 - micky.get_width() // 2, 400 - micky.get_height() // 2))
    screen.blit(rotated_left_hand, (400 - rotated_left_hand.get_width() // 2, 400 - rotated_left_hand.get_height() // 2))
    screen.blit(rotated_right_hand, (400 - rotated_right_hand.get_width() // 2, 400 - rotated_right_hand.get_height() // 2))

    pg.display.flip()
    clock.tick(60)  
pg.quit()