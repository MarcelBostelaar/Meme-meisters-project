import pygame
import config
import Graphics_game
import Turn_Order
import ButtonClass
import Music

white = (255,255,255)
fontsize = 30

Line_Tile = ButtonClass.Button("", white, font_size = fontsize)
Line_Tile_Biome = ButtonClass.Button("", white, font_size = fontsize)
Line_Tile_Owner = ButtonClass.Button("", white, font_size = fontsize)

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
            config.window = "Help_Menu"
            config.firsttime = True
        SelectTile()

def SelectTile():
    mouseposition = pygame.mouse.get_pos()
    if mouseposition[0] >= config.Gameboard_offsetx and mouseposition[0] <= config.window_width+config.Gameboard_offsetx and mouseposition[1] >= config.Gameboard_offsety and mouseposition[1] <= config.Gameboard_offsety+config.window_height:
        i = (int((mouseposition[0]-config.Gameboard_offsetx)/50), int((mouseposition[1]-config.Gameboard_offsety)/50))
        if i[0] >= 0 and i[0]<=17 and i[1] >=0 and i[1]<= 17:
            config.selectedtile = i
            Music.MouseClick()

        Tile_selected = config.mapArray[config.selectedtile[0]][config.selectedtile[1]]

        if Tile_selected.biome == "w":
            Line_Tile_Biome.text = "Biome: Water"
        elif Tile_selected.biome == "d":
            Line_Tile_Biome.text = "Biome: Desert"
        elif Tile_selected.biome == "i":
            Line_Tile_Biome.text = "Biome: Ice"
        elif Tile_selected.biome == "s":
            Line_Tile_Biome.text = "Biome: Swamp"
        elif Tile_selected.biome == "f":
            Line_Tile_Biome.text = "Biome: Forest"
        else:
            Line_Tile_Biome.text = "Biome: Gems"

        Line_Tile.text = "Current Tile = " + str(config.selectedtile)


def DrawTileInfo(pos):
    Line_Tile.draw(pos[0], pos[1], config.setDisplay)
    Line_Tile_Biome.draw(pos[0], pos[1]+30, config.setDisplay)

def Unit_Options():
    print("lol")

def move_unit(unit, pos_current, pos_target):
    x=0
    for i in config.mapArray[pos_current[0]][pos_current[1]].troops:
        if unit == i.Name:
            config.mapArray[pos_target[0]][pos_target[1]].troops.append(i)
            config.mapArray[pos_current[0]][pos_current[1]].troops.pop(x)
            return True
        x+=1
    return False
