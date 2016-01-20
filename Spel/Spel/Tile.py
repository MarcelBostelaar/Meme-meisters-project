class Tile:
    def __init__(self, biome):
        self.biome = biome
        self.owner = None
        self.troops = []
        self.building = None