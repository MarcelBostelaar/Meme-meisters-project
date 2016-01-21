import os, sys
import pygame
import random
from pygame.locals import *
from Player import *
from Tile import *
from ButtonClass import *

gamename = "Frequency"
window_height = 900
window_width = 1300

Gameboard_offsetx = 125
Gameboard_offsety = 0

fps = 60
fpsTime = pygame.time.Clock()

pygame.init()

setDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(gamename)

mapArray = [
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

def drawitems():
    Baseimg = pygame.image.load("textures/base_placeholder.png").convert()
    Baseimg.set_colorkey((255,0,255))
    for x in range(18):
        for y in range(18):
            if mapArray[x][y].owner != None:
                setDisplay.blit(Baseimg, (x*50+1+Gameboard_offsetx, y*50+1+Gameboard_offsety))



def drawboard():
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
    
def PlayerCreation(Pamount):
    playerlist = []
    for i in range(Pamount):
        newplayer = Player("newname") #later on, ask for name of player
        biomepicked = False
        while not biomepicked:
            j = random.randint(1,4)
            if j == 1:
                if mapArray[0][0].building == None:
                    mapArray[0][0].building = ["Base", 25]
                    mapArray[0][0].owner = newplayer
                    biomepicked = True
            elif j ==2:
                if mapArray[0][17].building == None:
                    mapArray[0][17].building = ["Base", 25]
                    mapArray[0][17].owner = newplayer
                    biomepicked = True
            elif j ==3:
                if mapArray[17][0].building == None:
                    mapArray[17][0].building = ["Base", 25]
                    mapArray[17][0].owner = newplayer
                    biomepicked = True
            elif j ==4:
                if mapArray[17][17].building == None:
                    mapArray[17][17].building = ["Base", 25]
                    mapArray[17][17].owner = newplayer
                    biomepicked = True

PlayerCreation(3)

while True:
    drawboard()
    drawitems()
    drawMouseHover()

    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            print("keydown")
        if event.type == MOUSEBUTTONDOWN:
            stateMouse = pygame.mouse.get_pressed()
            if stateMouse[0] == 1:
                if lol.pressed():
                    print("gold!")
                if kek.pressed():
                    print("Test!")
                
            



    lol = Button("Gold", (0,255,255), font_size = 30, texture = "textures/gold.png")
    kek = Button("test", (255,0,255), font_size = 232, height = 523, width = 800, bgcolor = (200,65,45))
    kek.draw(52+Gameboard_offsetx,96+Gameboard_offsety, setDisplay)
    lol.draw(420+Gameboard_offsetx,0+Gameboard_offsety, setDisplay)

    pygame.display.update()
    fpsTime.tick(fps)