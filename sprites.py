from Equipamentos.Armaduras.armadura import *
from Equipamentos.Armamentos.arma import *
import math
from config import *

import pygame
from pygame.locals import *



AllSprites = pygame.sprite.LayeredUpdates()
Walls = pygame.sprite.LayeredUpdates()
Inimigos = pygame.sprite.LayeredUpdates()
Ataques = pygame.sprite.LayeredUpdates()
Textos = pygame.sprite.LayeredUpdates()

TILESIZE = 30

pygame.init()

vet = pygame.math.Vector2

animation_walkin_right = [
    pygame.image.load("assets/Player/Sprite_Walkin_r/sprite_walkin_r_1.png"),
	pygame.image.load("assets/Player/Sprite_Walkin_r/sprite_walkin_r_2.png"),
]

for index, sprite in enumerate(animation_walkin_right):
    animation_walkin_right[index] = pygame.transform.scale(sprite, (32, 32))
    
animation_walkin_left = [
    pygame.image.load("assets/Player/Sprite_Walkin_L/sprite_walkin_l_1.png"),
	pygame.image.load("assets/Player/Sprite_Walkin_L/sprite_walkin_l_2.png"),

]

for index, sprite in enumerate(animation_walkin_left):
    animation_walkin_left[index] = pygame.transform.scale(sprite, (32, 32))  

animation_walkin_down = [
    pygame.image.load("assets/Player/Sprite_Walkin_D/sprite_walkin_d_1.png"),
	pygame.image.load("assets/Player/Sprite_Walkin_D/sprite_walkin_d_2.png"),

]

for index, sprite in enumerate(animation_walkin_down):
    animation_walkin_down[index] = pygame.transform.scale(sprite, (32, 32))
    
    
animation_walkin_up = [
    pygame.image.load("assets/Player/Sprite_Walkin_U/sprite_walkin_u_1.png"),
	pygame.image.load("assets/Player/Sprite_Walkin_U/sprite_walkin_u_2.png"),

]

for index, sprite in enumerate(animation_walkin_up):
    animation_walkin_up[index] = pygame.transform.scale(sprite, (32, 32)) 


animation_attack_r = [
	pygame.image.load("assets/Attacks/attack_effect_r_1.png"),
	pygame.image.load("assets/Attacks/attack_effect_r_2.png"),
	pygame.image.load("assets/Attacks/attack_effect_r_3.png")
]

for index, sprite in enumerate(animation_attack_r):
    animation_attack_r[index] = pygame.transform.scale(sprite, (1.5 *TILESIZE, 1.5 *TILESIZE))

animation_attack_l = [
	pygame.image.load("assets/Attacks/attack_effect_l_1.png"),
	pygame.image.load("assets/Attacks/attack_effect_l_2.png"),
	pygame.image.load("assets/Attacks/attack_effect_l_3.png")
]

for index, sprite in enumerate(animation_attack_l):
    animation_attack_l[index] = pygame.transform.scale(sprite, (1.5 *TILESIZE, 1.5 *TILESIZE))
    
animation_attack_u = [
	pygame.image.load("assets/Attacks/attack_effect_u_1.png"),
	pygame.image.load("assets/Attacks/attack_effect_u_2.png"),
	pygame.image.load("assets/Attacks/attack_effect_u_3.png")
]

for index, sprite in enumerate(animation_attack_u):
    animation_attack_u[index] = pygame.transform.scale(sprite, (1.5 *TILESIZE, 1.5 *TILESIZE))
    
animation_attack_d = [
	pygame.image.load("assets/Attacks/attack_effect_d_1.png"),
	pygame.image.load("assets/Attacks/attack_effect_d_2.png"),
	pygame.image.load("assets/Attacks/attack_effect_d_3.png")
]

