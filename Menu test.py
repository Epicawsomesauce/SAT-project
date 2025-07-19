import pygame, sys  # pygame is the foundation the game runs on and sys is what reads user inputs apparently

def main():
    pygame.init() # Must be used to allow pygame to be used
    SCREEN = pygame.display.set_mode((640, 480))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        SCREEN.fill((0,225,225))
        pygame.display.flip()

main()
