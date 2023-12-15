import pygame
import constants as const

class Game():
    '''
    The Game class handles the main loop in the present file.
    '''
    def __init__(self) -> None:
        '''
        Main Game constructor
        '''
        pygame.init()
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def play(self) -> None:
        '''
        Game loop
        '''
        while self.running:
            self.handle__events()

            self.screen.fill("purple")

            # flip() the display to put your work on screen
            pygame.display.flip()

            
            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()
        
    def handle__events(self) -> None:
        '''
        Events handling section
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

if __name__ == "__main__":
     game = Game()
     game.play()
