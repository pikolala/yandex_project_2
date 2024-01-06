import pygame as pg

class Background(pg.sprite.Sprite):
    def __init__(self, x, y, path):
        super().__init__()
        self.image = pg.image.load(path)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        self.rect.x += shift


