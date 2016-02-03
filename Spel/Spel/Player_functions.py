import config
import pygame
from Player import Player
import random
import Units

def PlayerCreation(name, color):
    #config.Playerlist = []

    newplayer = Player(name, color) #later on, ask for name of player
    biomepicked = False
    base = Units.Unit()
    base.Base()
    while not biomepicked:
        j = random.randint(1,4)
        if j == 1:
            if config.mapArray[0][0].building == None:
                config.mapArray[0][0].building = base
                config.mapArray[0][0].owner = newplayer.name
                biomepicked = True
        elif j ==2:
            if config.mapArray[0][17].building == None:
                config.mapArray[0][17].building = base
                config.mapArray[0][17].owner = newplayer.name
                biomepicked = True
        elif j ==3:
            if config.mapArray[17][0].building == None:
                config.mapArray[17][0].building = base
                config.mapArray[17][0].owner = newplayer.name
                biomepicked = True
        elif j ==4:
            if config.mapArray[17][17].building == None:
                config.mapArray[17][17].building = base
                config.mapArray[17][17].owner = newplayer.name
                biomepicked = True
    config.Playerlist.append(newplayer)