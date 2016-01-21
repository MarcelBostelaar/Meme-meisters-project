import pygame
pygame.init()

class Button():
    def __init__(self, text, font_color, font = None, font_size = 10, bgcolor = None, texture = None, height = None, width = None):
        self.text = text
        self.font_color = font_color

        self.height = height    #height and width of box of button to draw
        self.width = width
        
        self.bgcolor = bgcolor  #color of button background (if no texture)
        self.font = pygame.font.SysFont(font, font_size)
        self.texture = texture  #texture for background button
        
        self.texture_dim = None
        self.lastrender = None

    def draw(self, posx, posy, screen):
        if self.height != None and self.width != None:          #If there is a height and witdh set (no texture case)
            pygame.draw.rect(screen, self.bgcolor, (posx,posy,self.width,self.height))
            textsize = self.font.size(self.text)
            text_width_offset = (self.width - textsize[0])/2
            text_height_offset = (self.height - textsize[1])/2
            textrender = self.font.render(self.text, 1, self.font_color)
            screen.blit(textrender, (posx + text_width_offset, posy + text_height_offset))


        elif self.texture != None:                              #if there is a texture set
            texture = pygame.image.load(self.texture).convert()
            screen.blit(texture, (posx, posy))
            sizeTexture = texture.get_rect().size
            self.texture_dim = sizeTexture
            textsize = self.font.size(self.text)
            text_width_offset = (sizeTexture[0] - textsize[0])/2
            text_height_offset = (sizeTexture[1] - textsize[1])/2
            textrender = self.font.render(self.text, 1, self.font_color)
            screen.blit(textrender, (posx + text_width_offset, posy + text_height_offset))

        self.lastrender = (posx, posy)      #Saves the position of the last time it was rendered

    def pressed(self):
        mousepos = pygame.mouse.get_pos()
        if mousepos[0] >= self.lastrender[0] and mousepos[1] >= self.lastrender[1]:
            if self.texture_dim != None:
                if mousepos[0] <= self.lastrender[0] + self.texture_dim[0] and mousepos[1] <= self.lastrender[1] + self.texture_dim[1]:
                    return True

            else:
                if mousepos[0] <= self.lastrender[0] + self.width and mousepos[1] <= self.lastrender[1] + self.height:
                    return True
        return False