from typing import Counter
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('../sprite/pnj.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.position = [x,y]
        self.animations = [[self.get_image(0,0),self.get_image(32,0),self.get_image(64,0),self.get_image(96,0)],
        [self.get_image(0,32),self.get_image(32,32),self.get_image(64,32),self.get_image(96,32)],
        [self.get_image(0,64),self.get_image(32,64),self.get_image(64,64),self.get_image(96,64)],
        [self.get_image(0,96),self.get_image(32,96),self.get_image(64,96),self.get_image(96,96)]]
        self.directions = {
            "up" : 3,
            "left" : 1,
            "right" : 2,
            "down" : 0
        }
        self.count = 0


        self.feet = pygame.Rect(0,0, self.rect.width*0.5, 16) #take only the half of the body of the player

        self.past_position = self.position.copy() #Old position of the player

    def save_location(self):
        self.past_position = self.position.copy()

        
    #change animation
    def animation(self,direction,count):
        self.image = self.animations[direction][count]
        self.image.set_colorkey((0,0,0))

        
        


    #change position
    def orizental_right_up(self):
        self.position[0] += 2
        self.position[1] -= 2
    def orizental_left_up(self):
        self.position[0] -= 2
        self.position[1] -= 2
    def orizental_right_down(self):
        self.position[0] += 2
        self.position[1] += 2
    def orizental_left_down(self):
        self.position[0] -= 2
        self.position[1] += 2

    def right(self):
        self.position[0] += 2
    def left(self):
        self.position[0] -= 2
    def down(self):
        self.position[1] += 2
    def up(self):
        self.position[1] -= 2
    

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.past_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    
    def get_image(self,x,y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0,0), (x,y,32,32))
        return image