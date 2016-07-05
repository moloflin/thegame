import pygame
import time
from colors import *

#Inheriting sprite superclass
class Block(pygame.sprite.Sprite):
	def __init__(self, color = blue, width = 64, height = 64):
		super(Block, self).__init__()
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
	
	def setPos(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def setImg(self, filename = None):
		if (filename != None):
			self.image = pygame.image.load(filename)
			self.rect = self.image.get_rect()
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
						#heady_change = 0
					elif event.key == pygame.K_RIGHT:
						headx_change = blockSize
						#heady_change = 0
					elif event.key == pygame.K_UP:
						heady_change = -blockSize
						#headx_change = 0
					elif event.key == pygame.K_DOWN:
						heady_change = blockSize
						#headx_change = 0
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						headx_change = 0
					elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						heady_change = 0

			#Boundaries!-----------------------------------------------------------
			if head_x > display_width:
				head_x = 0 
			elif head_x < 0:
				head_x = display_width
			elif head_y > display_height:
				head_y = 0
			elif head_y < 0:
				head_y = display_height

			#Apply changes to square, fill background with white
			head_x += headx_change
			head_y += heady_change	
			gameDis.fill(white)

			#Drawing Squares
			block_group = pygame.sprite.Group()
			mainChar = Block(black, 10, 10)
			mainChar.setImg("mai.png")
			mainChar.setPos(head_x, head_y)
			squareOne = Block(red)
			squareOne.setPos(200, 200)
			squareTwo = Block(green)
			squareTwo.setPos(150, display_height/3)
			squareThree = Block(gray)
			squareThree.setPos(display_width/2, display_height/4)
			block_group.add(mainChar, squareOne, squareTwo, squareThree)
			block_group.draw(gameDis)
			pygame.display.update()
			#FPS-------------
			theClock.tick(FPS)
		#Quit pygame and python
		pygame.quit()
		quit()
	gameLoop()
