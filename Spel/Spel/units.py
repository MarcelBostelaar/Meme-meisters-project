#temporary class values - might be changed depending on implementation method.

class Unit:
    def __init__(self):
        self.IsAlive = True

    def Soldier(self):
        self.name = "Soldier" 
        self.MoveDistance = 1
        self.AttackRange = 0
        self.Power = 1
        self.Price = 150
        self.CanMove = True
        self.CanAttack = True
        self.CanBuild = True
        self.CanSpawn = False

    def Robot(self):
        self.Name = "Robot"
        self.MoveDistance = 1
        self.AttackRange = 0
        self.Power = 2
        self.Price = 300
        self.CanMove = True
        self.CanAttack = True
        self.CanBuild = True
        self.CanSpawn = False

    def Tank(self):
        self.Name = "Tank"
        self.MoveDistance = 1
        self.AttackRange = 2
        self.Power = 3
        self.Price = 750
        self.CanMove = True
        self.CanAttack = True
        self.CanBuild = True
        self.CanSpawn = False

    def Barracks(self, biome):
        self.Name = "Barracks"
        self.MoveDistance = 0
        self.AttackRange = 0
        self.Power = 5
        self.Price = 500
        self.CanMove = False
        self.CanAttack = False
        self.Biome = biome
        self.CanBuild = False
        self.CanSpawn = True

    def Boat(self):
        self.name = "Boat"
        self.MoveDistance = 2
        self.AttackRange = 0
        self.Power = 6
        self.Price = 1000
        self.CanMove = True
        self.CanAttack = False
        self.CanBuild = False
        self.CanSpawn = False

    def Base(self, biome):
        self.name = "Base"
        self.MoveDistance = 0
        self.AttackRange = 0
        self.Power = 25
        self.Price = 0
        self.CanMove = False
        self.CanAttack = False
        self.CanBuild = False
        self.CanSpawn = True
        self.Biome = biome
unit = Unit()

'''
class Soldier:
    def __init__(self):
        self.MoveDistance = 1
        self.AttackRange = 1
        self.Power = 1
        self.Price = 150
        self.CanMove = True
        self.CanAttack = True

class Robot:
    def __init__(self):
        self.MoveDistance = 1
        self.AttackRange = 1
        self.Power = 2
        self.Price = 300
        self.CanMove = True
        self.CanAttack = True

class Tank:
    def __init__(self):
        self.MoveDistance = 1
        self.AttackRange = 2
        self.Power = 3
        self.Price = 750
        self.CanMove = True
        self.CanAttack = True

class Barracks:
    def __init__(self, biome):
        self.MoveDistance = 0
        self.AttackRange = 0
        self.Power = 5
        self.Price = 500
        self.CanMove = False
        self.CanAttack = False

class Boat:
    def __init__(self):
        self.MoveDistance = 2
        self.AttackRange = 0
        self.Power = 6
        self.Price = 1000
        self.CanMove = True
        self.CanAttack = False

class Base:
    def __init__(self, biome):
        self.MoveDistance = 0
        self.AttackRange = 0
        self.Power = 25
        self.Price = 0
        self.CanMove = False
        self.CanAttack = False
'''