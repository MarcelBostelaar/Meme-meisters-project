import pygame
import config
import Graphics_game
import Turn_Order
import ButtonClass
import Music
import Units

white = (255,255,255)
fontsize = 30

Line_Tile = ButtonClass.Button("", white, font_size = fontsize)
Line_Tile_Biome = ButtonClass.Button("", white, font_size = fontsize)
Line_Tile_Owner = ButtonClass.Button("", white, font_size = fontsize)

def Mousedown():
    stateMouse = pygame.mouse.get_pressed()
    if stateMouse[0] == 1:
        Tile_selected = config.mapArray[config.selectedtile[0]][config.selectedtile[1]]
        if Graphics_game.end_turn_button.pressed():
            Turn_Order.EndTurn()
        if Graphics_game.menu_button.pressed():
            config.window = "Esc_Menu"
            config.firsttime = True
        if Graphics_game.help_button.pressed():
            print("Help button pressed")
            config.window = "Help_Menu"
            config.firsttime = True
        if Graphics_game.Troop1.pressed():
            print("meme1")
            config.selectedtroop = 1
            config.unit = config.Selectedunits[0]
        if Graphics_game.Troop2.pressed():
            print("meme2")
            config.selectedtroop = 2
            config.unit = config.Selectedunits[1]
        if Graphics_game.Troop3.pressed():
            print("meme3")
            config.unit = config.Selectedunits[2]
            config.selectedtroop = 3
        if Graphics_game.MoveLeft.pressed() and config.Selectedunits != [] and config.selectedtile[0]-1 >=0 and config.mapArray[config.selectedtile[0]][config.selectedtile[1]].owner == config.Playerlist[config.PlayerIndex].name:
            if move_unit(config.unit, config.selectedtile, (config.selectedtile[0]-1,config.selectedtile[1])):
                config.selectedtile = (config.selectedtile[0]-1,config.selectedtile[1])
                Turn_Order.OrderMatrix(1)
        if Graphics_game.MoveUp.pressed() and config.Selectedunits != [] and config.selectedtile[1]-1 >=0 and config.mapArray[config.selectedtile[0]][config.selectedtile[1]].owner == config.Playerlist[config.PlayerIndex].name:
            if move_unit(config.unit, config.selectedtile, (config.selectedtile[0],config.selectedtile[1]-1)):
                config.selectedtile = (config.selectedtile[0],config.selectedtile[1]-1)
                Turn_Order.OrderMatrix(1)
        if Graphics_game.MoveRight.pressed() and config.Selectedunits != [] and config.selectedtile[0]+1 <=17 and config.mapArray[config.selectedtile[0]][config.selectedtile[1]].owner == config.Playerlist[config.PlayerIndex].name:
            if move_unit(config.unit, config.selectedtile, (config.selectedtile[0]+1,config.selectedtile[1])):
                config.selectedtile = (config.selectedtile[0]+1,config.selectedtile[1])
                Turn_Order.OrderMatrix(1)
        if Graphics_game.MoveDown.pressed() and config.Selectedunits != [] and config.selectedtile[1]+1 <= 17 and config.mapArray[config.selectedtile[0]][config.selectedtile[1]].owner == config.Playerlist[config.PlayerIndex].name:
            if move_unit(config.unit, config.selectedtile, (config.selectedtile[0],config.selectedtile[1]+1)):
                config.selectedtile = (config.selectedtile[0],config.selectedtile[1]+1)
                Turn_Order.OrderMatrix(1)
        if Graphics_game.BuyTank.pressed() and Tile_selected.building != []:
            if buy_unit("Tank", config.selectedtile):
                Turn_Order.OrderMatrix(1)
        if Graphics_game.BuyRobot.pressed() and Tile_selected.building != []:
            if buy_unit("Robot", config.selectedtile):
                Turn_Order.OrderMatrix(1)
        if Graphics_game.BuySoldier.pressed() and Tile_selected.building != []:
            if buy_unit("Soldier", config.selectedtile):
                Turn_Order.OrderMatrix(1)
        if Graphics_game.BuyBarracks.pressed() and Tile_selected.troops != []:
            if buy_unit("Barracks", config.selectedtile):
                Turn_Order.OrderMatrix(1)
        if Graphics_game.BuyBoat.pressed() and Tile_selected.troops != []:
            if buy_unit("Boat", config.selectedtile):
                Turn_Order.OrderMatrix(1)



        if Graphics_game.attack_button.pressed():
            config.isattacking = True

        config.Selectedunits = []
        config.memetick = 0
        SelectTile()

