from sprites import *
import random
import pygame

sprite_inimigo_template = [
    pygame.image.load("assets/Inimigos/template.png")
]

for index, sprite in enumerate(sprite_inimigo_template):
    sprite_inimigo_template[index] = pygame.transform.scale(sprite, (2 * TILESIZE, 2 * TILESIZE))

sprites_espantalho = [
    pygame.image.load("assets/Inimigos/espantalho_0.png"),
    pygame.image.load("assets/Inimigos/espantalho_1.png")
    ]

for index, sprite in enumerate(sprites_espantalho):
    sprites_espantalho[index] = pygame.transform.scale(sprite, (2 * TILESIZE, 2 * TILESIZE))

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        
        self._layer = ENEMY_LAYER
        self.group = AllSprites, Inimigos
        
        super().__init__(self.group)
        
        
        self.vida = 0
        self.ATK = 0
        self.speed = 0

        self.facing = "DOWN"
        self.pos = vet(x * TILESIZE, y * TILESIZE)
        self.vel = vet(0, 0)
        
        self.sprites = sprite_inimigo_template
        
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.image.set_colorkey((0,0,0))
  
        self.rect = self.image.get_rect(center = (x, y))
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.sprite_frame = 0
    
    def anim(self):
        if self.sprite_frame >= 2:
            self.sprite_frame = 0
        self.image = sprites_espantalho[math.floor(self.sprite_frame)]
        self.sprite_frame += 0.05
    
    def tomar_dano(self, quantidade):
        if self.vida > 0:
            self.vida -= quantidade
        if self.vida <= 0:
            self.kill()
        
    def update(self):
        self.anim()
        self.rect.centerx += self.vel.x
        self.rect.centery += self.vel.y
        
        self.vel.x = 0
        self.vel.y = 0

class Espantalho(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.vida = 50
        self.ATK = 10
        self.speed = 0
        self.sprites = sprites_espantalho