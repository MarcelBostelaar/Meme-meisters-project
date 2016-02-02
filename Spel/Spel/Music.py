import pygame
import config
pygame.init()
#window = pygame.display.set_mode((640,600))

mouseclicksound = pygame.mixer.Sound("MouseClick.wav")
mouseclicksound.set_volume(0.2)

def MenuMusic():
    if config.music:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("MenuMusic.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.2)

def GameMusic():
    if config.music:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("GameMusic.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.2)

def MouseClick():
    pygame.mixer.Sound.play(mouseclicksound)

#circle = pygame.draw.circle(window, (50,30,90), (90,30),16,5)

#window.blit(window, circle)

#while True:
#    for event in pygame.event.get():
#        if event.type==pygame.QUIT:
#            pygame.quit()
#            sys.exit()
#MenuMusic()
#pygame.display.update()