import pygame as pg
import os
import main

main.pg.mixer.init()
jump_sound = pg.mixer.Sound("Hero/sound/30_Jump_03.wav")
#jump_sound.set_volume(main.SOUND_VOLUME)

#импорт анимаций
def import_folder(path):
    surface_list = []
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surface = pg.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list
class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        #движение игрока
        self.direction = pg.math.Vector2(0,0)
        self.speed = 4
        self.gravity = 0.8
        self.jump_speed = -16

        #статус игрока
        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    #импорт анимаций
    def import_character_assets(self):
        character_path = "Hero/"
        self.animations = {"idle":[], "walk":[], "jump":[], "fall":[], "run":[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    #анимация
    def animate(self):
        animation = self.animations[self.status]

        #цикл кадров
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = pg.transform.scale2x(image)
        else:
            flipped_image = pg.transform.flip(image, True, False)
            self.image = pg.transform.scale2x(flipped_image)

        #правильная установка rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    #управлление движения
    def get_input(self):
        self.import_character_assets()
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pg.K_a]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        if keys[pg.K_SPACE] and self.on_ground:
            self.jump()
            jump_sound.play()

    #получение статуса
    def get_status(self):
        keys = pg.key.get_pressed()
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                if keys[pg.K_LSHIFT]:
                    self.status = "run"
                else:
                    self.status = "walk"
            else:
                self.status = "idle"


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()