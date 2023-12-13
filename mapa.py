import pygame
from pygame.locals import *
from config import *
from sprites import *
from enemy import *



TILESIZE = 30

TILEMAP = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W..........................W',
    'W..........................W',
    'W..........................W',
    'W..........................W',
    'W..........................W',
    'W..........................W',
    'W.....S...........D........W',
    'W..........................W',
    'W..........................W',
    'W..........................W',
    'W..........................W',
    'W..........................W',
    'W..........................W',
    'W..........................W',
    'WWWWWWW..............WWWWWWW',
    'W..........................W',
    'W............P.............W',
    'W..........................W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    
]



def createTileMap(player):
    for i, row in enumerate(TILEMAP):
        for j, column in enumerate(row):
            Floor(j, i)
            if column == "W":
                Wall(j, i)         
            if column == "D":
                Espantalho(j, i)       
            if column == "P":
                player.pos.x = j * TILESIZE
                player.pos.y = i * TILESIZE



