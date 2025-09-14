import pygame, sys  # pygame is the foundation the game runs on and sys is what reads user inputs apparently
from pygame.locals import *
from PIL import Image 
from pygame import mixer

#Configurations and such

pygame.init() # Must be used to allow pygame to be used
icon = pygame.image.load("truckin.gif") #Sets the little image on the program
pygame.display.set_icon(icon)
pygame.display.set_caption("It's a work in progress")#Sets the text on the program window
fps = 60
fpsClock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((1080, 620)) #Sets window size
mixer.init()
mixer.music.set_volume(0.7)

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

def play():
    while True:
          
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
    
        SCREEN.fill((0,225,225))
    
        PLAY_TEXT = get_font(45).render("GAME GOES HERE.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                 if event.key == K_ESCAPE:
                      pygame.quit()
                      sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main()
        pygame.display.update()
 
        





def quit():
      pygame.quit()
      sys.exit()


def duck():
      mixer.music.play()
      pygame.time.wait(500)
      mixer.music.stop()
      
      

def main():

    while True:
		
        SCREEN.fill((0,225,225))
        mixer.music.load("duck.mp3")

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BUTTON = Button(image=pygame.image.load("basebsll.png"), pos=(540, 250), 
                            text_input="AWESOME SAUCE", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
        QUIT_BUTTON= Button(image=pygame.image.load("Peashooter.png"), pos=(760, 400), 
                            text_input="LEAVE", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
        DUCK_BUTTON= Button(image=pygame.image.load("duck.png"), pos=(330, 400), 
                            text_input="DUCK", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")

        for button in [PLAY_BUTTON, QUIT_BUTTON, DUCK_BUTTON]:
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                      quit()
                if DUCK_BUTTON.checkForInput(MENU_MOUSE_POS):
                      duck()
					
            pygame.display.update() 


main()
