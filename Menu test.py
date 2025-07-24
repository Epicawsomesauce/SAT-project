import pygame, sys  # pygame is the foundation the game runs on and sys is what reads user inputs apparently
from pygame.locals import *
def main():
    pygame.init() # Must be used to allow pygame to be used
    SCREEN = pygame.display.set_mode((640, 480))

    while True:

        SCREEN.fill((0,225,225))
        pygame.display.flip()
        icon = pygame.image.load("basebsll.jpg")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("It's a work in progress")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update
            if KeyboardInterrupt:
                    pygame.time.set_timer(pygame.QUIT, 3000)
   



    

main()
