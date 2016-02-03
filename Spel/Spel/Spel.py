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
import Turn_Order
import MainMenu
import PlayerMenu
import PlayerNameMenu
import Music
import SettingMenu
import HelpMenu

pygame.init()


Player_functions.PlayerCreation("henk", (0,0,0))
Player_functions.PlayerCreation("freek", (0,255,0))
Player_functions.PlayerCreation("klaas", (0,0,255))
#Player_functions.PlayerCreation("sjaak", (0,255,255))

config.Playerlist[0].money=49000
config.Playerlist[1].money=49000
config.Playerlist[2].money=49000
#config.Playerlist[3].money=49000

newunit = Units.Unit()
newunit.Tank()
print(newunit.Name)
for i in range(3):
    config.mapArray[1][0].troops.append(newunit)

newunit = Units.Unit()
newunit.Soldier()
config.mapArray[3][3].troops.append(newunit)
newunit = Units.Unit()
newunit.Robot()
config.mapArray[3][3].troops.append(newunit)
newunit = Units.Unit()
newunit.Tank()
config.mapArray[3][3].troops.append(newunit)

newunit = Units.Unit()
newunit.Soldier()
config.mapArray[3][13].troops.append(newunit)
newunit = Units.Unit()
newunit.Robot()
config.mapArray[3][13].troops.append(newunit)

newunit = Units.Unit()
newunit.Tank()
config.mapArray[14][13].troops.append(newunit)

config.mapArray[3][3].owner = config.Playerlist[2].name
config.mapArray[3][4].owner = config.Playerlist[0].name


#Game_Logic.move_unit("Tank", (3,3), (16, 16))

while True:
    if config.window == "MainMenu":
        #pygame.mixer.music.stop()
        if config.firsttime:
            if config.music == True:
                Music.MenuMusic()
            else:
                pygame.mixer.music.stop()
            config.firsttime = False
        MainMenu.game_intro()
    if config.window == "PlayerMenu":
        PlayerMenu.secondscreen()
    if config.window == "PlayerNameMenu":
        PlayerNameMenu.thirdscreen()
    if config.window == "SettingMenu":
        SettingMenu.settingscreen()



    if config.window == "Main":
        if config.firsttime:
            Music.GameMusic()
            Graphics_game.draw_background()
            Graphics_game.draw_logo((1000, 50))
            config.firsttime = False
        Graphics_game.draw_everything()
        if config.debug == True:
            Debug_screen.Draw((1000,0))
        Game_Logic.DrawTileInfo((600, 600))

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
                if event.key == pygame.K_F4:
                    Turn_Order.OrderMatrix(1)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                Game_Logic.Mousedown()


    if config.window == "Esc_Menu":
        if config.firsttime:
            EscMenu.Escape_Menu_Draw(((config.window_width-EscMenu.MenuWidth)/2,((config.window_height-EscMenu.MenuHeight)/2)), config.setDisplay)
            config.firsttime = False
        EscMenu.EscM_detect_presses()

    if config.window == "Help_Menu":
        if config.firsttime:
            HelpMenu.Help_Menu_Draw(((config.window_width-HelpMenu.MenuWidth)/2,((config.window_height-HelpMenu.MenuHeight)/2)), config.setDisplay)
            config.firsttime = False
        HelpMenu.HelpM_detect_presses()
    
                
#    config.setDisplay.blit(pygame.transform.scale(config.setDisplay, (600, 600)), (0,0))
    pygame.display.update()
    config.fpsTime.tick(config.fps)
    