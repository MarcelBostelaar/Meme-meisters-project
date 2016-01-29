import pygame
import config
import Graphics_game
import Turn_Order
import ButtonClass

shit = ButtonClass.Button("Current Tile = " + str(config.selectedtile), (255,255,255), font_size = 30)

def Mousedown():
    stateMouse = pygame.mouse.get_pressed()
    if stateMouse[0] == 1:
        if Graphics_game.end_turn_button.pressed():
            Turn_Order.EndTurn()
        if Graphics_game.menu_button.pressed():
            config.window = "Esc_Menu"
            config.firsttime = True
        if Graphics_game.help_button.pressed():
            print("Help button pressed")
        SelectTile()

def SelectTile():
    mouseposition = pygame.mouse.get_pos()
    if mouseposition[0] >= config.Gameboard_offsetx and mouseposition[0] <= config.window_width+config.Gameboard_offsetx and mouseposition[1] >= config.Gameboard_offsety and mouseposition[1] <= config.Gameboard_offsety+config.window_height:
        i = (int((mouseposition[0]-config.Gameboard_offsetx)/50), int((mouseposition[1]-config.Gameboard_offsety)/50))
        if i[0] >= 0 and i[0]<=17 and i[1] >=0 and i[1]<= 17:
            config.selectedtile = i
        shit.text = "Current Tile = " + str(config.selectedtile)

def DrawTileInfo(pos):
        shit.draw(pos[0], pos[1], config.setDisplay)