import pygame as pg
from tiles import AnimatedTile
from  random import randint
class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, "first_level_materials/slime")
        self.rect.y += 8
        self.speed = randint(1, 3)

    def reverse_image(self):
        if self.speed > 0:
            self.image = pg.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def move(self):
        self.rect.x += self.speed

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()