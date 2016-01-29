import pygame
pygame.init()
#window = pygame.display.set_mode((640,600))

def MenuMusic():
    pygame.mixer.music.load("MenuMusic.mp3")
    pygame.mixer.music.play(-1,0.0)

def GameMusic():
    pygame.mixer.music.load("GameMusic.mp3")
    pygame.mixer.music.play(-1,0.0)

#circle = pygame.draw.circle(window, (50,30,90), (90,30),16,5)

#window.blit(window, circle)

#while True:
#    for event in pygame.event.get():
#        if event.type==pygame.QUIT:
#            pygame.quit()
#            sys.exit()
#MenuMusic()
#pygame.display.update()