for index, sprite in enumerate(animation_attack_d):
    animation_attack_d[index] = pygame.transform.scale(sprite, (1.5 *TILESIZE, 1.5 *TILESIZE))
    

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		
		self._layer = PLAYER_LAYER
		self.group = AllSprites

		super().__init__(AllSprites)

		#Atributos
		self.stamina = 50
		self.vida = 100
		self.speed = 4

		#Equipamentos
		self.armamento = dict_Arma[0]
		self.armadura = dict_Armadura[0]
  
  
		#Posição
		self.facing = "DOWN"
		self.pos = vet(x * TILESIZE, y * TILESIZE)
		self.vel = vet(0, 0)
  
		#Sprite

		self.image = pygame.image.load("assets/MCNEW/Sprite_Walkin_D/sprite_walkin_d_1.png")
		self.image = pygame.transform.scale(self.image, (32, 32))
  
		self.rect = self.image.get_rect(center = (x, y))
		self.sprite_frame = 0
  
		#Ações
		self.atacando = False
		self.defendendo = False
  
		#Estados
		self.knockback = False
		self.knock = 2
		self.knockback_time = 0.125
		self.knockback_counter = 0
		
		self.stun = False

		self.invencibilty = False
		self.iframes = 90
		
	
	def update(self):
		self.move()
		self.anim()
		self.colisao_inimigos()
		self.check_knockback()
		self.check_iframes()

		self.rect.centerx += self.vel.x
		self.colisao_paredes(Walls, "x")
  
		self.rect.centery += self.vel.y
		self.colisao_paredes(Walls, "y")

		if self.atacando == False:
			self.hitbox = None
  
		self.vel.x = 0
		self.vel.y = 0
  
		self.pos = vet(self.rect.x, self.rect.y)
 	
	def move(self):
		keys = pygame.key.get_pressed()
		if self.stun == False:
			if keys[pygame.K_RIGHT]:
				self.vel.x = self.speed
				self.facing = "RIGHT"
			if keys[pygame.K_LEFT]:
				self.vel.x = -self.speed
				self.facing = "LEFT"
			if keys[pygame.K_UP]:
				self.vel.y = -self.speed
				self.facing = "UP"
			if keys[pygame.K_DOWN]:
				self.vel.y = self.speed
				self.facing = "DOWN"
		
		self.rect.topleft = self.pos
		#Fix para o Persoangem andando mais rápido na Diagonal
		if self.vel.x != 0 and self.vel.y != 0:
			self.vel.x /= math.sqrt(2)
			self.vel.y /= math.sqrt(2)
	
	def anim(self):
		if self.sprite_frame >= 2:
			self.sprite_frame = 0
			return
		if self.facing == "RIGHT":
			if self.vel.x == 0:
				self.image = animation_walkin_right[0]
			else:
				self.image  = animation_walkin_right[math.floor(self.sprite_frame)]
				self.sprite_frame += 0.1
	
		if self.facing == "LEFT":
			if self.vel.x == 0:
				self.image = animation_walkin_left[0]
			else:
				self.image  = animation_walkin_left[math.floor(self.sprite_frame)]
				self.sprite_frame += 0.1
	
		if self.facing == "DOWN":
			if self.vel.y == 0:
				self.image = animation_walkin_down[0]
			else:
				self.image  = animation_walkin_down[math.floor(self.sprite_frame)]
				self.sprite_frame += 0.1
	
		if self.facing == "UP":
			if self.vel.y == 0:
				self.image = animation_walkin_up[0]
			else:
				self.image  = animation_walkin_up[math.floor(self.sprite_frame)]
				self.sprite_frame += 0.1
 
	def tomar_knockback(self):
		if self.knockback == False:
			self.knockback = True
			self.stun = True
			if self.facing == "UP":
				self.vel.y = self.knock
				self.rect = self.rect.move(self.vel)
			if self.facing == "DOWN":
				self.vel.y = -self.knock
				self.rect = self.rect.move(self.vel)
			if self.facing == "RIGHT":
				self.vel.x = -self.knock
				self.rect = self.rect.move(self.vel)
			if self.facing == "LEFT":
				self.vel.x = self.knock
				self.rect = self.rect.move(self.vel)
    
			self.knockback_counter = self.knockback_time * FPS
   
	def check_knockback(self):
		if self.knockback == True:
			self.knockback_counter -= 1
			
			if self.knockback_counter <= 0:
				self.knockback = False
				self.stun = False
    
			else:
				if self.facing == "UP":
					self.vel.y = self.knock
					self.rect = self.rect.move(self.vel)
				if self.facing == "DOWN":
					self.vel.y = -self.knock
					self.rect = self.rect.move(self.vel)
				if self.facing == "RIGHT":
					self.vel.x = -self.knock
					self.rect = self.rect.move(self.vel)
				if self.facing == "LEFT":
					self.vel.x = self.knock
					self.rect = self.rect.move(self.vel)
			
	def tomar_iframes(self, iframes=90):
		self.invencibilty = True
		self.iframes = iframes
  
	def check_iframes(self):
		if self.invencibilty == True:
			self.iframes -= 1
			if self.iframes <= 0:
				self.invencibilty = False
				self.iframes = 90
 		
	def tomar_dano (self, quantidade):
		if self.invencibilty == False:
			self.tomar_knockback()
			if self.vida > 0:
				self.vida -= quantidade
			if self.vida <= 0:
				self.kill()
			self.tomar_iframes()
	
	def atacar(self):
		if not self.stun:
			self.atacando = True
	
	def colisao_ataque(self):
		for inimigo in Inimigos:
			colide = self.hitbox.colliderect((self.hitbox, inimigo.rect))
			if colide:
				inimigo.kill()

	def colisao_paredes(self, group, direcao):
		colide = pygame.sprite.spritecollide(self, group, False)
		if direcao == 'x':
			if colide:
				if self.vel.x > 0:
					self.rect.right = colide[0].rect.left
				if self.vel.x < 0:
					self.rect.left = colide[0].rect.right
		if direcao == 'y':
			if colide:
				if self.vel.y > 0:
					self.rect.bottom = colide[0].rect.top
				if self.vel.y < 0:
					self.rect.top = colide[0].rect.bottom
	
	def colisao_inimigos(self):
		colide = pygame.sprite.spritecollide(self, Inimigos, False)
		if colide:
			for inimigo in Inimigos:
				self.tomar_dano(inimigo.ATK)

	
	def defender(self):
		self.defendendo = True
		self.pos = self.pos
		print ("O Jogador está defendendo")
		
	def abrir_inventario(self):
		print(f'''Inventário:
	Arma: {self.armamento.Nome} ({self.armamento.Descricao})
	Armadura: {self.armadura.Nome} ({self.armadura.Descricao})''')

	def consumir(self):
		print ("O Jogador usou o Consumível")
  
