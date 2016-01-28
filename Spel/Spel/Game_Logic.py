import pygame
import config
import Graphics_game
import Turn_Order

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

    