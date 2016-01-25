import pygame
from config import *

Background_color = (0,0,0)

def drawitems():
    Baseimg = pygame.image.load("textures/base_placeholder.png").convert()
    Baseimg.set_colorkey((255,0,255))
    for x in range(18):
        for y in range(18):
            if mapArray[x][y].owner != None:
                setDisplay.blit(Baseimg, (x*50+1+Gameboard_offsetx, y*50+1+Gameboard_offsety))

def drawboard():
    setDisplay.fill(Background_color)
    waterImg = pygame.image.load("textures/water.png")
    forestImg = pygame.image.load("textures/forest.png")
    desertImg = pygame.image.load("textures/desert.png")
    iceImg = pygame.image.load("textures/ice.png")
    swampImg = pygame.image.load("textures/swamp.png")
    goldImg = pygame.image.load("textures/gold.png")

    for x in range(18):
        for y in range(18):
            if mapArray[x][y].biome == "s":
                  setDisplay.blit(swampImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "i":
                  setDisplay.blit(iceImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "d":
                  setDisplay.blit(desertImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "f":
                  setDisplay.blit(forestImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "w":
                  setDisplay.blit(waterImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "g":
                  setDisplay.blit(goldImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
    
    img = pygame.image.load("textures/black_border.png").convert()
    img.set_colorkey((255,0,255))
    for x in range(18):
        for y in range(18):
            setDisplay.blit(img, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))

def drawMouseHover():
    x = pygame.mouse.get_pos()
    posx = (x[0] - Gameboard_offsetx) - (x[0] - Gameboard_offsetx)%50 + Gameboard_offsetx
    posy = (x[1] - Gameboard_offsety) - (x[1] - Gameboard_offsety)%50 + Gameboard_offsety
    if posx >= Gameboard_offsetx and posx < Gameboard_offsetx + 900 and posy >= Gameboard_offsety and posy < Gameboard_offsety + 900:
        img = pygame.image.load("textures/white_border.png").convert()
        img.set_colorkey((255,0,255))
        setDisplay.blit(img, (posx, posy))