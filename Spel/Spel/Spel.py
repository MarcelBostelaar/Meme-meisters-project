import os, sys
import pygame
from pygame.locals import *

gamename = "Frequency"
window_height = 900
window_width = 900

fps = 30
fpsTime = pygame.time.Clock()

pygame.init()

setDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(gamename)

def drawboard():
    waterImg = pygame.image.load("textures/water.png")
    forestImg = pygame.image.load("textures/forest.png")
    desertImg = pygame.image.load("textures/desert.png")
    iceImg = pygame.image.load("textures/ice.png")
    swampImg = pygame.image.load("textures/swamp.png")
    goldImg = pygame.image.load("textures/gold.png")

    #mapArray = [[0 for x in range(18)]for y in range(18)]

    mapArray = [
        ["s","s","s","s","s","s","s","w","w","w","w","i","i","i","i","i","i","i"],
        ["s","s","s","s","s","s","s","w","w","w","w","i","i","i","i","i","i","i"],
        ["s","s","s","s","s","s","s","w","w","w","w","i","i","i","i","i","i","i"],
        ["s","s","s","s","s","s","s","w","w","w","w","i","i","i","i","i","i","i"],
        ["s","s","s","s","s","s","s","w","w","w","w","i","i","i","i","i","i","i"],
        ["s","s","s","s","s","s","w","w","w","w","w","w","i","i","i","i","i","i"],
        ["s","s","s","s","s","w","w","w","w","w","w","w","w","i","i","i","i","i"],
        ["w","w","w","w","w","w","w","g","g","g","g","w","w","w","w","w","w","w"],
        ["w","w","w","w","w","w","w","g","g","g","g","w","w","w","w","w","w","w"],
        ["w","w","w","w","w","w","w","g","g","g","g","w","w","w","w","w","w","w"],
        ["w","w","w","w","w","w","w","g","g","g","g","w","w","w","w","w","w","w"],
        ["d","d","d","d","d","w","w","w","w","w","w","w","w","f","f","f","f","f"],
        ["d","d","d","d","d","d","w","w","w","w","w","w","f","f","f","f","f","f"],
        ["d","d","d","d","d","d","d","w","w","w","w","f","f","f","f","f","f","f"],
        ["d","d","d","d","d","d","d","w","w","w","w","f","f","f","f","f","f","f"],
        ["d","d","d","d","d","d","d","w","w","w","w","f","f","f","f","f","f","f"],
        ["d","d","d","d","d","d","d","w","w","w","w","f","f","f","f","f","f","f"],
        ["d","d","d","d","d","d","d","w","w","w","w","f","f","f","f","f","f","f"] ]

    for x in range(18):
        for y in range(18):
            if mapArray[x][y] == "s":
                  setDisplay.blit(swampImg, (x*50, y*50))
            elif mapArray[x][y] == "i":
                  setDisplay.blit(iceImg, (x*50, y*50))
            elif mapArray[x][y] == "d":
                  setDisplay.blit(desertImg, (x*50, y*50))
            elif mapArray[x][y] == "f":
                  setDisplay.blit(forestImg, (x*50, y*50))
            elif mapArray[x][y] == "w":
                  setDisplay.blit(waterImg, (x*50, y*50))
            elif mapArray[x][y] == "g":
                  setDisplay.blit(goldImg, (x*50, y*50))
    
    img = pygame.image.load("textures/black_border.png").convert()
    img.set_colorkey((255,0,255))
    for x in range(18):
        for y in range(18):
            setDisplay.blit(img, (x*50, y*50))

def drawMouseHover():
    x = pygame.mouse.get_pos()
    posx = x[0] - x[0]%50
    posy = x[1] - x[1]%50
    
    img = pygame.image.load("textures/white_border.png").convert()
    img.set_colorkey((255,0,255))
    setDisplay.blit(img, (posx, posy))    

while True:
    drawboard()
    drawMouseHover()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(fps)