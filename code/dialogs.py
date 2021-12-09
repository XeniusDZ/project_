import pygame


class Dialog:

    dialog_x = 175
    dialog_y = 850

    def __init__(self):
        self.dialog = pygame.image.load('../dialogs/dialog_box.png')
        self.dialog = pygame.transform.scale(self.dialog, (1600,200))
        self.texts = []
        self.increment = 0
        self.index = 0
        self.font = pygame.font.Font("../dialogs/dialog_font.ttf", 30)
        self.show_dialog = False


    def execute(self, dialog):
        if self.show_dialog:
            self.next_text()
        else:
            self.show_dialog = True
            self.index = 0
            self.texts = dialog

    def show(self,screen):
        if self.show_dialog:
            self.increment += 1
            if self.increment >= len(self.texts[self.index]):
                self.increment = len(self.texts[self.index])
            screen.blit(self.dialog, (self.dialog_x, self.dialog_y))
            text = self.font.render(self.texts[self.index][0:self.increment], False, (0, 0, 0))
            screen.blit(text, (self.dialog_x + 150, self.dialog_y + 80))

    def next_text(self):
        self.increment = 0
        self.index += 1
        if self.index >= len(self.texts):
            self.show_dialog = False
