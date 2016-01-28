import pygame

waterImg = pygame.image.load("textures/water.png")
waterImg0 = pygame.image.load("textures/water0.png")
waterImg1 = pygame.image.load("textures/water1.png")
waterImg2 = pygame.image.load("textures/water2.png")
waterImg3 = pygame.image.load("textures/water3.png")
waterImg4 = pygame.image.load("textures/water4.png")
waterImg5 = pygame.image.load("textures/water5.png")
waterImg6 = pygame.image.load("textures/water6.png")
waterImg7 = pygame.image.load("textures/water7.png")
forestImg = pygame.image.load("textures/forest.png")
desertImg = pygame.image.load("textures/desert.png")
iceImg = pygame.image.load("textures/ice.png")
swampImg = pygame.image.load("textures/swamp.png")
goldImg = pygame.image.load("textures/gold.png")

Baseimg = pygame.image.load("textures/base_placeholder.png").convert()
Baseimg.set_colorkey((255,0,255))

Soldierimg = pygame.image.load("textures/soldier.png").convert()
Robotimg = pygame.image.load("textures/robot.png").convert()
Tankimg = pygame.image.load("textures/tank.png").convert()

Soldierimg.set_colorkey((255,0,255))
Robotimg.set_colorkey((255,0,255))
Tankimg.set_colorkey((255,0,255))

black_border_img = pygame.image.load("textures/black_border.png").convert()
black_border_img.set_colorkey((255,0,255))

white_border_img = pygame.image.load("textures/white_border.png").convert()
white_border_img.set_colorkey((255,0,255))

logo = pygame.image.load("textures/RealLogo.png").convert_alpha()
logo.set_colorkey((255,0,255))