import sys

import main
import pygame as pg
import csv
from tiles import *
from enemy import *
from decoration import *
from player import *
import threading

from functools import cache

tile_size = 36

def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = csv.reader(map, delimiter=",")
        for row in level:
            terrain_map.append(list(row))
        return terrain_map

@cache
def import_cut_graphics(path):
    surface = pg.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pg.Surface((tile_size, tile_size), flags=pg.SRCALPHA)
            new_surf.blit(surface, (0, 0), pg.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surf)

    return cut_tiles
class Level:
    def __init__(self, level_data, surface):
        #инициализация переменных
        self.level_music = pg.mixer.Sound("third_level_materials/3_music.mp3")
        main.music_channel.play(self.level_music, loops=-1)
        self.display_surface = surface
        self.world_shift = 0
        self.t = threading.Thread(target=self.shoot)
        self.t.daemon = True

        #инициализация игрока
        player_layout = import_csv_layout(level_data["player"])
        self.player = pg.sprite.GroupSingle()
        self.finish = pg.sprite.GroupSingle()
        self.player_setup(player_layout)

        #инициализация террейна
        terrain_layout = import_csv_layout(level_data["terrain"])
        self.terrain_sprites = self.create_tile_group(terrain_layout, "terrain")

        #инициализация декора
        decor_layout = import_csv_layout(level_data["decor"])
        self.decor_sprites = self.create_tile_group(decor_layout, "decor")

        #инициализация шипов
        spike_layout = import_csv_layout(level_data["spikes"])
        self.spike_sprites = self.create_tile_group(spike_layout, "spikes")

        #инициализация слайма
        slime_layout = import_csv_layout(level_data["slime"])
        self.slime_sprites = self.create_tile_group(slime_layout, "slime")

        #инициализация подвижных плиток
        moveable_terrain_layout = import_csv_layout(level_data["moveable terrain"])
        self.moveable_terrain_sprites = self.create_tile_group(moveable_terrain_layout, "moveable terrain")

        #инициализация пчелы
        bee_layout = import_csv_layout(level_data["bee"])
        self.bee_sprites = self.create_tile_group(bee_layout, "bee")

        #инициализация фонового декора
        background_decor_layout = import_csv_layout(level_data["background decor"])
        self.background_decor_sprites = self.create_tile_group(background_decor_layout, "background decor")

        #инициализация мага
        wizard_layout = import_csv_layout(level_data["wizard"])
        self.wizard_sprites = self.create_tile_group(wizard_layout, "wizard")

        self.bullet_sprites = pg.sprite.Group()

        #инициализация ограничений
        constraints_layout = import_csv_layout(level_data["constraints"])
        self.constraints_sprites = self.create_tile_group(constraints_layout, "constraints")

        self.background_sprite = pg.sprite.Group()
        for i in range(-1000, 5000, 1000):
            self.background_sprite.add(Background(i, 0, "third_level_materials/SET1_bakcground_night3.png"))

        self.t.start()

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == "0":
                    sprite = Player((x, y))
                    self.player.add(sprite)
                if val == "1":
                    finish_surface = pg.image.load("first_level_materials/Diamond.png").convert_alpha()
                    sprite = StaticTile(tile_size, x, y, finish_surface)
                    self.finish.add(sprite)

    def create_tile_group(self, layout, type):
        sprite_group = pg.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != "-1":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    sprite = ""
                    if type == "terrain":
                        terrain_tile_list = import_cut_graphics("third_level_materials/terrain.png")
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)


                    if type == "decor":
                        decor_tile_list = import_cut_graphics("third_level_materials/decor.png")
                        tile_surface = decor_tile_list[int(val)]
                        sprite = Decor(tile_size, x, y, tile_surface, 0)

                    if type == "background decor":
                        decor_tile_list = import_cut_graphics("third_level_materials/background_decor.png")
                        tile_surface = decor_tile_list[int(val)]
                        sprite = Decor(tile_size, x, y, tile_surface, 0)


                    if type == "spikes":
                        sprite = Spikes(tile_size, x, y)


                    if type == "slime":
                        sprite = Slime(tile_size, x, y, "first_level_materials/slime", 3)
                        sprite_group.add((sprite))

                    if type == "moveable terrain":
                        sprite = MoveableTerrain(tile_size * 3, x, y, "second_level_materials/moveable_ground", 2)
                        sprite_group.add((sprite))

                    if type == "bee":
                        sprite = Bee(tile_size + 1, x, y, "second_level_materials/bee", -5)
                        sprite_group.add((sprite))

                    if type == "wizard":
                        sprite = Wizard(tile_size, x, y, "third_level_materials/wizard")

                    if type == "constraints":
                        sprite = Tile(tile_size, x, y)

                    sprite_group.add((sprite))


        return sprite_group

    def shoot(self):
        while 1:
            pg.time.wait(2000)
            b = Bullet(self.wizard_sprites.sprites()[0].rect.x, self.wizard_sprites.sprites()[0].rect.y + 40, self.display_surface)
            self.bullet_sprites.add(b)
            for sprite in self.bullet_sprites.sprites():
                if sprite.rect.x < 0:
                    self.bullet_sprites.remove(sprite)


    def enemy_collision_reverse(self):
        for enemy in self.slime_sprites.sprites() + self.moveable_terrain_sprites.sprites() + self.bee_sprites.sprites():
            if pg.sprite.spritecollide(enemy, self.constraints_sprites, False):
                enemy.reverse()

    # настройка камеры
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        keys = pg.key.get_pressed()
        if player_x < 100 and direction_x < 0:
            if keys[pg.K_LSHIFT]:
                self.world_shift = 8
            else:
                self.world_shift = 4
            player.speed = 0

        elif player_x > 200 and direction_x > 0:
            if keys[pg.K_LSHIFT]:
                self.world_shift = -8
            else:
                self.world_shift = -4
            player.speed = 0
        else:
            if player.status == "run":
                player.speed = 8
            else:
                player.speed = 4
            self.world_shift = 0

    #горизонтальная коллизия
    def horizontal_movment_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain_sprites.sprites() + self.moveable_terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
    #вертикальная коллизия
    def vertical_movment_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.direction.y = 0
                    player.rect.top = sprite.rect.bottom
                    player.on_ceiling = True

        for sprite in self.moveable_terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    self.world_shift -= sprite.speed


        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def check_death(self):
        if self.player.sprite.rect.top > 600:
            main.user_interface.death()
            main.user_interface.update()
            main.lvl3()


    def check_win(self):
        if pg.sprite.spritecollide(self.player.sprite, self.finish, False):
            main.last_finish_menu()

    def check_enemy_collisions(self):
        player = self.player.sprite

        for sprite in self.slime_sprites.sprites() + self.spike_sprites.sprites() + self.bee_sprites.sprites() + self.bullet_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                main.user_interface.death()
                main.user_interface.update()
                main.lvl3()

    def pause(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            main.escape_menu()
    def run(self):
        self.background_sprite.update(self.world_shift)
        self.background_sprite.draw(self.display_surface)

        self.background_decor_sprites.draw(self.display_surface)
        self.background_decor_sprites.update(self.world_shift)

        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)

        self.spike_sprites.draw(self.display_surface)
        self.spike_sprites.update(self.world_shift)

        self.decor_sprites.draw(self.display_surface)
        self.decor_sprites.update(self.world_shift)


        self.slime_sprites.update(self.world_shift)
        self.constraints_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.slime_sprites.draw(self.display_surface)

        self.moveable_terrain_sprites.update(self.world_shift)
        self.moveable_terrain_sprites.draw(self.display_surface)

        self.bee_sprites.update(self.world_shift)
        self.bee_sprites.draw(self.display_surface)

        self.wizard_sprites.update(self.world_shift)
        self.wizard_sprites.draw(self.display_surface)
        self.bullet_sprites.update(self.world_shift)

        self.player.update()
        self.scroll_x()
        self.horizontal_movment_collision()
        self.vertical_movment_collision()
        self.player.draw(self.display_surface)
        self.finish.update(self.world_shift)
        self.finish.draw(self.display_surface)

        self.check_death()
        self.check_win()

        self.check_enemy_collisions()

        self.pause()