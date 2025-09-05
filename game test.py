import pygame, sys  # pygame is the foundation the game runs on and sys is what reads user inputs apparently
from pygame.locals import *
import time


#Configurations and such

pygame.init() # Must be used to allow pygame to be used
icon = pygame.image.load("truckin.gif") #Sets the little image on the program
pygame.display.set_icon(icon)
pygame.display.set_caption("It's a work in progress")#Sets the text on the program window
fps = 60
fpsClock = pygame.time.Clock()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Sets window size
SCREEN.fill((0,225,225)) 
font = pygame.font.Font('Mario-Kart-DS.ttf', 40) #Sets font
objects = []
gamestate = 1

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        SCREEN.blit(self.buttonSurface, self.buttonRect)
def guess():
    gamestate = 2
    print (gamestate)


def main():

    while True:

        pygame.display.flip()
    
        for object in objects:
           object.process()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
             if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            pygame.display.update()  
        
        if gamestate == 1:
            Button(SCREEN_WIDTH/8, SCREEN_HEIGHT/8, 20, 20, 'H', guess)
        if gamestate == 2:
            map()

           


main()
