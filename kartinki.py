import pygame.image
from pygame.examples.cursors import image

road_image = pygame.image.load('image/road.png').convert_alpha()
asphalt_image = pygame.image.load('image/asphalt.png').convert_alpha()
grass_image = pygame.image.load('image/grass.png').convert_alpha()
player_image = pygame.transform.flip(pygame.image.load('image/player.png').convert_alpha(), True, False)
fon_image = pygame.image.load('image/fon.jpg').convert_alpha()
start_image = pygame.image.load('image/start-finish.png').convert_alpha()
speedmetr_image = pygame.image.load('image/speedometr.png').convert_alpha()
taxmetr_image = pygame.image.load('image/taxometr.png').convert_alpha()
enemy_image = pygame.image.load('image/enemy.png')
startbutton_image = pygame.image.load('image/start.png').convert_alpha()
exitbutton_image = pygame.image.load('image/exit(1).png').convert_alpha()
buybutton_image = pygame.image.load('image/buy(1).png').convert_alpha()
optionbutton_image = pygame.image.load('image/option(1).png').convert_alpha()
startfon_image = pygame.transform.scale(pygame.image.load('image/start.jpg').convert_alpha(), (1200, 800))