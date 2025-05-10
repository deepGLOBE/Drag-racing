import pygame
import os
import sys
import random
from math import *
import math
from Tools.demo.sortvisu import steps

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60



sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

from pygame.camera import Camera
font = pygame.font.SysFont('aria',40)
from kartinki import *


def restart():
    global player_group, road_group, grass_group, asphalt_group, camera_group,player,start_group,enemy_group, camera, speedMetr,speedMetr2
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
    speedMetr = Circle(sc, 0, 1, 270, 710, 695, 100)
    speedMetr2 = Circle(sc, 0, 1, 270, 410, 695, 100)








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
            if self.position < 3400:
                self.speed = min(self.speed + self.acceleration, self.maxSpeed)
        elif self.speed > 0:
            self.speed = max(self.speed - self.breaking, 0)




        elif key[pygame.K_a]:
            if self.position > -300:
                self.speed = max(self.speed - self.acceleration, -round(self.maxSpeed / 1.5))
        elif self.speed < 0:
           self.speed = min(self.speed + self.breaking, 0)

        self.move()
        if self.rect.right > WIDTH / 2 + 500:
            self.rect.right = WIDTH / 2 + 500
            camera_group.update(-self.speed / 10)
        if self.rect.right < WIDTH / 2 - 500:
            self.rect.right = WIDTH / 2 - 500
            camera_group.update(self.speed / 10)

        if key[pygame.K_9]:
            FPS = 10

        if key[pygame.K_1]:
            self.maxSpeed = 30
        elif key[pygame.K_2]:
            self.maxSpeed = 50
        elif key[pygame.K_3]:
            self.maxSpeed = 70
        elif key[pygame.K_4]:
            self.maxSpeed = 120
        elif key[pygame.K_5]:
            self.maxSpeed = 170
        elif key[pygame.K_0]:
            self.maxSpeed = 100000
        speedMetr.maxArg = 170
        speedMetr.arg = abs(self.speed)
        speedMetr2.maxArg = max(self.maxSpeed, 1)
        speedMetr2.arg = abs(self.speed)


restart()
drawmaps('Drag.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    gamelvl()
    clock.tick(FPS)