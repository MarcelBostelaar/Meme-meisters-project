import pygame
from config import *
import ButtonClass
import random

Background_color = (0,0,0)

font_colour = (255,255,255)
fontsize = 30

end_turn_button = ButtonClass.Button("End Turn", font_colour, font_size=fontsize, width = 400, height = 75, bgcolor = (255,100,0))
menu_button = ButtonClass.Button("Menu", font_colour, font_size=fontsize, width = 300, height = 75, bgcolor = (255,100,0))
help_button = ButtonClass.Button("?", font_colour, font_size=fontsize, width = 75, height = 75, bgcolor = (255,100,0))

backgr = pygame.image.load("textures/parchment_texture.png")
sizeTexture_parchment = backgr.get_rect().size

waterImg = pygame.image.load("textures/water.png")
waterImg0 = pygame.image.load("textures/water0.png")
waterImg1 = pygame.image.load("textures/water1.png")
waterImg2 = pygame.image.load("textures/water2.png")
waterImg3 = pygame.image.load("textures/water3.png")
waterImg4 = pygame.image.load("textures/water4.png")
waterImg5 = pygame.image.load("textures/water5.png")
waterImg6 = pygame.image.load("textures/water6.png")
waterImg7 = pygame.image.load("textures/water7.png")
forestImg = pygame.image.load("textures/forest2x2.png")
forestImgLower = pygame.image.load("textures/forest2x1.png")
forestImgSide = pygame.image.load("textures/forest1x2.png")
desertImg = pygame.image.load("textures/desert2x2.png")
desertImgSide = pygame.image.load("textures/desert1x2.png")
iceImg = pygame.image.load("textures/ice2x2.png")
iceImgLower = pygame.image.load("textures/ice2x1.png")

swampImg = pygame.image.load("textures/swamp2x2.png")
goldImg = pygame.image.load("textures/goldtest.png")

Baseimg = pygame.image.load("textures/base_placeholder.png").convert()
Baseimg.set_colorkey((255,0,255))

Soldierimg = pygame.image.load("textures/soldier.png").convert()
Robotimg = pygame.image.load("textures/robot.png").convert()
Tankimg = pygame.image.load("textures/tank.png").convert()

Soldierimg.set_colorkey((255,0,255))
Robotimg.set_colorkey((255,0,255))
Tankimg.set_colorkey((255,0,255))

black_border_img = pygame.image.load("textures/black_border.png").convert()
black_border_img.set_colorkey((255,0,255))

white_border_img = pygame.image.load("textures/white_border.png").convert()
white_border_img.set_colorkey((255,0,255))

logo = pygame.image.load("textures/Logo.png").convert_alpha()
logo.set_colorkey((255,0,255))

def draw_everything():      #draws everything
    #draw_background()
    #
    drawboard()
    drawitems()
    drawMouseHover()
    draw_player_stats((1000, 360))
    draw_bottom_buttons((1000, 875))

def draw_bottom_buttons(pos):       #Draws the menu and help button
    menu_button.draw(pos[0], pos[1], setDisplay)
    help_button.draw(pos[0] + 325, pos[1], setDisplay)


def draw_logo(pos):             #draw the logo
    setDisplay.blit(logo, pos)

def draw_player_stats(pos):     #draws the player information. also includes end of turn button draw
    x=0
    for i in Playerlist:
        Name_text = ButtonClass.Button(i.name, font_colour, font_size = fontsize, width = 200, height = 25, bgcolor = (0,0,0))
        Money_text = ButtonClass.Button("ƒ " + str(i.money), font_colour, font_size=fontsize, width = 200, height = 25, bgcolor = (50,50,50))

        Name_text.draw(pos[0], pos[1]+50*x, setDisplay)
        Money_text.draw(pos[0]+200, pos[1]+50*x, setDisplay)
        x+=1

    end_turn_button.draw(pos[0], pos[1]+50*(x), setDisplay)

