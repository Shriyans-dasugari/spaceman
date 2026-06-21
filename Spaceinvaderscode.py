import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1200,600))

pygame.display.set_caption('Win against the other spaceship!')

image1 = pygame.image.load('l8Spaceinvadersprojekt/background.png')
image2 = pygame.image.load('l8Spaceinvadersprojekt/redspaceship.png')
image3 = pygame.image.load('l8Spaceinvadersprojekt/yellowspaceship.png')
# making image chsnge direction ans size 
redship = pygame.transform.rotate(pygame.transform.scale(image2,(60,40)),90)
yellowship = pygame.transform.rotate(pygame.transform.scale(image3,(60,40)),270)

def drawwindow(red,yellow):
    screen.blit(image1,(0,0))
    #using changed image as the variable 'redship' and 'yellowship'
    screen.blit(redship,(200,300))
    screen.blit(yellowship,(1000,300))
    pygame.display.update()

def redshipmovement(keypress,red):
    if keypress[pygame.K_a]:
        red.x-=2
    if keypress[pygame.K_d]:
        red.x+=2
    if keypress[pygame.K_w]:
        red.y+=2
    if keypress[pygame.K_s]:
        red.y-=2


# these arn't ships, these are invisable rectangles for. oving the spaceships
red = pygame.Rect(200,300,60,40)
yellow = pygame.Rect(1000,300,60,40)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    keypress = pygame.key.get_pressed()   
    redshipmovement(keypress,red)
    drawwindow(red,yellow)
    pygame.display.update()
    