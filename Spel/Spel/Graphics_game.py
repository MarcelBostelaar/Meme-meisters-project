import pygame
import config
import ButtonClass
import random
import Game_Logic
import Player_functions
import Units

Background_color = (0,0,0)

font_colour = (255,255,255)
fontsize = 30

end_turn_button = ButtonClass.Button("End Turn", font_colour, font_size=fontsize, width = 400, height = 75, bgcolor = (255,100,0))
menu_button = ButtonClass.Button("Menu", font_colour, font_size=fontsize, width = 300, height = 75, bgcolor = (255,100,0))
help_button = ButtonClass.Button("?", font_colour, font_size=fontsize, width = 75, height = 75, bgcolor = (255,100,0))
BuyTank = ButtonClass.Button("Buy Tank", font_colour, font_size = fontsize, width = 150, height = 30, bgcolor = (60,60,60))
BuyRobot = ButtonClass.Button("Buy Robot", font_colour, font_size = fontsize, width = 150, height = 30, bgcolor = (60,60,60))
BuySoldier = ButtonClass.Button("Buy Soldier", font_colour, font_size = fontsize, width = 150, height = 30, bgcolor = (60,60,60))
BuyBarracks = ButtonClass.Button("Buy Barracks", font_colour, font_size = fontsize, width = 150, height = 30, bgcolor = (60,60,60))
BuyBarracks.draw(1230, 500, config.setDisplay)
BuyTank.draw(1230, 500, config.setDisplay)
BuyRobot.draw(1230, 535, config.setDisplay)
BuySoldier.draw(1230, 570, config.setDisplay)


