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
gameDis = pygame.display.set_mode((800, 800))
pygame.display.set_caption('First Try!')
pygame.display.flip()
gameEnd = False
while not gameEnd:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameEnd = True
	#Fills screen with blue		
	gameDis.fill(blue)
	pygame.display.update()
#Quit pygame and python
pygame.quit()
quit()


