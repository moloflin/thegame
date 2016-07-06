import pygame
import time
import random
from colors import *

#Game Character Classes!-------------------------------------------------------
class Hero_Ship(pygame.sprite.Sprite):
	def __init__(self, imgfile):
		super(Hero_Ship, self).__init__()
		if (imgfile != None):
			self.image = pygame.image.load(imgfile)
			self.rect = self.image.get_rect()
	
	def setPos(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def moveUp(self):
		self.rect.y -= 10

	def moveDown(self):
		self.rect.y += 10

	def moveLeft(self):
		self.rect.x -= 10

	def moveRight(self):
		self.rect.x += 10

class Enemy_Ship_Basic(pygame.sprite.Sprite):
	def __init__(self, imgfile):
		super(Enemy_Ship_Basic, self).__init__()
		if (imgfile != None):
			self.image = pygame.image.load(imgfile)
			self.rect = self.image.get_rect()
	
	def setPos(self, x, y):
		self.rect.x = x
		self.rect.y = y

class Projectile_Basic(pygame.sprite.Sprite):
	def __init__(self):
		super(Projectile_Basic, self).__init__()
		WIDTH = 10
		HEIGHT = 10
		COLOR = red
		self.image = pygame.Surface((WIDTH, HEIGHT))
		self.image.fill(COLOR)
		self.rect = self.image.get_rect()
	def launch(self): 
		#Fires the projectile 5 pixels
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
	blockSize = 10
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
	enemyOne = Enemy_Ship_Basic("enemyRed.png")
	enemyTwo = Enemy_Ship_Basic("enemyRed.png")
	enemyThree = Enemy_Ship_Basic("enemyRed.png")
	allied_ship_group.add(mainChar)
	enemy_ship_group.add(enemyOne, enemyTwo, enemyThree)
	all_sprites_group.add(mainChar, enemyOne, enemyTwo, enemyThree)

	#Game loop--------------------------------------------------------------
	def gameLoop():
		#Variables to move square up/down
		gameEnd = False
		gameOver = False
		head_x = display_width / 2
		head_y = display_height / 2
		headx_change = 0
		heady_change = 0
		#Initialize clock for FPS
		theClock = pygame.time.Clock()
		FPS = 30
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
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						headx_change = -blockSize
					elif event.key == pygame.K_RIGHT:
						headx_change = blockSize
					elif event.key == pygame.K_UP:
						heady_change = -blockSize
					elif event.key == pygame.K_DOWN:
						heady_change = blockSize
					elif event.key == pygame.K_SPACE:
						basicProj = Projectile_Basic()
						basicProj.rect.x = mainChar.rect.x
						basicProj.rect.y = mainChar.rect.y
						all_sprites_group.add(basicProj)
						basicProj.launch()
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						headx_change = 0
					elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						heady_change = 0

			#Boundaries & Refresh Background---------------------------------------
			if head_x > display_width:
				head_x = 0 
			elif head_x < 0:
				head_x = display_width
			elif head_y > display_height:
				head_y = 0
			elif head_y < 0:
				head_y = display_height
			gameDis.fill(black)
			#Drawing Background-----------------------------------------------------
			for item in starList:
				item[1] += 1
				pygame.draw.circle(gameDis, white, item, 2)
				if item[1] > 800:
					item[1] = -3
					item[0] = random.randrange(800)

			#Movement!--------------------------------------------------------------
			head_x += headx_change
			head_y += heady_change

			#Drawing Sprites
			mainChar.setPos(head_x, head_y)
			enemyOne.setPos(200, 200)
			enemyTwo.setPos(150, display_height/3)
			enemyThree.setPos(display_width/2, display_height/4)
			all_sprites_group.draw(gameDis)
			pygame.display.update()

			#Player/Enemy Interaction!----------------------------------------------
			#for basicProj in 
			#ships_destroyed_list = pygame.sprite.spritecollide(basicProj, ship_group, True)

			#FPS-------------------------------------------------------------------
			theClock.tick(FPS)
		#Quit pygame and python
		pygame.quit()
		quit()
	gameLoop()