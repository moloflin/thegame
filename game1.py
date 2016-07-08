import pygame
import sys
import time
import random
from colors import *

#Game Character Classes!-------------------------------------------------------
class Hero_Ship(pygame.sprite.Sprite):
	def __init__(self, imgfile):
		super(Hero_Ship, self).__init__()
		if (imgfile != None):
			self.image = pygame.image.load(imgfile)
		self.change_x = 0
		self.change_y = 0
		self.rect = self.image.get_rect()

	def setPos(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def update(self):
		self.rect.x += self.change_x
		self.rect.y += self.change_y
	
	def goLeft(self):
		self.change_x -= 6
	
	def goRight(self):
		self.change_x += 6
	
	def goUp(self):
		self.change_y -= 6
	
	def goDown(self):
		self.change_y += 6

	def stop(self):
		self.change_x = 0
		self.change_y = 0

class Enemy_Ship_Basic(pygame.sprite.Sprite):
	def __init__(self, imgfile):
		super(Enemy_Ship_Basic, self).__init__()
		if (imgfile != None):
			self.image = pygame.image.load(imgfile)
			self.rect = self.image.get_rect()
	
	def setPos(self, x, y):
		self.rect.x = x
		self.rect.y = y
	def update(self):
		return

class Projectile_Basic(pygame.sprite.Sprite):
	def __init__(self):
		super(Projectile_Basic, self).__init__()
		WIDTH = 5
		HEIGHT = 5
		COLOR = red
		self.image = pygame.Surface((WIDTH, HEIGHT))
		self.image.fill(COLOR)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y -= 5
	
#Background Stuff--------------------------------------------------------
starList = []
for q in range(50):
	x = random.randrange(0, 800)
	y = random.randrange(0, 800)
	starList.append([x, y])
#Start------------------------------------------------------------------- 
#Guard to make sure this is file we're actually running
if (__name__ == "__main__"):
	pygame.init()
	#Set up display
	window_size = display_height, display_width = 800, 800
	gameDis = pygame.display.set_mode(window_size)
	pygame.display.set_caption('Moving Square!')
	#Inititalize screen (first update)
	pygame.display.flip()

	#User Messages----------------------------------------------------------
	font = pygame.font.SysFont(None, 25)
	def pushToScreen(msg, color):
		screenText = font.render(msg, True, color)
		#Placing text to screen at middle point
		gameDis.blit(screenText, [display_width/2, display_height/2])

	#Sprite Groups----------------------------------------------------------
	allied_ship_group = pygame.sprite.Group()
	enemy_ship_group = pygame.sprite.Group()
	proj_list = pygame.sprite.Group()
	all_sprites_group = pygame.sprite.Group()
	mainChar = Hero_Ship("mai.png")
	enemies = 5
	for q in range(enemies):
		enemy = Enemy_Ship_Basic("enemyRed.png")
		enemy.rect.x = random.randrange(display_width)
		enemy.rect.y = random.randrange(display_height)
		enemy_ship_group.add(enemy)
		all_sprites_group.add(enemy)
	allied_ship_group.add(mainChar)
	all_sprites_group.add(mainChar)
	#Initialize clock for FPS
	theClock = pygame.time.Clock()
	#Game loop--------------------------------------------------------------
	def gameLoop():
		gameEnd = False
		gameOver = False
		enemies_left = [enemies]
		enemy_count = len(enemies_left)
		#Variables to move square up/down
		head_x = display_width / 2
		head_y = display_height / 2
		#headx_change = 0
		#heady_change = 0
		FPS = 30
		mainChar.rect.x = display_width / 2
		mainChar.rect.y = display_height / 2
		while not gameEnd:
			while gameOver == True:
				gameDis.fill(white)
				pushToScreen("Game over, press C to play again or Q to quit", red)
				pygame.display.update()
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							gameEnd = True
							gameOver = False
						if event.key == pygame.K_c:
							gameLoop()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameEnd = True
			#Player Controlled Movement & Shooting-------------------------------------------------------
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						mainChar.goLeft()
					if event.key == pygame.K_RIGHT:
						mainChar.goRight()
					if event.key == pygame.K_UP:
						mainChar.goUp()
					if event.key == pygame.K_DOWN:
						mainChar.goDown()
					if event.key == pygame.K_SPACE:
						#Fire Projectile (BASIC)
						projectile = Projectile_Basic()
						projectile.rect.x = mainChar.rect.x
						projectile.rect.y = mainChar.rect.y
						all_sprites_group.add(projectile)
						proj_list.add(projectile)
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
						mainChar.stop()
				if enemy_count == 0:
					gameOver = True
			#head_x += headx_change
			#head_y += heady_change
			all_sprites_group.update()
			#Player/Enemy Interaction!----------------------------------------------
			for projectile in proj_list:
				hit_list = pygame.sprite.spritecollide(projectile, enemy_ship_group, True)
				for enemy in hit_list:
					proj_list.remove(projectile)
					all_sprites_group.remove(projectile)
					enemy_count -= 1
				if projectile.rect.y < 0:
					proj_list.remove(projectile)
					all_sprites_group.remove(projectile)

			#Boundaries & Refresh Background--------------------------------------------------
			if mainChar.rect.x > display_width:
				mainChar.rect.x = 0 
			elif mainChar.rect.x < 0:
				mainChar.rect.x = display_width
			elif mainChar.rect.y > display_height:
				mainChar.rect.y = 0
			elif mainChar.rect.y < 0:
				mainChar.rect.y = display_height
			gameDis.fill(black)

			#Drawing Background-----------------------------------------------------
			for item in starList:
				item[1] += 1
				pygame.draw.circle(gameDis, white, item, 2)
				if item[1] > 800:
					item[1] = -3
					item[0] = random.randrange(800)

			#Setting Positions & Drawing Sprites--------------------------------------------------------
			#mainChar.setPos(head_x, head_y)
			all_sprites_group.draw(gameDis)
			#Final Update
			pygame.display.update()
			#FPS-------------------------------------------------------------------
			theClock.tick(FPS)
		#Quit pygame and python
		pygame.quit()
		quit()
	gameLoop()