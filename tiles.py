import pygame as pg
import os
def import_folder(path):
    surface_list = []
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pg.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list

class Tile(pg.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        self.rect.x += shift

class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

class Spikes(StaticTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pg.image.load("first_level_materials/Spikes.png").convert_alpha())
        offset_y = y + size + 5
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))

class AnimatedTile(Tile):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.frames_index = 0
        self.image = self.frames[self.frames_index]

    def animate(self):
        self.frames_index += 0.15
        if self.frames_index >= len((self.frames)):
            self.frames_index = 0
        self.image = self.frames[int(self.frames_index)]

    def update(self, shift):
        self.animate()
        self.rect.x += shift

class Decor(StaticTile):
    def __init__(self, size, x, y, surface, offset):
        super().__init__(size, x, y, surface)
        offset_y = y - offset
        self.rect.topleft = (x, offset_y)