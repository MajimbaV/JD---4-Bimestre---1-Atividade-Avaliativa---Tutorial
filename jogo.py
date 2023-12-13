import pygame
import sys
from pygame.locals import *
from mapa import *

pygame.init()

CLOCK = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TUTORIAL TESTE")

TextoTeste = TextBox(["USE AS SETAS DO TECLADO PARA SE MOVER, Z PARA FECHAR ESSE MENU E X PARA ATACAR!"])
player = Player(0, 0)


createTileMap(player)

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
               TextoTeste.close_box()
            if event.key == pygame.K_x:
                if player.facing == "UP":
                    Attack(player, player.rect.x, player.rect.y - TILESIZE)
                if player.facing == "DOWN":
                    Attack(player, player.rect.x, player.rect.y + TILESIZE)
                if player.facing == "LEFT":
                    Attack(player, player.rect.x - TILESIZE, player.rect.y )
                if player.facing == "RIGHT":
                    Attack(player, player.rect.x + TILESIZE, player.rect.y)
        
    display.fill((0, 0, 0))
    
    AllSprites.update()
    AllSprites.draw(display)
        
    pygame.display.update()
    CLOCK.tick(FPS)