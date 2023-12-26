import pygame as pg

#класс блока
class Tile(pg.sprite.Sprite):
    def __init__(self, pos, size):
        ground = pg.image.load("first_level_materials/Ground_02.png")
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
