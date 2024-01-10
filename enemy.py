import pygame as pg
from tiles import AnimatedTile
class Enemy(AnimatedTile):
    def __init__(self, size, x, y, path, speed):
        super().__init__(size, x, y, path)
        self.speed = speed

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

class Slime(Enemy):
    def __init__(self, size, x, y, path, speed):
        super().__init__(size, x, y, path, speed)
        self.rect.y += 8

class MoveableTerrain(Enemy):
    def __init__(self, size, x, y, path, speed):
        super().__init__(size, x, y, path, speed)
        self.rect.bottomleft = self.rect.topleft
        self.rect.y += 36

class Bee(Enemy):
    def __init__(self, size, x, y, path, speed):
        super().__init__(size, x, y, path, speed)
        self.rect.y -= 36
        self.rect.x -= 1
