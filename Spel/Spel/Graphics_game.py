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
forestImg = pygame.image.load("textures/forest.png")
desertImg = pygame.image.load("textures/desert.png")
iceImg = pygame.image.load("textures/ice.png")
swampImg = pygame.image.load("textures/swamp.png")
goldImg = pygame.image.load("textures/gold.png")

Baseimg = pygame.image.load("textures/base_placeholder.png").convert()
Baseimg.set_colorkey((255,0,255))

black_border_img = pygame.image.load("textures/black_border.png").convert()
black_border_img.set_colorkey((255,0,255))

white_border_img = pygame.image.load("textures/white_border.png").convert()
white_border_img.set_colorkey((255,0,255))

logo = pygame.image.load("textures/logo.png").convert()
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
    for x in range(18):
        for y in range(18):
            if mapArray[x][y].owner != None:
                setDisplay.blit(Baseimg, (x*50+1+Gameboard_offsetx, y*50+1+Gameboard_offsety))



def drawboard():                        #draws the 
    #setDisplay.fill(Background_color)
    AnimationTick = pop()
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
                if AnimationTick % 32 <= 4:
                    setDisplay.blit(waterImg0, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif AnimationTick % 32 <= 8:
                    setDisplay.blit(waterImg1, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif AnimationTick % 32 <= 12:
                    setDisplay.blit(waterImg2, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif AnimationTick % 32 <= 16:
                    setDisplay.blit(waterImg3, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif AnimationTick % 32 <= 20:
                    setDisplay.blit(waterImg4, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif AnimationTick % 32 <= 24:
                    setDisplay.blit(waterImg5, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                elif AnimationTick % 32 <= 28:
                    setDisplay.blit(waterImg6, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
                else:
                    setDisplay.blit(waterImg7, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
            elif mapArray[x][y].biome == "g":
                  setDisplay.blit(goldImg, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))
    
    for x in range(18):
        for y in range(18):
            setDisplay.blit(black_border_img, (x*50+Gameboard_offsetx, y*50+Gameboard_offsety))

counter = 0

def pop():
    a = [1,2,3,4]  
    a.pop()
    global counter
    counter += 1
    return counter
 

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