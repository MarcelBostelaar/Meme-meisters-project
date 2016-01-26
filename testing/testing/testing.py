import os, sys
import pygame

pygame.init()

gamename = "Frequency"
window_height = 900
window_width = 1300

fps = 30
fpsTime = pygame.time.Clock()

setDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(gamename)

x = 1
direction = "blue"
thing = [direction, x]

def animate(timeinsec, direction, x):
    if direction == "blue":
        x +=1
    if x == 6:
        direction = "red"
    else:
        x -= 1
        if x == 1:
            direction = "blue"
    Image = pygame.image.load(str(x) + ".png")

    setDisplay.blit(Image, (0,0))
    return [direction, x]

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    thing = animate(1, thing[0], thing[1])

    pygame.display.update()
    fpsTime.tick(fps)