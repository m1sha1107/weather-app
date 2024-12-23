import pygame as pyg
from sys import exit
from random import randint
#initialize pyg
pyg.init()

#create window
screen = pyg.display.set_mode((800, 400))
pyg.display.set_caption('game')

#create timing clock
clock = pyg.time.Clock()

#setup for restart
game_active = True
overhead_time = 0

#create plain surface
color_surface = pyg.Surface((100, 200))
color_surface.fill('red')

#create image surface, .convert(), .convert_alpha() for good practice
sky_surface  = pyg.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pyg.image.load('graphics/ground.png').convert_alpha()
ground_rect = ground_surface.get_rect(topleft= (0, 300))

#enemy spawning
chance = 50
active_list = []

#create text surface: font.render(text, AA, color)
font = pyg.font.Font('font/Pixeltype.ttf', 50)
score_surface = font.render('score', False, 'Black')
score_rect = score_surface.get_rect(center=(400, 100))

#pyg.Rect() for rect from scratch
#player.surface
player_surf = pyg.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (100, 300))
player_gravity = 0

snail_surface = pyg.image.load('graphics/snail/snail1.png').convert_alpha()
snail_surface = pyg.transform.rotozoom(snail_surface, 0, 0.7)
snail_rect = snail_surface.get_rect(midbottom=(30, 300))


#create main loop
while True:
    #event loop
    for event in pyg.event.get():
        print(event)
        if event.type == pyg.QUIT:
            pyg.quit()
            exit()

        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_SPACE and player_rect.bottom >= ground_rect.top:
                player_gravity = -17
            if event.key == pyg.K_r:
                game_active = True
                overhead_time = pyg.time.get_ticks()
                player_rect.midbottom = (100, 300)
                snail_rect.x = 800
    if game_active:
        #screen.blit(surface, pos) -> place surface on top of screen (in this case on display surface)
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, ground_rect)

        time = int(pyg.time.get_ticks() / 1000 - overhead_time / 1000)
        score_surface = font.render(f"time: {time}", False, "Black")
        screen.blit(score_surface, (300, 10))

        screen.blit(player_surf, player_rect)
        if player_rect.left > 800: player_rect.right = 1
        if player_rect.right < 0: player_rect.left = 800

        screen.blit(snail_surface, snail_rect)
        snail_rect.left -= 2
        if snail_rect.right < 0: snail_rect.left = 800
        
        # left-right movement
        key_pos = pyg.key.get_pressed()
        if key_pos[pyg.K_LEFT]:
            player_rect.x -= 8
        if key_pos[pyg.K_RIGHT]:
            player_rect.x +=8

        #gravity
        player_gravity += 1
        player_rect.y += player_gravity

        #floor collision
        if player_rect.bottom >= ground_rect.top:
            player_rect.bottom = ground_rect.top

        #gameover condition
        if player_rect.colliderect(snail_rect):
            game_active = False
        #rect.collidepoint((x, y)) to check for point collision
        # if snail_rect.colliderect(player_rect):
        #     print("collision")

        # mouse_pos = pyg.mouse.get_pos()
        # mouse_press = pyg.mouse.get_pressed()
        # if player_rect.collidepoint(mouse_pos):
        #     if mouse_press[0]: 
        #         player_rect = player_surf.get_rect(center= mouse_pos)
    else:
        screen.fill("black")
        score_surface = font.render(f'final score: {time}', False, 'white')
        gameover_surface = font.render('game over', False, 'white')
        screen.blit(gameover_surface, gameover_surface.get_rect(center = (400, 200)))
        screen.blit(score_surface, score_surface.get_rect(center = (400, 100)))
    
    #update display with changes
    pyg.display.update()
    #indicates that mainloop cannot tick more than 60 times a second (sets max framerate)
    clock.tick(60)