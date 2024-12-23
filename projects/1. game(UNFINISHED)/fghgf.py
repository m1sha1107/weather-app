from time import sleep
import pygame as pyg
from sys import exit
from random import choice

#startup
pyg.init()
screen_size = (1200, 800)
screen = pyg.display.set_mode(screen_size)
clock = pyg.time.Clock()

start_point= (400, 400)
rect_generate = pyg.USEREVENT + 1
#background surface
bg_surf = pyg.Surface(screen_size)
bg_rect = bg_surf.get_rect(topleft=(0, 0))

# test_surface = pyg.Surface((150, 50))
# test_surface.fill("green")
# rect = test_surface.get_rect(center= (600, 400))

#fonts, audio etc
font = pyg.font.Font('Pixeltype.ttf', 50)

#player sprite class
class Player(pyg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pyg.Surface((25, 25))
        self.image.fill("blue")
        self.rect = self.image.get_rect(center=start_point)
        self.speed = 5

    def move(self):
        keys = pyg.key.get_pressed()
        if keys[pyg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pyg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pyg.K_UP]:
            self.rect.y -= self.speed
        if keys[pyg.K_DOWN]:
            self.rect.y += self.speed

    def update(self):
        if pyg.sprite.spritecollide(player.sprite, path_group, False):
            self.move()
        else:
            self.rect.x -= 2


player = pyg.sprite.GroupSingle()
player.add(Player())

path_surf_hor = pyg.Surface((150, 50))
path_surf_vert = pyg.Surface((50, 150))
class Path(pyg.sprite.Sprite):
    def __init__(self, rect, orient):
        super().__init__()
        if orient == "hor":
            self.image = pyg.Surface((150, 50))
        elif orient == "vert":
            self.image = pyg.Surface((50, 150))
        else:
            print("invalid orientation")
        self.image.fill("red")
        self.rect = rect
        # #poor man's switch case
        # if where == "topleft": self.rect = self.image.get_rect(topleft=coords)
        # elif where == "topright": self.rect = self.image.get_rect(topright=coords)
        # elif where == "bottomleft": self.rect = self.image.get_rect(bottomleft=coords)
        # elif where == "bottomright": self.rect = self.image.get_rect(bottomright=coords)
        # elif where == "midtop": self.rect = self.image.get_rect(midtop=coords)
        # elif where == "mibottom": self.rect = self.image.get_rect(midbottom=coords)
        # elif where == "midleft": self.rect = self.image.get_rect(midleft=coords)
        # elif where == "midright": self.rect = self.image.get_rect(midright=coords)
        # else: self.rect = self.image.get_rect(center=coords)
    
    def update(self):
        self.rect.x -= 2
        if self.rect.right < -5:
            self.kill()

path_group = pyg.sprite.Group()
#set spawn
start_rect = path_surf_hor.get_rect(center = start_point)
spawn = Path(start_rect, "hor")
path_group.add(spawn)
prev = [start_rect, "right"]

#generate next rectangle path in maze 
#there is definitely a better way to write this
def generate_rect(prev):
    global path_group
    prev_rect, prev_dir = prev
    if prev_dir == "right": 
        dir = choice(["up", "down", "right"])
        not_valid = True
        while not_valid:
            not_valid = False
            if dir == "up":
                mockrect = path_surf_vert.get_rect(bottomright=prev_rect.bottomright) #(prev_rect.right, prev_rect.bottom)
                orient = "vert"
            if dir == "down":
                mockrect = path_surf_vert.get_rect(topright=prev_rect.topright)#(prev_rect.right, prev_rect.top)
                orient = "vert"
            if dir == "right":
                mockrect = path_surf_hor.get_rect(topleft=prev_rect.topright)#(prev_rect.right, prev_rect.top)
                orient = "hor"
            if dir == "left":
                mockrect = path_surf_hor.get_rect(bottomright=prev_rect.bottomright)#(prev_rect.left, prev_rect.top)
                orient = "hor"
            #check if generated rect is valid
            if mockrect.top < 0 or mockrect.bottom > 800:
                print(f"invalid: {dir}")
                not_valid = True
                dir = choice(["up", "down", "right"])

    if prev_dir == "left":
        dir = choice(["up", "down", "left"])
        not_valid = True
        while not_valid:
            not_valid = False
            if dir == "up":
                mockrect = path_surf_vert.get_rect(bottomleft=prev_rect.bottomleft)#(prev_rect.left, prev_rect.bottom)
                orient = "vert"
            if dir == "down":
                mockrect = path_surf_vert.get_rect(topleft=prev_rect.topleft)#(prev_rect.left, prev_rect.top)
                orient = "vert"
            if dir == "left":
                mockrect = path_surf_hor.get_rect(topright=prev_rect.topleft)#(prev_rect.left, prev_rect.top)
                orient = "hor"
            #check if generated rect is valid
            if mockrect.top < 0 or mockrect.bottom > 800:
                print(f"invalid: {dir}")
                not_valid = True
                dir = choice(["up", "down", "left"])

    if prev_dir == "up":
        dir = choice(["up","down", "right",])
        not_valid = True
        while not_valid:
            not_valid = False
            if dir == "up":
                mockrect = path_surf_vert.get_rect(bottomleft=prev_rect.topleft)#(prev_rect.left, prev_rect.top)
                orient = "vert"
            if dir == "down":
                mockrect = path_surf_vert.get_rect(topleft=prev_rect.topleft)#(prev_rect.left, prev_rect.top)
                orient = "vert"
            if dir == "right":
                mockrect = path_surf_hor.get_rect(topleft=prev_rect.topleft)#(prev_rect.left, prev_rect.top)
                orient = "hor"
            if dir == "left":
                mockrect = path_surf_hor.get_rect(topright=prev_rect.topright)#(prev_rect.right, prev_rect.top)
                orient = "hor"
            #check if generated rect is valid
            if mockrect.top < 0 or mockrect.bottom > 800:
                print(f"invalid: {dir}")
                not_valid = True
                dir = choice(["up","down", "right"])
    
    if prev_dir == "down":
        dir = choice(["up", "down", "right"])
        not_valid = True
        while not_valid:
            not_valid = False
            if dir == "up":
                mockrect = path_surf_vert.get_rect(topleft=prev_rect.topleft)#(prev_rect.left, prev_rect.bottom)
                orient = "vert"
            if dir == "down":
                mockrect = path_surf_vert.get_rect(topleft=prev_rect.bottomleft)#(prev_rect.left, prev_rect.bottom)
                orient = "vert"
            if dir == "right":
                mockrect = path_surf_hor.get_rect(bottomleft=prev_rect.bottomleft)#(prev_rect.left, prev_rect.bottom)
                orient = "hor"
            if dir == "left":
                mockrect = path_surf_hor.get_rect(bottomright=prev_rect.bottomright)#(prev_rect.right, prev_rect.bottom)
                orient = "hor"
            #check if generated rect is valid
            if mockrect.top < 0 or mockrect.bottom > 800:
                print(f"invalid: {dir}")
                not_valid = True
                dir = choice(["up", "down", "right"])
    path_group.add(Path(mockrect, orient))
    print(dir)
    #sleep(2)
    return mockrect, dir
    
    
#title screen setup:
title_surface = font.render('Mazerunner', False, 'white')
title_rect =title_surface.get_rect(center=(600, 400))
screen.blit(title_surface, title_rect)
pyg.display.update()
break_outer = True
#title screen loop
while break_outer:
    break_outer = True
    for event in pyg.event.get():
        if event.type == pyg.KEYDOWN:
            break_outer = False
        if event.type == pyg.QUIT:
                pyg.quit()
                exit()
    pyg.display.update()


#main game loop
while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            exit()
        
    if prev[0].left < 1300:
        prev[0], prev[1] = generate_rect(prev)
    
    screen.blit(bg_surf, bg_rect)
    
    path_group.draw(screen)
    path_group.update()
    player.draw(screen)
    player.update()
    
    pyg.display.update()
    clock.tick(60)
