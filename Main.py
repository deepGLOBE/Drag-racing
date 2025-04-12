import pygame
import os
import sys
import random
from math import *

from pygame.camera import Camera

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



def restart():
    global player_group, road_group, grass_group, asphalt_group, camera_group
    player_group = pygame.sprite.Group()
    road_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()
    camera_group = SuperGroup()
    asphalt_group = pygame.sprite.Group()




def gamelvl():
    sc.fill('dimgray')
    player_group.draw(sc)
    player_group.update()
    road_group.draw(sc)
    road_group.update()
    asphalt_group.draw(sc)
    asphalt_group.update()



def drawmaps(nameFile):
    maps = []
    source = "lvl/" + str(nameFile)
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



























while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    'gamelvl()'
    clock.tick(FPS)