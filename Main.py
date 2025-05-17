import pygame
import os
import sys
import random
from math import *
import math
from Tools.demo.sortvisu import steps
import webbrowser



pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60

gamelvl_ = "menu"
mapSelect = "Drag"
# mapSelect = "drag2"

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()




from pygame.camera import Camera
font = pygame.font.SysFont('aria',40)
from kartinki import *








def restart():
    global player_group, road_group, grass_group, asphalt_group, camera_group,player,start_group,enemy_group, camera, speedMetr,speedMetr2, button_group
    camera = 0
    player_group = pygame.sprite.Group()
    road_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()
    camera_group = pygame.sprite.Group()
    asphalt_group = pygame.sprite.Group()
    start_group = pygame.sprite.Group()
    player = Player(player_image, (300,85))
    player_group.add(player)
    enemy_group = pygame.sprite.Group()
    enemy = Enemy(enemy_image, (300, 250))
    enemy_group.add(enemy)
    camera_group.add(enemy)
    speedMetr = Circle(sc, 0, 1, 250, 710, 695, 100)
    speedMetr2 = Circle(sc, 0, 1, 250, 410, 695, 100)
    button_group = pygame.sprite.Group()

    button_start = Button(startbutton_image, (500,500), 'game')
    button_group.add(button_start)
    button_exit = Button(exitbutton_image, (500, 700), 'exit')
    button_group.add(button_exit)
    button_buy = Button(buybutton_image, (500, 600), 'buy')
    button_group.add(button_buy)
    button_option = Button(optionbutton_image, (500, 400), 'option')
    button_group.add(button_option)



def startmenu():
    sc.blit(startfon_image,(0,0))
    button_group.draw(sc)
    button_group.update()

    pygame.display.update()



def gamelvl():
    sc.blit(fon_image,(0,0))
    sc.blit(taxmetr_image, (300,600))
    sc.blit(speedmetr_image, (600, 600))
    road_group.draw(sc)
    road_group.update(0)
    asphalt_group.draw(sc)
    asphalt_group.update(0)
    grass_group.draw(sc)
    grass_group.update(0)
    start_group.draw(sc)
    start_group.update(0)
    enemy_group.draw(sc)
    enemy_group.update(0)
    player_group.draw(sc)
    player_group.update()

    speedMetr.render()
    speedMetr2.render()
    text_font = font.render(f'скорость {player.speed}', True, 'white')
    sc.blit(text_font, (600, 600))
    pygame.display.update()


def drawmaps(nameFile):
    maps = []
    source = "karta/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 5):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])

    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == '1':
                grass = Grass(grass_image, pos)
                grass_group.add(grass)
                camera_group.add(grass)
            elif maps[i][j] == '2':
                road = Road(road_image, pos)
                road_group.add(road)

                camera_group.add(road)
            elif maps[i][j] == '3':
                asphalt = Asphalt(asphalt_image, pos)
                asphalt_group.add(asphalt)
                camera_group.add(asphalt)
            elif maps[i][j] == '4':
                start = Start(start_image, pos)
                start_group.add(start)
                camera_group.add(start)


class Button(pygame.sprite.Sprite):
    def __init__(self,image,pos,next_lvl):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.next_lvl = next_lvl


    def update(self):
        global gamelvl_
        click = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.left < click[0] < self.rect.right and self.rect.top < click[1] < self.rect.bottom:
                gamelvl_ = self.next_lvl

        if pygame.mouse.get_pressed()[0]:
            if self.rect.left < click[0] < self.rect.right and self.rect.top < click[1] < self.rect.bottom:
                if self.next_lvl == 'buy':
                    webbrowser.open('https://www.tiktok.com/ru-RU/', new=0)
                gamelvl_ = self.next_lvl
                if gamelvl_ == 'game':
                    restart()
                    drawmaps(mapSelect + ".txt")






class Road(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step




class Grass(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step

class Start(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Circle:
    def __init__(self, surface, arg, maxArg, a, pos_x, pos_y, r, color=(255, 0, 0)):
        self.surface = surface
        self.arg = arg
        self.maxArg = maxArg
        self.a = a
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.r = r
        self.color = color

    def render(self):
        rad = math.radians(self.a)
        delta_rad = (rad - math.pi) / 2
        rad_arg = rad / self.maxArg * self.arg - delta_rad
        pygame.draw.line(self.surface, self.color, (self.pos_x, self.pos_y), (self.r * -math.cos(rad_arg) + self.pos_x, self.r * -math.sin(rad_arg) + self.pos_y), 3)





class Asphalt(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Enemy(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.position = 0
        self.speed = 4


    def update(self, step):
        self.position += self.speed
        self.rect.x += self.speed + step


class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.position = 0
        self.maxSpeed = 0
        self.speed = 0
        self.acceleration = 1
        self.breaking = 1


    def move(self):
        self.rect.x += self.speed / 10
        self.position += self.speed / 10

    def update(self):
        global FPS
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.speed = min(self.speed + self.acceleration, self.maxSpeed)
        elif self.speed > 0:
            self.speed = max(self.speed - self.breaking, 0)




        elif key[pygame.K_a]:
            self.speed = max(self.speed - self.acceleration, -round(self.maxSpeed / 1.5))
        elif self.speed < 0:
           self.speed = min(self.speed + self.breaking, 0)

        self.move()
        if self.rect.right > WIDTH / 2 + 500:
            self.rect.right = WIDTH / 2 + 500
            camera_group.update(-self.speed // 10)
        if self.rect.right < WIDTH / 2 - 500:
            print(123)
            self.rect.right = WIDTH / 2 - 500
            camera_group.update(-self.speed // 10)

        if key[pygame.K_9]:
            FPS = 10

        if key[pygame.K_1]:
            self.maxSpeed = 40
        elif key[pygame.K_2]:
            self.maxSpeed = 60
        elif key[pygame.K_3]:
            self.maxSpeed = 80
        elif key[pygame.K_4]:
            self.maxSpeed = 120
        elif key[pygame.K_5]:
            self.maxSpeed = 180
        elif key[pygame.K_6]:
            self.maxSpeed = 250
        elif key[pygame.K_7]:
            self.maxSpeed = 300



        speedMetr.maxArg = 240
        speedMetr.arg = abs(self.speed)
        speedMetr2.maxArg = max(self.maxSpeed, 1)
        speedMetr2.arg = abs(self.speed)

restart()
while True:
    print(gamelvl_)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if gamelvl_ == 'menu':
        startmenu()
    elif gamelvl_ == 'game':
        gamelvl()
    elif gamelvl_ == 'exit':
        pygame.quit()
        sys.exit()
    elif gamelvl_ == "option":
        mapSelect = "drag2"

        startmenu()
    clock.tick(FPS)