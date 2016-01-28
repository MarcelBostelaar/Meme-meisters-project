import config
import pygame
from Player import Player
import random

def PlayerCreation(name):
    #config.Playerlist = []

    newplayer = Player(name) #later on, ask for name of player
    biomepicked = False
    while not biomepicked:
        j = random.randint(1,4)
        if j == 1:
            if config.mapArray[0][0].building == None:
                config.mapArray[0][0].building = ["Base", 25]
                config.mapArray[0][0].owner = newplayer.name
                biomepicked = True
        elif j ==2:
            if config.mapArray[0][17].building == None:
                config.mapArray[0][17].building = ["Base", 25]
                config.mapArray[0][17].owner = newplayer.name
                biomepicked = True
        elif j ==3:
            if config.mapArray[17][0].building == None:
                config.mapArray[17][0].building = ["Base", 25]
                config.mapArray[17][0].owner = newplayer.name
                biomepicked = True
        elif j ==4:
            if config.mapArray[17][17].building == None:
                config.mapArray[17][17].building = ["Base", 25]
                config.mapArray[17][17].owner = newplayer.name
                biomepicked = True
    config.Playerlist.append(newplayer)