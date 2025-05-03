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


