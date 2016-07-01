import pygame
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
gameDis = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Moving Square!')
#Inititalize screen (first update)
pygame.display.flip()
#Variables to move square up/down
gameEnd = False
head_x = 300
head_y = 300
headx_change = 0
heady_change = 0
#Initialize clock for FPS
theClock = pygame.time.Clock()

#Game loop--------------------------------------------------------------
while not gameEnd:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameEnd = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				headx_change = -10
			elif event.key == pygame.K_RIGHT:
				headx_change = 10
			elif event.key == pygame.K_UP:
				heady_change = -10
			elif event.key == pygame.K_DOWN:
				heady_change = 10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				headx_change = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				heady_change = 0
#Apply changes to square
	head_x += headx_change
	head_y += heady_change	
	gameDis.fill(white)
#Drawing Square
	pygame.draw.rect(gameDis, black, [head_x, head_y, 10, 10])
	pygame.display.update()
	#FPS-------------
	theClock.tick(30)
#Quit pygame and python
pygame.quit()
quit()


