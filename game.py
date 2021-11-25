import pygame
from pygame.constants import K_DOWN, K_LEFT, QUIT, K_d, K_q, K_s
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

        #collisions
        self.walls = []

        for object in tmx.objects:
            if object.type == "collision":
                self.walls.append(pygame.Rect(object.x, object.y, object.width, object.height))
            

        #draw layers
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
        self.group.add(self.player)
        


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

   
    def run(self):
        #fps
        clock = pygame.time.Clock()

        #Loop for running
        running = True


        while running:
            
            self.clavish()

            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            #modify to 60fps
            clock.tick(60)
