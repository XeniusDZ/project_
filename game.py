import pygame
from pygame.constants import QUIT
import pyscroll
import pytmx
from player import Player



class Start:
    def __init__(self):
        #create game window
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption("Terros")
        #install the map
        tmx = pytmx.util_pygame.load_pygame('map.tmx')
        map = pyscroll.data.TiledMapData(tmx)
        map_layer = pyscroll.orthographic.BufferedRenderer(map, self.screen.get_size())
        map_layer.zoom = 2

        #create player
        position = tmx.get_object_by_name("spawn")
        self.player = Player(position.x,position.y)

        #draw layers
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
    def run(self):
                #Loop for running
        running = True

        while running:
            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
