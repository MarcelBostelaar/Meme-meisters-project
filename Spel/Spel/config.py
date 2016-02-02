from Tile import Tile
import pygame

window = "MainMenu"
debug=False
music = False

gamename = "Frequency"
window_height = 1000
window_width = 1500

Gameboard_offsetx = 50
Gameboard_offsety = 50

fps = 60
fpsTime = pygame.time.Clock()


PlayerIndex = 0
TurnTick = 0

mapArray = [
    [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
    [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
    [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
    [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
    [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
    [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
    [Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("s"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("i"), Tile("i"), Tile("i"), Tile("i"), Tile("i")],
    [Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("g"), Tile("g"), Tile("g"), Tile("g"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w")],
    [Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("g"), Tile("g"), Tile("g"), Tile("g"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w")],
    [Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("g"), Tile("g"), Tile("g"), Tile("g"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w")],
    [Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("g"), Tile("g"), Tile("g"), Tile("g"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w")],
    [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
    [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
    [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
    [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
    [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
    [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")],
    [Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("d"), Tile("w"), Tile("w"), Tile("w"), Tile("w"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f"), Tile("f")] ]

setDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(gamename)

Playerlist = []

firsttime = True

selectedtile = (2,8)
SelectedTroop = None