import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Hit it!')

# set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
RED=(25,0,0)

# set up point system and player image
Knight50 = pygame.image.load('knight50.png')
kx=0
ky=0

foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20

foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6


# run the game loop
while True:
    kpos = ((kx, ky), (kx, ky + 50), (kx +50, ky), (kx + 50, ky + 50))#top left, bottom left, top right, bottom right
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False




    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # move the player
    if moveDown and ky + 50< WINDOWHEIGHT:
        ky += MOVESPEED
        print(kpos)

    if moveUp and ky > 0:
        ky -= MOVESPEED
        print(kpos)
    if moveLeft and kx > 0:
        kx -= MOVESPEED
        print(kpos)
    if moveRight and kx+50 < WINDOWWIDTH:
        kx += MOVESPEED
        print(kpos)

    # draw the player onto the surface

    windowSurface.blit(Knight50, (kx,ky))
    # check if the player has intersected with any food squares.


    # draw the food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
