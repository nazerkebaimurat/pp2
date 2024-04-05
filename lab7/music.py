import pygame
import os

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Music Player")

music_dir = r"C:\Users\rrro0\OneDrive\Рабочий стол\MyMusic"

music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
pygame.mixer.init()

def play_music(index):
    pygame.mixer.music.load(os.path.join(music_dir, music_files[index]))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def play_next(index):
    index = (index + 1) % len(music_files)
    play_music(index)
    return index

def play_previous(index):
    index = (index - 1) % len(music_files)
    play_music(index)
    return index

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

font = pygame.font.Font(None, 36)
current_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music(current_index)
            elif event.key == pygame.K_RIGHT: 
                current_index = play_next(current_index)
            elif event.key == pygame.K_LEFT:  
                current_index = play_previous(current_index)
            elif event.key == pygame.K_ESCAPE: 
                running = False

    
    screen.fill((255, 255, 255))

    status = "Playing" if pygame.mixer.music.get_busy() else "Paused"
    song_name = music_files[current_index] if music_files else "No songs found"
    draw_text(f"Status: {status}", font, (0, 0, 0), 300, 200)
    draw_text(f"Current Song: {song_name}", font, (0, 0, 0), 300, 250)
    pygame.display.flip()

pygame.quit()
