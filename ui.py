import main
import pygame as pg

class UI:
    def __init__(self, surface):
        #настрока
        self.display_surface = surface
        self.current_health = 5

        #здоровье
        self.health = pg.sprite.Group()
        self.update()
    def update(self):
        self.health.empty()
        for i in range(self.current_health):
            self.health_sprite = pg.sprite.Sprite()
            self.health_sprite.image = pg.image.load("first_level_materials/Life.png")
            self.health_sprite.rect = self.health_sprite.image.get_rect()
            self.health_sprite.rect.left = 36 * i
            self.health.add(self.health_sprite)
    def show_health(self):
        self.health.draw(self.display_surface)

    def death(self):
        self.current_health -= 1
        if self.current_health == 0:
            main.death_menu()