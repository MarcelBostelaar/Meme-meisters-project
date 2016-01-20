import os, sys
import pygame
from pygame.locals import *
from Player import *
from Tile import *

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

    mapArray = [    #later, change so that it stores a tile entity
        [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
        [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
        [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
        [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
        [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
        [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
        [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
        [Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("g"), Tile("g"), Tile("g"), Tile("g"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w")],
        [Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("g"), Tile("g"), Tile("g"), Tile("g"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w")],
        [Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("g"), Tile("g"), Tile("g"), Tile("g"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w")],
        [Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("g"), Tile("g"), Tile("g"), Tile("g"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w")],
        [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
        [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
        [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
        [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
        [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
        [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
        [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")] ]


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
    
def PlayerCreation(Pamount):
    playerlist = []
    for i in range(Pamount):
        newplayer = Player(newname) #later on, ask for name of player

while True:
    drawboard()
    drawMouseHover()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(fps)