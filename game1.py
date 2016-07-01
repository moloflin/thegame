import pygame
import time
#Start
x = pygame.init()
#Printing init returned tuple...not sure why just kinda interesting!
print(x)
#Colors!
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#Set up display
display_height = 800
display_width = 800
gameDis = pygame.display.set_mode((display_width, display_height))
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

		#Apply changes to square
		head_x += headx_change
		head_y += heady_change	
		gameDis.fill(white)
		#Drawing Squares
		pygame.draw.rect(gameDis, black, [head_x, head_y, blockSize, blockSize])
		pygame.draw.rect(gameDis, blue, [display_width/3, display_height/3, blockSize*2, blockSize*2])
		pygame.draw.rect(gameDis, blue, [display_width/4, display_height/3, blockSize*2, blockSize*2])
		pygame.draw.rect(gameDis, blue, [display_width/5, display_height/3, blockSize*2, blockSize*2])
		pygame.draw.rect(gameDis, blue, [display_width/6, display_height/3, blockSize*2, blockSize*2])
		pygame.display.update()
		#FPS-------------
		theClock.tick(FPS)
	#Quit pygame and python
	pygame.quit()
	quit()
gameLoop()
