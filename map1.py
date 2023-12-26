import pygame as pg
from tiles import Tile
from player import Player

#карта уровня
level_map = [
"XXXXXXXXXXXXXXXXXXXX",
"                    ",
"       P            ",
"XXXXXXXXXXXXXXXXXXXX",
"                    ",
"                    ",
"                    ",
"                    ",
"                X   ",
"                X   ",
"                    ",
"                    ",
"                X   ",
"                XX  ",
"XXXXXXXXXXXXXXXXXXXX",]
#размер блока
tile_size = 40

#класс уровня
class Level:
    def __init__(self, level_data, surface):

        #настройка уровня
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    #инициализация уровня
    def setup_level(self, layout):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add((tile))
                if cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add((player_sprite))

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 100 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > 200 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    #горизонтальная коллизия
    def horizontal_movment_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    #вертикальная коллизия
    def vertical_movment_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.direction.y = 0
                    player.rect.top = sprite.rect.bottom


    #отрисовка уровня
    def run(self):
        #блоки уровня
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        #игрок
        self.player.update()
        self.horizontal_movment_collision()
        self.vertical_movment_collision()
        self.player.draw(self.display_surface)
