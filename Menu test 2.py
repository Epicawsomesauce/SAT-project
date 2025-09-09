import pygame, sys  # pygame is the foundation the game runs on and sys is what reads user inputs apparently
from pygame.locals import *
from PIL import Image 

#Configurations and such

pygame.init() # Must be used to allow pygame to be used
icon = pygame.image.load("truckin.gif") #Sets the little image on the program
pygame.display.set_icon(icon)
pygame.display.set_caption("It's a work in progress")#Sets the text on the program window
fps = 60
fpsClock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((1280, 720)) #Sets window size
objects = []
gamestate = 0

def get_font(size):
    return pygame.font.Font("Mario-Kart-DS.ttf", size) #Sets font

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


def main():

    while True:
		
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BUTTON = Button(image=pygame.image.load("basebsll.jpg"), pos=(640, 250), 
                            text_input="AWESOME SAUCE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
             if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            pygame.display.update()  


main()