class Guerreiro(Player):
	def __init__(self):
		super().__init__()
		self.armamento = dict_Arma[1]
		self.armadura = dict_Armadura[1]
		self.vida += self.armadura.DEF
		self.speed = 3
		self.stamina = 60

class Mago(Player):
	def __init__(self):
		super().__init__()
		self.armamento = dict_Arma[2]
		self.armadura = dict_Armadura[2]
		self.vida += self.armadura.DEF
		self.speed = 4
		self.stamina = 100
    
class Arqueiro(Player):
	def __init__(self):
		super().__init__()
		self.armamento = dict_Arma[3]
		self.armadura = dict_Armadura[3]
		self.vida += self.armadura.DEF
		self.speed = 5
		self.stamina = 80



class Attack(pygame.sprite.Sprite):
    def __init__(self, player, x, y):
        
        self._layer = PLAYER_LAYER
        self.group = AllSprites, Ataques
        
        super().__init__(self.group)
        
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.player = player
        
        self.sprite_frame = 0
        
        self.image = animation_attack_d[1]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.anim()
        self.colisao()
        
    def colisao(self):
        colide = pygame.sprite.spritecollide(self, Inimigos, False)
        if colide:
            for alvo in colide:
                alvo.tomar_dano(self.player.armamento.ATK)
    
    def anim(self):
        direction = self.player.facing
        
        if direction == "UP":
            self.image = animation_attack_u[math.floor(self.sprite_frame)]
            self.sprite_frame += 0.5
            if self.sprite_frame >= 3:
                self.kill()
        if direction == "RIGHT":
            self.image = animation_attack_r[math.floor(self.sprite_frame)]
            self.sprite_frame += 0.5
            if self.sprite_frame >= 3:
                self.kill()
        if direction == "DOWN":
            self.image = animation_attack_d[math.floor(self.sprite_frame)]
            self.sprite_frame += 0.5
            if self.sprite_frame >= 3:
                self.kill()
        if direction == "LEFT":
            self.image = animation_attack_l[math.floor(self.sprite_frame)]
            self.sprite_frame += 0.5
            if self.sprite_frame >= 3:
                self.kill()
 
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        
        self._layer = WALL_LAYER
        self.group = AllSprites, Walls
        
        super().__init__(self.group)
        
        self.pos = vet(x * TILESIZE, y * TILESIZE)
        self.width = TILESIZE
        self.height = TILESIZE
        
        #self.image = pygame.transform.scale(pygame.image.load("assets/tile_set01.png"), (self.width, self.height))
        self.image = pygame.image.load("assets/TileSet/tile_set01.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
    
        self._layer = FLOOR_LAYER
        self.group = AllSprites
        
        super().__init__(self.group)
        
        self.pos = vet(x * TILESIZE, y * TILESIZE)
        self.width = TILESIZE
        self.height = TILESIZE
        
        #self.image = pygame.transform.scale(pygame.image.load("assets/tile_set01.png"), (self.width, self.height))
        self.image = pygame.image.load("assets/TileSet/tile_set00.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y



class TextBox(pygame.sprite.Sprite):
    def __init__(self, text):
        
        self._layer = TEXTBOX_LAYER
        self.group = AllSprites, Textos
        
        super().__init__(self.group)
        
        self.font = pygame.font.SysFont("Arial", 20)
        self.page = 0
        self.content = text
        self.frame_sprite = pygame.image.load("assets/HUD/textbox_frame.png")
        self.frame_sprite = pygame.transform.scale(self.frame_sprite, (600, 180))
        self.image = self.frame_sprite
        self.pos = vet(WIDTH/2, HEIGHT - 120)
        self.rect = self.image.get_rect(center= (self.pos.x, self.pos.y))
        
        self.text = self.font.render(self.content[self.page], True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.image.get_width()/2, self.image.get_height()/2))
        self.text_frame = 0
        
    def update(self):
        words = [word.split(' ') for word in self.content[self.page].splitlines()]  # 2D array where each row is a list of words.
        space = self.font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.image.get_size()
        x, y = 20, 20
        for line in words:
            for word in line:
                word_surface = self.font.render(word, True, (255,255,255))
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = 20  # Reset the x.
                    y += word_height  # Start on new row.
                self.image.blit(word_surface, (x, y))
                x += word_width + space
            x = 20  # Reset the x.
            y += word_height  # Start on new row.
            
    def close_box(self):
        if self.page >= (len(self.content)- 1):
            self.kill()
        else:
            self.page += 1
                
