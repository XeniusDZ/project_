import pygame

def main_music():
    pygame.mixer.init()
    music = pygame.mixer.music
    music.load("../music/battle.mp3")
    music.play(-1)
def sound(music_interraction):
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(music_interraction))

