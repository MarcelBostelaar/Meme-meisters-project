import config
import Graphics_game

def OrderMatrix(increment):
    config.TurnTick += increment
    if config.TurnTick == 4:
        EndTurn()


def EndTurn():
    GiveMoney()
    config.TurnTick = 0
    config.PlayerIndex +=1
    print (str(config.PlayerIndex) + "'s turn has ended")
    if config.PlayerIndex == 4:
        config.PlayerIndex = 0
    #Graphics_game.draw_background()

def GiveMoney():
    player = config.Playerlist[config.PlayerIndex].name

    moneytogive = 0

    for x in range(18):
        for y in range(18):
            if config.mapArray[x][y].owner == player:
                if x <= 6 and y <= 6:   #swamp
                    if config.mapArray[0][0].owner == player:
                        moneytogive += 50
                    else:
                        moneytogive += 100
                elif x<=6 and y>=11:    #desert
                    if config.mapArray[0][17].owner == player:
                        moneytogive += 50
                    else:
                        moneytogive += 100
                elif x>=11 and y<=6:    #ice
                    if config.mapArray[17][0].owner == player:
                        moneytogive += 50
                    else:
                        moneytogive += 100
                elif x>=11 and y>=11:   #forrest
                    if config.mapArray[17][17].owner == player:
                        moneytogive += 50
                    else:
                        moneytogive += 100
                elif x >=7 and x <= 10 and y>= 7 and y<=10: #gold
                    moneytogive += 150
    config.Playerlist[config.PlayerIndex].money += moneytogive