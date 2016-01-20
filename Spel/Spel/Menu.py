import pygame

pygame.init() #initialize pygame

class EscMenu():
    def __init__(self, screen, items, bgcolor=(50,50,50), font=None, font_size=30, font_color=(255,255,255)):

        self.screen = screen
        self.scr_width = self.screen.get_rect().width #fetches screen rectangle dimensions, stores width as EscMenu.scr_width
        self.scr_height = self.screen.get_rect().height

        self.bgcolor = bgcolor

        self.items = items
        self.font = pygame.font.SysFont(font, font_size) #use default font, font size 30 (assigned in def __init__)
        self.font_color = font_color

        self.items = [] #create empyt list .items
        for index, item in enumerate(items): #lists all entries in 'items' with the corresponding index
            label = self.font.render(item, 1, font_color) #stores render query per item  (text -> alias -> color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.scr_width / 2) - (width / 2)
            text_height = len(items) * height
            posy = (self.scr_height / 2) - (text_height / 2) + (index * height)

            self.items.append([item, label, (width, height), (posx, posy)])
        
    def run(self):
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

            self.screen.fill(self.bgcolor)

            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
            pygame.display.flip()

if __name__ == "__main__": #Execute if module is main module

    screen = pygame.display.set_mode((640,480), 0, 32)
    menu_items = ('Start', 'Quit')
    pygame.display.set_caption('Memes')
    em = EscMenu(screen, menu_items)

    em.run()