import pygame
import time
import Graphics_game
import config
import ButtonClass
import Music
import Saving

pygame.init()

display_width = 1500
display_height = 1000

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

fontsize = 20

NewGame = ButtonClass.Button("New Game", black, font = "algerian", font_size = 30, bgcolor = mudblue, height = 150, width = 500)
LoadGame = ButtonClass.Button("Load Game", black, font = "algerian", font_size = 20, bgcolor = mudgreen, height = 95, width = 300)
Settings = ButtonClass.Button("Settings", black, font = "algerian", font_size = 20, bgcolor = mudyellow, height = 88, width = 120)
QuitGame = ButtonClass.Button("Quit Game", black, font = "algerian", font_size = 20, bgcolor = mudred, height = 88, width = 120)

def quitgame():
    pygame.quit()
    quit()

#gameDisplay = pygame.display.set_mode((display_width,display_height))
#pygame.display.set_caption("Frequency")
#clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(config.setDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quit()
    else:
        pygame.draw.rect(config.setDisplay, ic, (x,y,w,h))

    smallText = pygame.font.SysFont("algerian",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    config.setDisplay.blit(textSurf, textRect)

def secondscreen():
    config.window="PlayerMenu"
    config.firsttime = True

def game_intro():
    
    #intro = True

    #while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if NewGame.pressed():
                config.window="PlayerMenu"
            if QuitGame.pressed():
                pygame.quit()
                quit()
            if Settings.pressed():
                config.window="SettingMenu"
            if LoadGame.pressed():
                Saving.load()
                config.window = "Main"
                config.firsttime = True


    #Music.MenuMusic()
    Graphics_game.draw_background()
    NewGame.draw(500,450,config.setDisplay)
    QuitGame.draw(765,780,config.setDisplay)
    LoadGame.draw(600,650,config.setDisplay)
    Settings.draw(615,780,config.setDisplay)
    #Graphics_game.draw_socialmedia((1200,800))
    largeText = pygame.font.SysFont("algerian",135)
    TextSurf, TextRect = text_objects("Frequency", largeText)
    TextRect.center = ((display_width/2),(display_height/3.5))
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