import pygame
import time
import Graphics_game
import config
import ButtonClass
import TextInputClass
import Player_functions
import PlayerMenu
import Player_functions

import copy

pygame.init()

display_width = 1500
display_height = 1000

width_textbox = 250
height_textbox = 24
width_color_box = 50
height_color_box = 24
width_textbox_color = 90

black = (0,0,0)
white = (255,255,255)
#colors are in a range of 0-255 (256 different entries)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_yellow = (239,254,54)
bright_blue = (64,132,244)
red = (200,0,0)
green = (0,200,0)
yellow = (236,220,26)
blue = (11,83,202)
mudgreen = (51,125,2)
mudyellow = (119,117,19)
mudred = (112,46,27)
mudblue = (1,66,137)
magenta = (255,0,255)
gray = (129,126,97)
mudorange = (120,95,7)
mudgray = (2,71,55)
weirdbrown = (169,78,16)
communist_red = (255,0,0)
swedish_blue = (0,0,255)
radioactive_green = (0,255,0)

fontsize = 20
#pygame.mixer.music.load("Title.mp3")

pos_name_boxX = 500
pos_name_boxY = 500

player1 = ButtonClass.Button("1", mudgray, font = "algerian", font_size = 30, bgcolor = gray, height = 88, width = 88)
player2 = ButtonClass.Button("2", black, font = "algerian", font_size = 30, bgcolor = mudorange, height = 88, width = 88)
player3 = ButtonClass.Button("3", mudgray, font = "algerian", font_size = 30, bgcolor = gray, height = 88, width = 88)
player4 = ButtonClass.Button("4", black, font = "algerian", font_size = 30, bgcolor = mudorange, height = 88, width = 88)
HowMany = ButtonClass.Button("Name(s) Of The Player(s)?", white, font = "algerian", font_size = 40)
Back = ButtonClass.Button("Back", black, font = "algerian", font_size = 20, bgcolor = mudyellow, height = 80, width = 180)
startgame = ButtonClass.Button("Start Game", black, font = "algerian", font_size = 20, bgcolor = mudorange, height = 80, width = 180)

playername1 = TextInputClass.TextBox(width_textbox, height_textbox, text = "Player1")
playername2 = TextInputClass.TextBox(width_textbox, height_textbox, text = "Player2")
playername3 = TextInputClass.TextBox(width_textbox, height_textbox, text = "Player3")
playername4 = TextInputClass.TextBox(width_textbox, height_textbox, text = "Player4")
playercolor1 = TextInputClass.TextBox(width_textbox_color, height_textbox, text = "Player Colour")
playercolor2 = TextInputClass.TextBox(width_textbox_color, height_textbox, text = "Player Colour")
playercolor3 = TextInputClass.TextBox(width_textbox_color, height_textbox, text = "Player Colour")
playercolor4 = TextInputClass.TextBox(width_textbox_color, height_textbox, text = "Player Colour")
player1colorR = TextInputClass.TextBox(width_color_box, height_color_box, text = "255", restriction = "int", maxlenght = 3, bgcolor = communist_red)
player1colorG = TextInputClass.TextBox(width_color_box, height_color_box, text = "0", restriction = "int", maxlenght = 3, bgcolor = radioactive_green)
player1colorB = TextInputClass.TextBox(width_color_box, height_color_box, text = "0", restriction = "int", maxlenght = 3, bgcolor = swedish_blue)
player2colorR = TextInputClass.TextBox(width_color_box, height_color_box, text = "0", restriction = "int", maxlenght = 3, bgcolor = communist_red)
player2colorG = TextInputClass.TextBox(width_color_box, height_color_box, text = "255", restriction = "int", maxlenght = 3, bgcolor = radioactive_green)
player2colorB = TextInputClass.TextBox(width_color_box, height_color_box, text = "0", restriction = "int", maxlenght = 3, bgcolor = swedish_blue)
player3colorR = TextInputClass.TextBox(width_color_box, height_color_box, text = "0", restriction = "int", maxlenght = 3, bgcolor = communist_red)
player3colorG = TextInputClass.TextBox(width_color_box, height_color_box, text = "0", restriction = "int", maxlenght = 3, bgcolor = radioactive_green)
player3colorB = TextInputClass.TextBox(width_color_box, height_color_box, text = "255", restriction = "int", maxlenght = 3, bgcolor = swedish_blue)
player4colorR = TextInputClass.TextBox(width_color_box, height_color_box, text = "0", restriction = "int", maxlenght = 3, bgcolor = communist_red)
player4colorG = TextInputClass.TextBox(width_color_box, height_color_box, text = "0", restriction = "int", maxlenght = 3, bgcolor = radioactive_green)
player4colorB = TextInputClass.TextBox(width_color_box, height_color_box, text = "0", restriction = "int", maxlenght = 3, bgcolor = swedish_blue)

