import os, sys
import pygame
import random
from Player import Player
from Tile import Tile
from ButtonClass import Button
import EscMenu
import config
import Graphics_game
import Player_functions
import Debug_screen
import Game_Logic
import Units
#import MainMenu

pygame.init()


Player_functions.PlayerCreation(4)

config.Playerlist[0].name="henk"
config.Playerlist[1].name="freek"
config.Playerlist[2].name="klaas"

config.Playerlist[0].money=420
config.Playerlist[1].money=1337
config.Playerlist[2].money=6969

newunit = Units.Unit()
newunit.Soldier()
print(newunit.Name)
for i in range(4):
    config.mapArray[4][4].troops.append(newunit)
config.mapArray[4][4].troops.pop(2)

while True:


    if config.window == "Main":
        if config.firsttime:
            Graphics_game.draw_background()
            Graphics_game.draw_logo((1000, 50))
            config.firsttime = False
        Graphics_game.draw_everything()
        if config.debug == True:
            Debug_screen.Draw((1000,0))

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    config.window = "Esc_Menu"
                    config.firsttime = True
                if event.key == pygame.K_F3:
                    config.debug = not config.debug
                    config.firsttime = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                Game_Logic.Mousedown()


    if config.window == "Esc_Menu":
        if config.firsttime:
            EscMenu.Escape_Menu_Draw(((config.window_width-EscMenu.MenuWidth)/2,((config.window_height-EscMenu.MenuHeight)/2)), config.setDisplay)
            config.firsttime = False
        EscMenu.EscM_detect_presses()

    
                
#    config.setDisplay.blit(pygame.transform.scale(config.setDisplay, (600, 600)), (0,0))
    pygame.display.update()
    config.fpsTime.tick(config.fps)