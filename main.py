import pygame
import sys

pygame.init()
height = 150
width = 150
screen = pygame.display.set_mode((height,width))
#screen = pygame.display.set_mode((height,width),pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Segoe UI', 30)
 
 
def fpsrun():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("white"))
	return fps_text
 
i = 0
while i<=10 :
	screen.fill((0, 0, 0))
	screen.blit(fpsrun(), (60,50))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	clock.tick(60)
	pygame.display.update()


 
pygame.quit()