def SelectTile():
    config.Selectedunits = []
    mouseposition = pygame.mouse.get_pos()
    if mouseposition[0] >= config.Gameboard_offsetx and mouseposition[0] <= config.window_width+config.Gameboard_offsetx and mouseposition[1] >= config.Gameboard_offsety and mouseposition[1] <= config.Gameboard_offsety+config.window_height:
        i = (int((mouseposition[0]-config.Gameboard_offsetx)/50), int((mouseposition[1]-config.Gameboard_offsety)/50))
        if i[0] >= 0 and i[0]<=17 and i[1] >=0 and i[1]<= 17:
            if config.isattacking:
                combat(config.selectedtile, i)
                config.isattacking = False
                Turn_Order.OrderMatrix(1)
            else:
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
    if (config.mapArray[pos_target[0]][pos_target[1]].owner != config.mapArray[pos_current[0]][pos_current[1]].owner) and config.mapArray[pos_target[0]][pos_target[1]].owner != None:
        print("Units not on same side")
        return False
    if abs(pos_current[0]-pos_target[0])+abs(pos_current[1]-pos_target[1]) >1:
        print("Units too far apart to move there!")
        return False
    if config.mapArray[pos_target[0]][pos_target[1]].biome == "w" and unit != "Boat":
        if len(config.mapArray[pos_target[0]][pos_target[1]].troops) != 0:
            x = 0
            for i in config.mapArray[pos_current[0]][pos_current[1]].troops:
                if unit == i.Name:
                    config.mapArray[pos_target[0]][pos_target[1]].troops[0].troops.append(i)
                    config.mapArray[pos_current[0]][pos_current[1]].troops.pop(x)
                    config.mapArray[pos_target[0]][pos_target[1]].owner = config.mapArray[pos_current[0]][pos_current[1]].owner
                    return True
        return False
    if config.mapArray[pos_target[0]][pos_target[1]].biome == "w" and unit == "Boat":
        if config.mapArray[pos_target[0]][pos_target[1]].troops == []:
            config.mapArray[pos_target[0]][pos_target[1]].troops.append(config.mapArray[pos_current[0]][pos_current[1]].troops[0])
            config.mapArray[pos_current[0]][pos_current[1]].troops.pop(0)
            config.mapArray[pos_target[0]][pos_target[1]].owner = config.mapArray[pos_current[0]][pos_current[1]].owner
            return True
        return False
    if config.mapArray[pos_target[0]][pos_target[1]].biome != "w" and unit == "Boat":
        if config.mapArray[pos_current[0]][pos_current[1]].troops[0].Name == "Boat":
            if len(config.mapArray[pos_current[0]][pos_current[1]].troops[0].troops) == 0:
                return False
            y = 0
            x = 0
            for i in config.mapArray[pos_current[0]][pos_current[1]].troops[0].troops:
                if y == 0:
                    config.Selectedunits = []
                if len(config.mapArray[pos_target[0]][pos_target[1]].troops) <3:
                    config.mapArray[pos_target[0]][pos_target[1]].troops.append(i)
                    config.Selectedunits.append(i)
                    config.mapArray[pos_current[0]][pos_current[1]].troops[0].troops.pop(x)
                    config.mapArray[pos_target[0]][pos_target[1]].owner = config.mapArray[pos_current[0]][pos_current[1]].owner
                
                y+=1
                x+=1
            config.Selectedunits = []
            return True
    if config.mapArray[pos_target[0]][pos_target[1]].building != None:
        return False
    x=0
    for i in config.mapArray[pos_current[0]][pos_current[1]].troops:
        if unit == i.Name:
            config.mapArray[pos_target[0]][pos_target[1]].troops.append(i)
            config.mapArray[pos_current[0]][pos_current[1]].troops.pop(x)
            config.mapArray[pos_target[0]][pos_target[1]].owner = config.mapArray[pos_current[0]][pos_current[1]].owner
            return True
        x+=1
    return False