def quitgame():
    pygame.quit()
    quit()

#gameDisplay = pygame.display.set_mode((display_width,display_height))
#pygame.display.set_caption("Frequency")
#clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def game():
    config.window="Main"
    config.firsttime = True

def calculate_color(R, G, B):       #takes strings of numbers and returns a color tuple (R,G,B)
    if len(R) == 0:
        R = 0
    else:
        R = int(R)
        if R >255:
            R = 255
    if len(G) == 0:
        G = 0
    else:
        G = int(G)
        if G >255:
            G = 255
    if len(B) == 0:
        B = 0
    else:
        B = int(B)
        if B >255:
            B = 255
    return (R,G,B)

def resetgame():
    print("game resetten")
    config.mapArray= copy.deepcopy(config.original_mapArray)    #derefferences original_maparray
    print(config.mapArray[0][0])
    print(config.original_mapArray[0][0])
    config.Playerlist = []
    config.PlayerIndex = 0
    config.TurnTick = 0
    config.selectedtile = (2,8)
    config.Selectedunits = []
    print("Game gereset")

def thirdscreen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Back.pressed():
                config.window="PlayerMenu"

            if startgame.pressed():
                config.window="Main"
                config.firsttime = True
                resetgame()
                if config.numofplayers >=1:
                    print("Player 1")
                    print(config.Playerlist)
                    Player_functions.PlayerCreation(playername1.text, playercolor1.bgcolor)
                    print("Player 1 appended")
                if config.numofplayers >=2:
                    print("Player 2")
                    print(config.Playerlist)
                    Player_functions.PlayerCreation(playername2.text, playercolor2.bgcolor)
                if config.numofplayers >=3:
                    print("Player 3")
                    print(config.Playerlist)
                    Player_functions.PlayerCreation(playername3.text, playercolor3.bgcolor)
                if config.numofplayers >=4:
                    print("Player 4")
                    print(config.Playerlist)
                    Player_functions.PlayerCreation(playername4.text, playercolor4.bgcolor)

            if config.numofplayers >=1:
                playername1.handlemousepress()
                player1colorR.handlemousepress()
                player1colorG.handlemousepress()
                player1colorB.handlemousepress()

            if config.numofplayers  >=2:
                playername2.handlemousepress()
                player2colorR.handlemousepress()
                player2colorG.handlemousepress()
                player2colorB.handlemousepress()

            if config.numofplayers  >=3:
                playername3.handlemousepress()
                player3colorR.handlemousepress()
                player3colorG.handlemousepress()
                player3colorB.handlemousepress()

            if config.numofplayers  >=4:
                playername4.handlemousepress()
                player4colorR.handlemousepress()
                player4colorG.handlemousepress()
                player4colorB.handlemousepress()

        if event.type == pygame.KEYDOWN:        #All keystrokes are handled here
            playername1.handle_char(event)
            playername2.handle_char(event)
            playername3.handle_char(event)
            playername4.handle_char(event)
            player1colorR.handle_char(event)
            player1colorG.handle_char(event)
            player1colorB.handle_char(event)
            player2colorR.handle_char(event)
            player2colorG.handle_char(event)
            player2colorB.handle_char(event)
            player3colorR.handle_char(event)
            player3colorG.handle_char(event)
            player3colorB.handle_char(event)
            player4colorR.handle_char(event)
            player4colorG.handle_char(event)
            player4colorB.handle_char(event)


    Graphics_game.draw_background()
    Back.draw(135,830,config.setDisplay)
    HowMany.draw(835,200,config.setDisplay)
    largeText = pygame.font.SysFont("algerian",90)
    TextSurf, TextRect = text_objects("Frequency", largeText)
    TextRect.center = ((display_width/4),(display_height/6))
    startgame.draw(835,830,config.setDisplay)
    

    if config.numofplayers >=1:
        playercolor1.bgcolor = calculate_color(player1colorR.text,player1colorG.text,player1colorB.text)    #sets the background color of the "player colour" bar into the calculated rgb
        playername1.draw((pos_name_boxX, pos_name_boxY))                                                    #draws the player name menu
        player1colorR.draw((pos_name_boxX+width_textbox, pos_name_boxY))                                    #Draws the red textbar
        player1colorG.draw((pos_name_boxX+width_textbox+width_color_box, pos_name_boxY))                    #Draws the green textbar
        player1colorB.draw((pos_name_boxX+width_textbox+2*width_color_box, pos_name_boxY))                  #Draws the blue textbar
        playercolor1.draw((pos_name_boxX+width_textbox+3*width_color_box, pos_name_boxY))                   #
    if config.numofplayers  >=2:
        playercolor2.bgcolor = calculate_color(player2colorR.text,player2colorG.text,player2colorB.text) 
        playername2.draw((pos_name_boxX, pos_name_boxY+25))
        player2colorR.draw((pos_name_boxX+width_textbox, pos_name_boxY+25))
        player2colorG.draw((pos_name_boxX+width_textbox+width_color_box, pos_name_boxY+25))
        player2colorB.draw((pos_name_boxX+width_textbox+2*width_color_box, pos_name_boxY+25))
        playercolor2.draw((pos_name_boxX+width_textbox+3*width_color_box, pos_name_boxY+25))
    if config.numofplayers  >=3:
        playercolor3.bgcolor = calculate_color(player3colorR.text,player3colorG.text,player3colorB.text) 
        playername3.draw((pos_name_boxX, pos_name_boxY+50))
        player3colorR.draw((pos_name_boxX+width_textbox, pos_name_boxY+50))
        player3colorG.draw((pos_name_boxX+width_textbox+width_color_box, pos_name_boxY+50))
        player3colorB.draw((pos_name_boxX+width_textbox+2*width_color_box, pos_name_boxY+50))
        playercolor3.draw((pos_name_boxX+width_textbox+3*width_color_box, pos_name_boxY+50))
    if config.numofplayers  >=4:
        playercolor4.bgcolor = calculate_color(player4colorR.text,player4colorG.text,player4colorB.text) 
        playername4.draw((pos_name_boxX, pos_name_boxY+75))
        player4colorR.draw((pos_name_boxX+width_textbox, pos_name_boxY+75))
        player4colorG.draw((pos_name_boxX+width_textbox+width_color_box, pos_name_boxY+75))
        player4colorB.draw((pos_name_boxX+width_textbox+2*width_color_box, pos_name_boxY+75))
        playercolor4.draw((pos_name_boxX+width_textbox+3*width_color_box, pos_name_boxY+75))
    
    

    config.setDisplay.blit(TextSurf, TextRect)


   # button("New Game",500,450,500,150,green,bright_green,secondscreen)
   # button("Quit",780,780,100,100,red,bright_red,quitgame)
   # button("Load Game",600,650,300,80,yellow,bright_yellow,quitgame)
   # button("Settings",620,780,100,100,blue,bright_blue,quitgame)
        
    #pygame.draw.rect(gameDisplay, red, (500,450,100,50))
    #if 500+100 > mouse[0] > 500 and 450+50 > mouse[1] > 450:
        #pygame.draw.rect(gameDisplay, bright_red, (500,450,100,50))
    #else:
        #pygame.draw.rect(gameDisplay, red, (500,450,100,50))

    #pygame.display.update()
    #clock.tick(15)

#game_intro()
#pygame.quit()
#quit()