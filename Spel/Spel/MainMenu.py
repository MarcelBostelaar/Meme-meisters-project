import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
#colors are in a range of 0-255 (256 different entries)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_yellow = (239,254,54)
bright_blue = (64,132,244)
red = (200,0,0)
green = (0,200,0)
yellow = (236,220,26)
blue = (11,83,202)
#pygame.mixer.music.load("Title.mp3")

def game_loop():
    print("gameloop")

def quitgame():
    pygame.quit()
    quit()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Frequency")
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Frequency", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("New Game",200,450,100,50,green,bright_green,game_loop)
        button("Quit",500,450,100,50,red,bright_red,quitgame)
        button("Load Game",350,450,100,50,yellow,bright_yellow,quitgame)
        button("Settings",350,520,100,50,blue,bright_blue,quitgame)
        
        #pygame.draw.rect(gameDisplay, red, (500,450,100,50))
        #if 500+100 > mouse[0] > 500 and 450+50 > mouse[1] > 450:
            #pygame.draw.rect(gameDisplay, bright_red, (500,450,100,50))
        #else:
            #pygame.draw.rect(gameDisplay, red, (500,450,100,50))

        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.quit()
quit()