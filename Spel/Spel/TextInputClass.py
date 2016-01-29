import pygame
import config

class TextBox:
    def __init__(self, width, height, fontsize = 20, font_color = (255,255,255), bgcolor = (0,0,0), font = None, maxlenght = 20):
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(font, fontsize)
        self.font_color = font_color
        self.bgcolor = bgcolor

        self.isactive = False
        self.text = ""
        self.lastrender = None
        self.maxlenght = maxlenght

    def handle_char(self, event):
        if event.key == pygame.K_RETURN:        #In case of enter, stop typing
            self.isactive = False
        elif event.key == ord("\b"):            #backspace removes letter
            self.text = self.text[:-1]
        elif event.key >= 32 and event.key <=126:
            if event.key >=97 and event.key <=122 and (pygame.key.get_pressed()[pygame.K_RSHIFT] or pygame.key.get_pressed()[pygame.K_LSHIFT])== 1: #In case you type a letter with shift pressed, make capital letter
                event.key -= 32
            if len(self.text) <= self.maxlenght:
                self.text = self.text + chr(event.key)

    def handlemousepress(self):
        mousepos = pygame.mouse.get_pos()
        if mousepos[1] <= self.lastrender[1]+self.height and mousepos[0] <= self.lastrender[0]+self.width and mousepos[0] >= self.lastrender[0] and mousepos[1] >= self.lastrender[1]:
            self.isactive = True
        else:
            self.isactive = False

    def draw(self, pos):

        self.lastrender = pos

        if self.isactive:
            textrender = self.font.render(self.text + "|", 1, self.font_color)
        else:
            textrender = self.font.render(self.text, 1, self.font_color)
        sizeText = textrender.get_rect().size


        pygame.draw.rect(config.setDisplay, self.bgcolor, (pos[0], pos[1], self.width, self.height))
        config.setDisplay.blit(textrender, (pos[0], pos[1]+sizeText[1]/2))