Troop1 = ButtonClass.Button("", font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
Troop2 = ButtonClass.Button("", font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
Troop3 = ButtonClass.Button("", font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
Troop1.draw(1010, 610, config.setDisplay)
Troop2.draw(1136, 610, config.setDisplay)
Troop3.draw(1262, 610, config.setDisplay)

MoveLeft = ButtonClass.Button("<", font_colour, font_size = fontsize, width = 25, height = 25, bgcolor = (25,25,25))
MoveUp = ButtonClass.Button("^", font_colour, font_size = fontsize, width = 25, height = 25, bgcolor = (25,25,25))
MoveRight = ButtonClass.Button(">", font_colour, font_size = fontsize, width = 25, height = 25, bgcolor = (25,25,25))
MoveDown = ButtonClass.Button("v", font_colour, font_size = fontsize, width = 25, height = 25, bgcolor = (25,25,25))
MoveLeft.draw(1115, 542, config.setDisplay)
MoveUp.draw(1152, 505, config.setDisplay)
MoveRight.draw(1189, 542, config.setDisplay)
MoveDown.draw(1152, 579, config.setDisplay)

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

frame = pygame.image.load("textures/Overlay.png")

swampImg = pygame.image.load("textures/swamp2x2.png")
goldImg = pygame.image.load("textures/goldtest.png")

Baseimg = pygame.image.load("textures/base_placeholder.png").convert()
Baseimg.set_colorkey((255,0,255))

Soldierimg = pygame.image.load("textures/soldier.png").convert_alpha()
Robotimg = pygame.image.load("textures/robot.png").convert_alpha()
Tankimg = pygame.image.load("textures/tank.png").convert_alpha()
Barrackimg = pygame.image.load("textures/Barracks.png").convert_alpha()
Boatimg = pygame.image.load("textures/Boat.png").convert_alpha()

Soldierimg.set_colorkey((255,0,255))
Robotimg.set_colorkey((255,0,255))
Tankimg.set_colorkey((255,0,255))

black_border_img = pygame.image.load("textures/black_border.png").convert_alpha()

white_border_img = pygame.image.load("textures/white_border.png").convert()
white_border_img.set_colorkey((255,0,255))

HUDbackground = pygame.image.load("textures/HUDbg.png").convert_alpha()
logo = pygame.image.load("textures/Logo.png").convert_alpha()
currenttile = None

black = (0,0,0)
logo.set_colorkey((255,0,255))

health = ButtonClass.Button("", (0,255,0), font_size = fontsize)

attack_button = ButtonClass.Button("Attack", (255,255,255), font_size = fontsize, width = 150, height = 30, bgcolor = (255,155,155))
attack_button.draw(1230, 535, config.setDisplay)

def draw_everything():      #draws everything
    #draw_background()
    #
    drawboard()
    drawitems()
    drawMouseHover()
    draw_player_stats((1000, 150))
    draw_bottom_buttons((1000, 875))
    draw_HUD((1010, 500))

def draw_bottom_buttons(pos):       #Draws the menu and help button
    menu_button.draw(pos[0], pos[1], config.setDisplay)
    help_button.draw(pos[0] + 325, pos[1], config.setDisplay)


def draw_logo(pos):             #draw the logo
    config.setDisplay.blit(logo, pos)
TileX = 0


def draw_HUD(pos):
    global currenttile
    global TileX
    Tile_selected = config.mapArray[config.selectedtile[0]][config.selectedtile[1]]
    
    config.setDisplay.blit(HUDbackground, (pos[0]-10,pos[1]-10))

    if Tile_selected.biome == "w":
        currenttile = pygame.image.load("textures/water.png").convert_alpha()
    elif Tile_selected.biome == "d":
        currenttile = pygame.image.load("textures/desert2x2.png").convert_alpha()
    elif Tile_selected.biome == "i":
        currenttile = pygame.image.load("textures/ice2x2.png").convert_alpha()
    elif Tile_selected.biome == "s":
        currenttile = pygame.image.load("textures/swamp2x2.png").convert_alpha()
    elif Tile_selected.biome == "f":
        currenttile = pygame.image.load("textures/forest2x2.png").convert_alpha()
    elif Tile_selected.biome == "g":
        currenttile = pygame.image.load("textures/goldtest.png").convert_alpha()
    if config.selectedtroop in [1, 2, 3]:
        MoveLeft = ButtonClass.Button("<", black, font_size = fontsize, width = 25, height = 25, bgcolor = (200,200,200))
        MoveUp = ButtonClass.Button("^", black, font_size = fontsize, width = 25, height = 25, bgcolor = (200,200,200))
        MoveRight = ButtonClass.Button(">", black, font_size = fontsize, width = 25, height = 25, bgcolor = (200,200,200))
        MoveDown = ButtonClass.Button("v", black, font_size = fontsize, width = 25, height = 25, bgcolor = (200,200,200))
    else:
        MoveLeft = ButtonClass.Button("<", font_colour, font_size = fontsize, width = 25, height = 25, bgcolor = (25,25,25))
        MoveUp = ButtonClass.Button("^", font_colour, font_size = fontsize, width = 25, height = 25, bgcolor = (25,25,25))
        MoveRight = ButtonClass.Button(">", font_colour, font_size = fontsize, width = 25, height = 25, bgcolor = (25,25,25))
        MoveDown = ButtonClass.Button("v", font_colour, font_size = fontsize, width = 25, height = 25, bgcolor = (25,25,25))
    MoveLeft.draw(1115, 542, config.setDisplay)
    MoveUp.draw(1152, 505, config.setDisplay)
    MoveRight.draw(1189, 542, config.setDisplay)
    MoveDown.draw(1152, 579, config.setDisplay)

#    BuyButton = ButtonClass.Button("Buy", font_colour, font_size = fontsize, width = 150, height = 100, bgcolor = (155,155,155))
#    BuyButton.draw(1230, 500, config.setDisplay)
    if Tile_selected.building != None:
        BuyTank = ButtonClass.Button("Buy Tank", font_colour, font_size = fontsize, width = 150, height = 30, bgcolor = (155,155,155))
        BuyRobot = ButtonClass.Button("Buy Robot", font_colour, font_size = fontsize, width = 150, height = 30, bgcolor = (155,155,155))
        BuySoldier = ButtonClass.Button("Buy Soldier", font_colour, font_size = fontsize, width = 150, height = 30, bgcolor = (155,155,155))
        BuyTank.draw(1230, 500, config.setDisplay)
        BuyRobot.draw(1230, 535, config.setDisplay)
        BuySoldier.draw(1230, 570, config.setDisplay)
    if Tile_selected.troops != []:
        BuyBarracks = ButtonClass.Button("Buy Barracks", font_colour, font_size = fontsize, width = 150, height = 30, bgcolor = (140,99,60))
        BuyBarracks.draw(1230, 500, config.setDisplay)
        attack_button.draw(1230, 535, config.setDisplay)
#    config.setDisplay.blit(HUDbackground, (pos[0]-10,pos[1]-10))
#    config.setDisplay.blit(MoveLeft, (pos[0]+110,pos[1]+37))
#    config.setDisplay.blit(MoveUp, (pos[0]+147,pos[1]))
#    config.setDisplay.blit(MoveRight, (pos[0]+184,pos[1]+37))
#    config.setDisplay.blit(MoveDown, (pos[0]+147,pos[1]+74))
    if Tile_selected.troops != []:
        if config.memetick == 0:
            for i in Tile_selected.troops:
                Unit = i.Name
                config.memetick = 1
                config.Selectedunits.append(Unit)

        if len(Tile_selected.troops) >= 3:
            Troop1 = ButtonClass.Button(config.Selectedunits[0], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
            Troop2 = ButtonClass.Button(config.Selectedunits[1], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
            Troop3 = ButtonClass.Button(config.Selectedunits[2], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
            if config.selectedtroop == 1:
                Troop1 = ButtonClass.Button(config.Selectedunits[0], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (155,155,155))
            elif config.selectedtroop == 2:
                Troop2 = ButtonClass.Button(config.Selectedunits[1], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (155,155,155))
            elif config.selectedtroop == 3:
                Troop3 = ButtonClass.Button(config.Selectedunits[2], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (155,155,155))
            Troop1.draw(1010, 610, config.setDisplay)
            Troop2.draw(1136, 610, config.setDisplay)
            Troop3.draw(1262, 610, config.setDisplay)
        elif len(Tile_selected.troops) >= 2:
            Troop1 = ButtonClass.Button(config.Selectedunits[0], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
            Troop2 = ButtonClass.Button(config.Selectedunits[1], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
            if config.selectedtroop == 1:
                Troop1 = ButtonClass.Button(config.Selectedunits[0], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (155,155,155))
            elif config.selectedtroop == 2:
                Troop2 = ButtonClass.Button(config.Selectedunits[1], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (155,155,155))
            Troop1.draw(1010, 610, config.setDisplay)
            Troop2.draw(1136, 610, config.setDisplay)
        else: 
            Troop1 = ButtonClass.Button(config.Selectedunits[0], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
            if config.selectedtroop == 1:
                Troop1 = ButtonClass.Button(config.Selectedunits[0], font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (155,155,155))
            Troop1.draw(1010, 610, config.setDisplay)
    else:
        Troop1 = ButtonClass.Button("", font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
        Troop2 = ButtonClass.Button("", font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
        Troop3 = ButtonClass.Button("", font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
        config.selectedtroop = 0

    #if config.selectedtroop == 1:
    #    Troop1 = ButtonClass.Button("", font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (155,155,155))
    #    Troop1.draw(1010, 610, config.setDisplay)
    #elif config.selectedtroop == 2:
    #    Troop2 = ButtonClass.Button("", font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (155,155,155))
    #    Troop2.draw(1010, 610, config.setDisplay)
    #elif config.selectedtroop == 3:
    #    Troop3 = ButtonClass.Button("", font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (155,155,155))
    #    Troop3.draw(1010, 610, config.setDisplay)
    #config.selectedtroop = 0
    #del config.Selectedunits[:]

#    for i in Tile_selected.troops:
#        if Tile_selected.troops != []:
#            Unit = i.Name
#            Troop = ButtonClass.Button(Unit, font_colour, font_size=fontsize, width = 120 , height = 30, bgcolor = (100,100,100))
#            Troop.draw(1010 + TileX , 610 ,config.setDisplay)
#            TileX += 126 
#    TileX = 0     
    config.setDisplay.blit(currenttile, pos)


def draw_player_stats(pos):     #draws the player information. also includes end of turn button draw
    x=0
    for i in config.Playerlist:
        Name_text = ButtonClass.Button(i.name, font_colour, font_size = fontsize, width = 200, height = 25, bgcolor = i.color)
        Money_text = ButtonClass.Button("ƒ " + str(i.money), font_colour, font_size=fontsize, width = 200, height = 25, bgcolor = (50,50,50))

        Name_text.draw(pos[0], pos[1]+50*x, config.setDisplay)
        Money_text.draw(pos[0]+200, pos[1]+50*x, config.setDisplay)
        x+=1

    end_turn_button.draw(pos[0], pos[1]+50*(x), config.setDisplay)
    config.setDisplay.blit(frame, (pos[0], pos[1]+50*config.PlayerIndex))

#def turnoverlay(pos):

#        setDisplay.blit(frame,(pos[0], pos[1]+50*PlayerIndex, setDisplay))
#        pygame.display.update()


def drawitems():        #draws units on field
    global VertCount
    global HoriCount
    for x in range(18):
        VertCount += 1
        for y in range(18):
            HoriCount += 1
            for u in config.Playerlist:
                if u.name == config.mapArray[x][y].owner:
                    color = u.color
            if config.mapArray[x][y].building != None:
                pygame.draw.rect(config.setDisplay, color, (x*50+1+config.Gameboard_offsetx, y*50+1+config.Gameboard_offsety, 48,48))
                config.setDisplay.blit(Baseimg, (x*50+1+config.Gameboard_offsetx, y*50+1+config.Gameboard_offsety))
                health.text = str(config.mapArray[x][y].building.Power)
                health.draw(x*50+1+config.Gameboard_offsetx, y*50+1+config.Gameboard_offsety, config.setDisplay)
            if config.mapArray[x][y].troops != []:
                j = 0
                for i in config.mapArray[x][y].troops:
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
                        pygame.draw.rect(config.setDisplay, color, (x*50+1+config.Gameboard_offsetx+xoffset, y*50+1+config.Gameboard_offsety+yoffset, 24,24))
                        config.setDisplay.blit(Soldierimg, (x*50+1+config.Gameboard_offsetx+xoffset, y*50+1+config.Gameboard_offsety+yoffset))
                    elif i.Name == "Robot":
                        pygame.draw.rect(config.setDisplay, color, (x*50+1+config.Gameboard_offsetx+xoffset, y*50+1+config.Gameboard_offsety+yoffset, 24,24))
                        config.setDisplay.blit(Robotimg, (x*50+1+config.Gameboard_offsetx+xoffset, y*50+1+config.Gameboard_offsety+yoffset))
                    elif i.Name == "Tank":
                        pygame.draw.rect(config.setDisplay, color, (x*50+1+config.Gameboard_offsetx+xoffset, y*50+1+config.Gameboard_offsety+yoffset, 24,24))
                        config.setDisplay.blit(Tankimg, (x*50+1+config.Gameboard_offsetx+xoffset, y*50+1+config.Gameboard_offsety+yoffset))
                    elif i.Name == "Boat":
                        pygame.draw.rect(config.setDisplay, color, (x*50+1+config.Gameboard_offsetx, y*50+1+config.Gameboard_offsety, 48,48))
                        config.setDisplay.blit(Boatimg, (x*50+1+config.Gameboard_offsetx, y*50+1+config.Gameboard_offsety))
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
            if config.mapArray[x][y].biome == "s" and VertCount % 2 == 1 and HoriCount % 2 == 1:
                  config.setDisplay.blit(swampImg, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
            elif config.mapArray[x][y].biome == "i":
                if VertCount % 2 == 1 and HoriCount % 2 == 0 and HoriCount %18 != 0 and VertCount % 18 != 0:
                    config.setDisplay.blit(iceImg, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
                elif HoriCount %18 == 0 and VertCount % 18 != 0:
                     config.setDisplay.blit(iceImgLower, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
            elif config.mapArray[x][y].biome == "d":
                 if VertCount % 2 == 0 and HoriCount % 2 == 1 and HoriCount %18 != 0 and VertCount % 18 != 0:
                     config.setDisplay.blit(desertImg, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
                 elif HoriCount %18 != 0 and VertCount % 18 == 0:
                     config.setDisplay.blit(desertImgSide, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
            elif config.mapArray[x][y].biome == "f":
                if VertCount % 2 == 0 and HoriCount % 2 == 0 and HoriCount %18 != 0 and VertCount % 18 != 0:
                     config.setDisplay.blit(forestImg, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
                elif HoriCount %18 == 0 and VertCount % 18 != 0:
                     config.setDisplay.blit(forestImgLower, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
                elif HoriCount %18 != 0 and VertCount % 18 == 0:
                     config.setDisplay.blit(forestImgSide, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
                elif HoriCount %18 == 13 and VertCount % 18 == 13:
                     config.setDisplay.blit(forestImg, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))

            elif config.mapArray[x][y].biome == "f" and VertCount == 13 and HoriCount == 13:
                  setDisplay.blit(forestImg, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
            elif config.mapArray[x][y].biome == "w":
                config.setDisplay.blit(waterImgThisTick, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))
            elif config.mapArray[x][y].biome == "g":
                if goldcounter in [134, 136, 170, 172]:
                    config.setDisplay.blit(goldImg, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))

    for x in range(18):
        for y in range(18):
            config.setDisplay.blit(black_border_img, (x*50+config.Gameboard_offsetx, y*50+config.Gameboard_offsety))

watercounter = 0

def pop():
    a = [1,2,3,4]  
    a.pop()
    global watercounter
    watercounter += 1
    return watercounter
 

def drawMouseHover():
    x = pygame.mouse.get_pos()
    posx = (x[0] - config.Gameboard_offsetx) - (x[0] - config.Gameboard_offsetx)%50 + config.Gameboard_offsetx
    posy = (x[1] - config.Gameboard_offsety) - (x[1] - config.Gameboard_offsety)%50 + config.Gameboard_offsety
    if posx >= config.Gameboard_offsetx and posx < config.Gameboard_offsetx + 900 and posy >= config.Gameboard_offsety and posy < config.Gameboard_offsety + 900:
        config.setDisplay.blit(white_border_img, (posx, posy))

def draw_background():
    posx = 0
    posy = 0
    while posx<config.window_width:
        while posy<config.window_height:
            config.setDisplay.blit(backgr, (posx,posy))
            posy += sizeTexture_parchment[1]
        posx += sizeTexture_parchment[0]
        posy = 0
    #setDisplay.blit(backgr, (0,0))
