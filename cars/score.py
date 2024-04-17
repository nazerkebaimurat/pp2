"""""
import pygame
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if not game_over_flag:
        if len(coins_group) < 5:
            new_coin = Coin()
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

    else:  # Moved the rendering of game over and score display outside the conditional block
        display_game_over(P1.coins_collected)

    pygame.display.flip()
    FramePerSec.tick(FPS)

    if game_over_flag:
        pygame.time.wait(2000)  
        pygame.quit()
        sys.exit()



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        def display_game_over(score):
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, 'red')
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()
"""