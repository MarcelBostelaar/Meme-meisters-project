import pygame
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

frame = pygame.image.load("textures/frame.png")

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("your turn")

clock = pygame.time.Clock()

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    gameDisplay.fill(white)
    gameDisplay.blit(frame, (50,50))
#    pygame.draw.rect(gameDisplay, red, (400,200,50,25))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()