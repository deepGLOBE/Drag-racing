import pygame
import os
import sys
import random
from math import *

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

from kartinki import *


def restart():
    global player_group, road_group, grass_group, asphalt_group, camera_group,player,start_group
    player_group = pygame.sprite.Group()
    road_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()
    camera_group = pygame.sprite.Group()
    asphalt_group = pygame.sprite.Group()
    start_group = pygame.sprite.Group()
    player = Player(player_image, (50,50))
    player_group.add(player)

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

    player_group.draw(sc)
    player_group.update()


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

class Asphalt(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.speed = 1



    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x += self.speed
            if self.rect.right > WIDTH/2 + 500:
                self.rect.right = WIDTH/2 + 500
                camera_group.update(-self.speed)

        elif key[pygame.K_a]:
            self.rect.x -= self.speed
            if self.rect.right < WIDTH/2 - 500:
                self.rect.right = WIDTH/2 - 500
                camera_group.update(self.speed)

        if key[pygame.K_1]:
            self.speed = 3
        elif key[pygame.K_2]:
            self.speed = 5
        elif key[pygame.K_3]:
            self.speed = 7
        elif key[pygame.K_4]:
            self.speed = 12

restart()
drawmaps('Drag.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    gamelvl()
    clock.tick(FPS)