def buy_unit(unit, pos_buying):
    buying_tile = config.mapArray[pos_buying[0]][pos_buying[1]]
    player = config.Playerlist[config.PlayerIndex]
    newunit = Units.Unit()
    if unit != "Barracks" and unit != "Boat":
        if buying_tile.building != None and buying_tile.owner == player.name:
            if unit == "Soldier":
                newunit.Soldier()
                if buying_tile.biome == "i":
                    newunit.Price -= 30
            if unit == "Robot":
                newunit.Robot()
                if buying_tile.biome == "f":
                    newunit.Price -= 60
            if unit == "Tank":
                newunit.Tank()
                if buying_tile.biome == "d":
                    newunit.Price -= 150

            for x in range(-1, 2):
                for y in range(-1, 2):
                    if pos_buying[0]+x >=0 and pos_buying[0]+x <=17 and pos_buying[1]+y >=0 and pos_buying[1]+y <=17:
                        if config.mapArray[pos_buying[0]+x][pos_buying[1]+y].building == None and len(config.mapArray[pos_buying[0]+x][pos_buying[1]+y].troops) < 3 and config.mapArray[pos_buying[0]+x][pos_buying[1]+y].biome != "w" and (config.mapArray[pos_buying[0]+x][pos_buying[1]+y].owner == player.name or config.mapArray[pos_buying[0]+x][pos_buying[1]+y].owner == None):
                            if newunit.Price <= player.money:
                                config.Playerlist[config.PlayerIndex].money -= newunit.Price
                                config.mapArray[pos_buying[0]+x][pos_buying[1]+y].troops.append(newunit)
                                config.mapArray[pos_buying[0]+x][pos_buying[1]+y].owner = config.Playerlist[config.PlayerIndex].name
                                return True
        return False
    else:
        if buying_tile.owner == player.name:
            if unit == "Boat":
                newunit.Boat()
                if buying_tile.biome == "s":
                    newunit.Price -= 200

                for x in range(3):
                    for y in range(3):
                        if x == 2:
                            xdifference = -1
                        else:
                            xdifference = x
                        if y == 2:
                            ydifference = -1
                        else:
                            ydifference = y
                        if abs(xdifference) + abs(ydifference) == 1:
                            if pos_buying[0]+xdifference >=0 and pos_buying[0]+xdifference <=17 and pos_buying[1]+ydifference >=0 and pos_buying[1]+ydifference <=17:
                                if config.mapArray[pos_buying[0]+xdifference][pos_buying[1]+ydifference].owner == None and config.mapArray[pos_buying[0]+xdifference][pos_buying[1]+ydifference].biome == "w":
                                    if newunit.Price <= player.money:
                                        config.Playerlist[config.PlayerIndex].money -= newunit.Price
                                        config.mapArray[pos_buying[0]+xdifference][pos_buying[1]+ydifference].troops.append(newunit)
                                        config.mapArray[pos_buying[0]+xdifference][pos_buying[1]+ydifference].owner = config.Playerlist[config.PlayerIndex].name
                                        return True
                return False



            elif unit == "Barracks":
                newunit.Barracks()
                doesownbiome = False
                if config.mapArray[0][0].owner == player.name and config.mapArray[0][0].biome == buying_tile.biome:
                    doesownbiome = True
                if config.mapArray[17][0].owner == player.name and config.mapArray[17][0].biome == buying_tile.biome:
                    doesownbiome = True
                if config.mapArray[0][17].owner == player.name and config.mapArray[0][17].biome == buying_tile.biome:
                    doesownbiome = True
                if config.mapArray[17][17].owner == player.name and config.mapArray[17][17].biome == buying_tile.biome:
                    doesownbiome = True
                if not doesownbiome:
                    newunit.Price = 1500

                for x in range(3):
                    for y in range(3):
                        if x == 2:
                            xdifference = -1
                        else:
                            xdifference = x
                        if y == 2:
                            ydifference = -1
                        else:
                            ydifference = y
                        if abs(xdifference) + abs(ydifference) == 1:
                            if pos_buying[0]+xdifference >=0 and pos_buying[0]+xdifference <=17 and pos_buying[1]+ydifference >=0 and pos_buying[1]+ydifference <=17:
                                if config.mapArray[pos_buying[0]+xdifference][pos_buying[1]+ydifference].owner == None and config.mapArray[pos_buying[0]+xdifference][pos_buying[1]+ydifference].building == None and config.mapArray[pos_buying[0]+xdifference][pos_buying[1]+ydifference].biome != "w":
                                    if newunit.Price <= player.money:
                                        config.Playerlist[config.PlayerIndex].money -= newunit.Price
                                        config.mapArray[pos_buying[0]+xdifference][pos_buying[1]+ydifference].building = newunit
                                        config.mapArray[pos_buying[0]+xdifference][pos_buying[1]+ydifference].owner = config.Playerlist[config.PlayerIndex].name
                                        return True
                return False
    return False