def drawitems():        #draws units on field
    global VertCount
    global HoriCount
    for x in range(18):
        VertCount += 1
        for y in range(18):
            HoriCount += 1
            for u in Playerlist:
                if u.name == mapArray[x][y].owner:
                    color = u.color
            if mapArray[x][y].building != None:
                pygame.draw.rect(setDisplay, color, (x*50+1+Gameboard_offsetx, y*50+1+Gameboard_offsety, 48,48))
                setDisplay.blit(Baseimg, (x*50+1+Gameboard_offsetx, y*50+1+Gameboard_offsety))
            if mapArray[x][y].troops != []:
                j = 0
                for i in mapArray[x][y].troops:
                    if j == 0:
                        xoffset = 0
                        yoffset = 0
                    elif j == 1:
                        xoffset = 24
                        yoffset = 0
                    elif j == 2:
                        xoffset = 0
                        yoffset = 24
                    if i.Name == "Soldier":
                        pygame.draw.rect(setDisplay, color, (x*50+1+Gameboard_offsetx+xoffset, y*50+1+Gameboard_offsety+yoffset, 24,24))
                        setDisplay.blit(Soldierimg, (x*50+1+Gameboard_offsetx+xoffset, y*50+1+Gameboard_offsety+yoffset))
                    elif i.Name == "Robot":
                        pygame.draw.rect(setDisplay, color, (x*50+1+Gameboard_offsetx+xoffset, y*50+1+Gameboard_offsety+yoffset, 24,24))
                        setDisplay.blit(Robotimg, (x*50+1+Gameboard_offsetx+xoffset, y*50+1+Gameboard_offsety+yoffset))
                    elif i.Name == "Tank":
                        pygame.draw.rect(setDisplay, color, (x*50+1+Gameboard_offsetx+xoffset, y*50+1+Gameboard_offsety+yoffset, 24,24))
                        setDisplay.blit(Tankimg, (x*50+1+Gameboard_offsetx+xoffset, y*50+1+Gameboard_offsety+yoffset))
                    j +=1


VertCount = 0
HoriCount = 0
def drawboard():                        #draws the 
    #setDisplay.fill(Background_color)
    AnimationTick = pop()
    goldcounter = 0
    global VertCount
    global HoriCount
    if AnimationTick % 32 <= 4:
        waterImgThisTick = waterImg0
    elif AnimationTick % 32 <= 8:
        waterImgThisTick = waterImg1
    elif AnimationTick % 32 <= 12:
        waterImgThisTick = waterImg2
    elif AnimationTick % 32 <= 16:
        waterImgThisTick = waterImg3
    elif AnimationTick % 32 <= 20:
        waterImgThisTick = waterImg4
    elif AnimationTick % 32 <= 24:
        waterImgThisTick = waterImg5
    elif AnimationTick % 32 <= 28:
        waterImgThisTick = waterImg6
    else:
        waterImgThisTick = waterImg7

    for x in range(18):
        VertCount += 1
        for y in range(18):
            goldcounter += 1
            HoriCount += 1
            if mapArray[x][y].biome == "s" and VertCount % 2 == 1 and HoriCount % 2 == 1:
                  setDisplay.blit(swampImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "i":
                if VertCount % 2 == 1 and HoriCount % 2 == 0 and HoriCount %18 != 0 and VertCount % 18 != 0:
                    setDisplay.blit(iceImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif HoriCount %18 == 0 and VertCount % 18 != 0:
                     setDisplay.blit(iceImgLower, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "d":
                 if VertCount % 2 == 0 and HoriCount % 2 == 1 and HoriCount %18 != 0 and VertCount % 18 != 0:
                     setDisplay.blit(desertImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                 elif HoriCount %18 != 0 and VertCount % 18 == 0:
                     setDisplay.blit(desertImgSide, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "f":
                if VertCount % 2 == 0 and HoriCount % 2 == 0 and HoriCount %18 != 0 and VertCount % 18 != 0:
                     setDisplay.blit(forestImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif HoriCount %18 == 0 and VertCount % 18 != 0:
                     setDisplay.blit(forestImgLower, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif HoriCount %18 != 0 and VertCount % 18 == 0:
                     setDisplay.blit(forestImgSide, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif HoriCount %18 == 13 and VertCount % 18 == 13:
                     setDisplay.blit(forestImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))

            elif mapArray[x][y].biome == "f" and VertCount == 13 and HoriCount == 13:
                  setDisplay.blit(forestImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "w":
                setDisplay.blit(waterImgThisTick, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "g":
                if goldcounter in [134, 136, 170, 172]:
                    setDisplay.blit(goldImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))

    for x in range(18):
        for y in range(18):
            setDisplay.blit(black_border_img, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))

watercounter = 0

def pop():
    a = [1,2,3,4]  
    a.pop()
    global watercounter
    watercounter += 1
    return watercounter
 

def drawMouseHover():
    x = pygame.mouse.get_pos()
    posx = (x[0] - Gameboard_offsetx) - (x[0] - Gameboard_offsetx)%50 + Gameboard_offsetx
    posy = (x[1] - Gameboard_offsety) - (x[1] - Gameboard_offsety)%50 + Gameboard_offsety
    if posx >= Gameboard_offsetx and posx < Gameboard_offsetx + 900 and posy >= Gameboard_offsety and posy < Gameboard_offsety + 900:
        setDisplay.blit(white_border_img, (posx, posy))

def draw_background():
    posx = 0
    posy = 0
    while posx<window_width:
        while posy<window_height:
            setDisplay.blit(backgr, (posx,posy))
            posy += sizeTexture_parchment[1]
        posx += sizeTexture_parchment[0]
        posy = 0
    #setDisplay.blit(backgr, (0,0))