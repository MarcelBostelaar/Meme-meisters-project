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

pygame.init()


Player_functions.PlayerCreation(4)

config.Playerlist[0].name="henk"
config.Playerlist[1].name="freek"
config.Playerlist[2].name="klaas"

config.Playerlist[0].money=420
config.Playerlist[1].money=1337
config.Playerlist[2].money=6969


while True:
    
    if config.window == "Main":
        Graphics_game.draw_everything()
        if config.debug == True:
            Debug_screen.Draw((900,0))

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    config.window = "Esc_Menu"
                if event.key == pygame.K_F3:
                    config.debug = not config.debug
            if event.type == pygame.MOUSEBUTTONDOWN:
                Game_Logic.Mousedown()


    if config.window == "Esc_Menu":
        EscMenu.Escape_Menu_Draw(((config.window_width-EscMenu.MenuWidth)/2,((config.window_height-EscMenu.MenuHeight)/2)), config.setDisplay)
        EscMenu.EscM_detect_presses()

    
                
#    config.setDisplay.blit(pygame.transform.scale(config.setDisplay, (600, 600)), (0,0))
    pygame.display.update()
    config.fpsTime.tick(config.fps)