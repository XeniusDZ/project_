import pygame
from game import Start
from music import main_music

if __name__ == '__main__':
    main_music()
    pygame.init()
    start = Start()
    start.run()
