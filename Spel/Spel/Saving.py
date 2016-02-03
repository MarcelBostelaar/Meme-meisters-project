import pygame
import config
import pickle

def save():
    picklelist = []
    picklelist.append(config.Playerlist)
    picklelist.append(config.PlayerIndex)
    picklelist.append(config.TurnTick)
    picklelist.append(config.mapArray)
    picklelist.append(config.selectedtile)
    picklelist.append(config.selectedtroop)
    picklelist.append(config.Selectedunits)
    picklelist.append(config.unit)

    pickle.dump(picklelist, open("GameSave.dat", "wb"))

def load():
    picklelist = pickle.load(open("GameSave.dat", "rb"))

    config.Playerlist = picklelist[0]
    config.PlayerIndex = picklelist[1]
    config.TurnTick = picklelist[2]
    config.mapArray = picklelist[3]
    config.selectedtile = picklelist[4]
    config.selectedtroop = picklelist[5]
    config.Selectedunits = picklelist[6]
    config.unit = picklelist[7]