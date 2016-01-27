import config


def OrderMatrix(increment):
    config.TurnTick += increment
    if config.TurnTick == 4:
        config.PlayerIndex += 1
        config.TurnTick = 0
        print (str(config.PlayerIndex) + "'s turn has ended")
        if config.PlayerIndex == 4:
            config.PlayerIndex = 0

def EndTurn():
    config.TurnTick = 0
    config.PlayerIndex +=1
    print (str(config.PlayerIndex) + "'s turn has ended")
    if config.PlayerIndex == 4:
        config.PlayerIndex = 0
