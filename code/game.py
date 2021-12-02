import pygame
from pygame.constants import K_DOWN, K_LEFT, QUIT, K_d, K_q, K_s
import pyscroll
import pytmx
from map import MapManager
from player import Player

class Start:
    def __init__(self):

        self.running = True
        self.map = "map"


        #create game window
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption("Terros")


        #create player
        self.player = Player(0,0)
        self.map_manager = MapManager(self.screen,self.player)

        #collisions
        self.walls = []
        


    def clavish(self):
        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_z] or pressed[pygame.K_UP]) and (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]):
            self.player.orizental_right_up()
            self.player.animation(self.player.directions["up"],self.player.count)
            self.player.count += 1
            if self.player.count > 2:
                self.player.count = 0
        elif (pressed[pygame.K_z] or pressed[pygame.K_UP]) and (pressed[pygame.K_q] or pressed[pygame.K_LEFT]):
            self.player.orizental_left_up()
            self.player.animation(self.player.directions["up"],self.player.count)
            self.player.count += 1
            if self.player.count > 2:
                self.player.count = 0
        elif (pressed[pygame.K_s] or pressed[pygame.K_DOWN]) and (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]):
            self.player.orizental_right_down()
            self.player.animation(self.player.directions["down"],self.player.count)
            self.player.count += 1
            if self.player.count > 2:
                self.player.count = 0
        elif (pressed[pygame.K_s] or pressed[pygame.K_DOWN]) and (pressed[pygame.K_q] or pressed[pygame.K_LEFT]):
            self.player.orizental_left_down()
            self.player.animation(self.player.directions["down"],self.player.count)
            self.player.count += 1
            if self.player.count > 2:
                self.player.count = 0
        elif pressed[pygame.K_z] or pressed[pygame.K_UP]:
            self.player.up()
            self.player.animation(self.player.directions["up"],self.player.count)
            self.player.count += 1
            if self.player.count > 2:
                self.player.count = 0
        elif pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            self.player.down()
            self.player.animation(self.player.directions["down"],self.player.count)
            self.player.count += 1
            if self.player.count > 2:
                self.player.count = 0
        elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.player.right()
            self.player.animation(self.player.directions["right"],self.player.count)
            self.player.count += 1
            if self.player.count > 2:
                self.player.count = 0
        elif pressed[pygame.K_q] or pressed[pygame.K_LEFT]:  
            self.player.left()
            self.player.animation(self.player.directions["left"],self.player.count)
            self.player.count += 1
            if self.player.count > 2:
                self.player.count = 0


    

    def update(self):
        self.map_manager.update()

    def run(self):
        #fps
        clock = pygame.time.Clock()
        while self.running:
            self.player.save_location()
            self.clavish()

            self.update()
            self.map_manager.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
            #modify to 60fps
            clock.tick(60)
