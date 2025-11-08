import pygame
from constants import *
from player import Player
from logger import log_state

# class Player:
#     def __init__(self, x, y):
#         self.x = SCREEN_WIDTH / 2
#         self.y = SCREEN_HEIGHT / 2



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
   
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill(black)
        player.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000
        
        



if __name__ == "__main__":
    main()
