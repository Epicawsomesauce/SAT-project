import pygame, sys  # pygame is the foundation the game runs on and sys is what reads user inputs apparently
from pygame.locals import *
from PIL import Image 
from pygame import mixer
import random
import csv

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
duckPoints = 1

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



def play(rand, points, round):
    while True:
          
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((0,225,225))
        img = f'{rand}.png'

        PLAY_TEXT = get_font(45).render("WHERE IS THIS?.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(540, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_GUESS = Button(image=None, pos=(1000, 500), 
            text_input="GUESS", font=get_font(30), base_color="#ff9ae2", hovering_color="#ff86dd")
        
        PICTURE= Button(image=pygame.image.load(img), pos=(540, 360), 
                            text_input="", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
        


        PLAY_GUESS.changeColor(PLAY_MOUSE_POS)
        PLAY_GUESS.update(SCREEN)

        for button in [PICTURE, PLAY_GUESS]:
            button.changeColor(PLAY_MOUSE_POS)
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
                if PLAY_GUESS.checkForInput(PLAY_MOUSE_POS):
                    guess(rand,points,round)
        pygame.display.update()
 

def evil(duckPoints):
    morePoints = duckPoints + 1
    return morePoints


def quit():
      pygame.quit()
      sys.exit()


def duck():
    mixer.music.load("duck.mp3")
    mixer.music.play(1)
  

def evilDuck():
    mixer.music.load("evilQuack.mp3")
    mixer.music.play(-1)

def guess(rand, points, round):
    value = 0

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill((0,225,225))
        GUESS = Button(image=pygame.image.load("background.png"), pos=(540, 310), 
                text_input="", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
        CONFIRM = Button(image=pygame.image.load("gift2.png"), pos=(100, 560), 
                text_input="CONFRIM", font=get_font(30), base_color="#000000", hovering_color="#900067")
        GUESS.changeColor(PLAY_MOUSE_POS)
        GUESS.update(SCREEN)

        if value == 0:
            for button in [GUESS, CONFIRM]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(SCREEN)
        elif value == 1:
             for button in [GUESS, PICTURE, CONFIRM]:
                        button.changeColor(PLAY_MOUSE_POS)
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
                if GUESS.checkForInput(PLAY_MOUSE_POS):
                    x,y = pygame.mouse.get_pos()
                    #print(x,y)
                    PICTURE= Button(image=pygame.image.load("hollow.png"), pos=(x, y), 
                text_input="", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
                    value = 1

                if CONFIRM.checkForInput(PLAY_MOUSE_POS):
                    if value == 0:
                         print('oops')
                         break
                    elif value != 0:
                        with open('data.csv', newline='') as csvfile:
                                reader = csv.reader(csvfile)
                                for row in reader:
                                    for element in row:
                                        if int(element) == rand:
                                            x2 = int(row[1])
                                            y2 = int(row[2])
                                            points = int((200-(((((y2-y)**2) + ((x2-x)**2))**1/2)/1000))+ points)
                                            if points < 0:
                                                 points = 0
                                            print (points)
                        rand = random.randint(0,3)
                        round = round + 1
                        if round >= 3:
                            end(points)
                        play(rand, points, round)
                                  

        
        pygame.display.update()
        

def main(duckPoints):
    points = 0

    while True:
		
        SCREEN.fill((0,225,225))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BUTTON = Button(image=pygame.image.load("basebsll.png"), pos=(540, 250), 
                            text_input="AWESOME SAUCE", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
        QUIT_BUTTON= Button(image=pygame.image.load("Peashooter.png"), pos=(760, 400), 
                            text_input="LEAVE", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
        if duckPoints <= 10:
            DUCK_BUTTON= Button(image=pygame.image.load("duck.png"), pos=(330, 400), 
                            text_input="DUCK", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
        elif duckPoints >= 10:
             DUCK_BUTTON= Button(image=pygame.image.load("evilDuck.png"), pos=(330, 400), 
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
                    round = 0
                    rand = random.randint(0,3)
                    play(rand, points, round)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                      quit()
                if DUCK_BUTTON.checkForInput(MENU_MOUSE_POS):
                      if duckPoints <= 10:
                        duck()
                      elif duckPoints >= 10:
                           evilDuck()
                      duckPoints = evil(duckPoints)
            pygame.display.update() 


def end(points):
     while True:
          SCREEN.fill((0,225,225))
          END_MOUSE_POS = pygame.mouse.get_pos()

          SCORE = Button(image=None, pos=(540, 260), 
                text_input=f"your  score  is  {points}", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff9ae2")
          
          QUIT_BUTTON = Button(image=pygame.image.load("Peashooter.png"), pos=(760, 500), 
                            text_input="LEAVE", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
          
          AGAIN_BUTTON = Button(image=pygame.image.load("heavy.png"), pos=(330, 300), 
                            text_input="AGAIN", font=get_font(75), base_color="#ff9ae2", hovering_color="#ff86dd")
          
          for button in [SCORE, QUIT_BUTTON, AGAIN_BUTTON]:
               button.changeColor(END_MOUSE_POS)
               button.update(SCREEN)
          
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
               if event.type == pygame.MOUSEBUTTONDOWN:
                    if QUIT_BUTTON.checkForInput(END_MOUSE_POS):
                         quit()
                    if AGAIN_BUTTON.checkForInput(END_MOUSE_POS):
                         duckpoints = 0
                         main(duckpoints)
          pygame.display.update()

            

main(duckPoints)
