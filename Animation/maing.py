import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400))

AQUA=(0,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)
RED=(255,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
DISPLAYSURF.fill(BLUE)

pygame.draw.rect(DISPLAYSURF, GREEN, (0, 300, 500, 100)) #ground
pygame.draw.rect(DISPLAYSURF, BLACK, (300, 225, 100, 75)) #house frame
pygame.draw.rect(DISPLAYSURF, WHITE, (320,250, 10,10)) #window 1
pygame.draw.rect(DISPLAYSURF, WHITE, (370,250, 10,10)) #window 2, notice that it is NOT at x 380
#you would think with 20 in from the left, to be equal it would be 20 in from the right, but NOPE
pygame.draw.rect(DISPLAYSURF, WHITE, (360,275, 20,25)) #door

pygame.draw.polygon(DISPLAYSURF, BLACK, ((300,225),(399,225),(350,175)))#roof
###SECOND PERSON
pygame.draw.circle(DISPLAYSURF, BLACK, (200, 250), 7, 2) #head
pygame.draw.line(DISPLAYSURF, BLACK, (200, 257), (200, 280), 2)#body
pygame.draw.line(DISPLAYSURF, BLACK, (200, 280), (190, 300), 2)#right leg
pygame.draw.line(DISPLAYSURF, BLACK, (200, 280), (210, 300), 2)#left leg
pygame.draw.line(DISPLAYSURF, BLACK, (200, 272), (190, 258), 2)#left arm
pygame.draw.line(DISPLAYSURF, BLACK, (200, 272), (210, 258), 2)#right arm

##FIRST PERSON
pygame.draw.circle(DISPLAYSURF, BLACK, (170, 250), 7, 2) #head
pygame.draw.line(DISPLAYSURF, BLACK, (170, 257), (170, 280), 2)#body
pygame.draw.line(DISPLAYSURF, BLACK, (170, 280), (160, 300), 2)#right leg
pygame.draw.line(DISPLAYSURF, BLACK, (170, 280), (180, 300), 2)#left leg
pygame.draw.line(DISPLAYSURF, BLACK, (170, 272), (160, 258), 2)#left arm
pygame.draw.line(DISPLAYSURF, BLACK, (170, 272), (180, 258), 2)#right arm

pygame.display.set_caption('First Drawing!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

