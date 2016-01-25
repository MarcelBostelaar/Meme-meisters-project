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

pygame.init()


Player_functions.PlayerCreation(3)


while True:
    
    if config.window == "Main":
        Graphics_game.drawboard()
        Graphics_game.drawitems()
        Graphics_game.drawMouseHover()
        if config.debug == True:
            Debug_screen.Draw((900,0))

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    config.window = "Esc_Menu"
                if event.key == pygame.K_F3:
                    config.debug = not config.debug


    if config.window == "Esc_Menu":
        EscMenu.Escape_Menu_Draw(((config.window_width-EscMenu.MenuWidth)/2,((config.window_height-EscMenu.MenuHeight)/2)), config.setDisplay)
        EscMenu.EscM_detect_presses()
        print(config.window)

    
                
    
    pygame.display.update()
    config.fpsTime.tick(config.fps)