def combat(AttackingTile, DefendingTile):
    tile1 = config.mapArray[AttackingTile[0]][AttackingTile[1]]
    tile2 = config.mapArray[DefendingTile[0]][DefendingTile[1]]
    if abs(AttackingTile[0]-DefendingTile[0])+abs(AttackingTile[1]-DefendingTile[1]) >1:
        print("Troops not next to each other")
        return False
    if tile1.owner == tile2.owner:
        print("Troops are on the same side")
        return False
    if tile2.building == None:
        print("Fighting units")
        if len(tile1.troops) == 0 or len(tile2.troops) == 0:
            print("One of the two tiles doesnt have units")
            return False
        tile1_str = 0
        tile2_str = 0
        for i in tile1.troops:
            tile1_str += i.Power
        for i in tile2.troops:
            tile2_str += i.Power

        tile1_newstr = tile1_str - tile2_str
        tile2_newstr = tile2_str - tile1_str
        x = 0
        for i in tile1.troops:
            if tile1_newstr > 0:
                tile1_newstr -= i.Power
            else:
                config.mapArray[AttackingTile[0]][AttackingTile[1]].troops = config.mapArray[AttackingTile[0]][AttackingTile[1]].troops[:x]
            x +=1

        x = 0
        for i in tile2.troops:
            if tile2_newstr > 0:
                tile2_newstr -= i.Power
            else:
                config.mapArray[DefendingTile[0]][DefendingTile[1]].troops = config.mapArray[DefendingTile[0]][DefendingTile[1]].troops[:x]
            x +=1
    else:
        print("Fighting a building")
        tile1_str = 0
        for i in tile1.troops:
            tile1_str += i.Power
        config.mapArray[DefendingTile[0]][DefendingTile[1]].building.Power -= tile1_str
        if config.mapArray[DefendingTile[0]][DefendingTile[1]].building.Power <1:
            config.mapArray[DefendingTile[0]][DefendingTile[1]].building = None
    config.TurnTick += 1

def janitor():
    for x in range(18):
        for y in range(18):
            if len(config.mapArray[x][y].troops) == 0 and config.mapArray[x][y].building == None:
                config.mapArray[x][y].owner = None