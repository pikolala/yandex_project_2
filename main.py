import pygame as pg
import sys


FPS = 60
WIDTH = 800
HEIGHT = 600

s = open("menu_materials/settings.txt", "r").readlines()
s = [i.replace("\n", "") for i in s]
SOUND_VOLUME = float(s[0])
MUSIC_VOLUME = float(s[1])



pg.init()
pg.mixer.init()

sound_channel = pg.mixer.Channel(0)
music_channel = pg.mixer.Channel(1)

menu_music = pg.mixer.Sound("menu_materials/menu_music.mp3")
buttons_sound = pg.mixer.Sound("menu_materials/press_button.mp3")

sound_channel.set_volume(SOUND_VOLUME)
music_channel.set_volume(MUSIC_VOLUME)

pg.display.set_caption("Game")
icon = pg.image.load("menu_materials/icon.png")
pg.display.set_icon(icon)
screen = pg.display.set_mode((WIDTH, HEIGHT))



class Button:
    def __init__(self, screen, color, rect, width=0):
        self.button = pg.draw.rect(screen, color, rect, width)

    def clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.collidepoint(event.pos):
                sound_channel.play(buttons_sound)
                return True

def live():
    while 1:
        sound_channel.set_volume(SOUND_VOLUME)
        music_channel.set_volume(MUSIC_VOLUME)


def menu():
    screen.fill((0, 0, 0))
    background = pg.image.load("menu_materials/фон.png")
    screen.blit(background, (0, 0))
    button_start = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2, (HEIGHT // 2) - 50 // 2 - 100, 200, 50))
    button_settings = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2, (HEIGHT // 2) - 50 // 2 - 0, 200, 50))
    button_quit = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2, (HEIGHT // 2) - 50 // 2 + 100, 200, 50))


    font = pg.font.Font(None, 36)
    text_button_start = font.render('Играть', True, (180, 0, 0))
    text_button_quit = font.render('Выйти из игры', True, (180, 0, 0))
    text_button_settings = font.render('Настройки', True, (180, 0, 0))

    screen.blit(text_button_start, ((WIDTH // 2) - 200 // 2 + 100 - 36, (HEIGHT // 2) - 50 // 2 - 100 + 25 - 12))
    screen.blit(text_button_settings,((WIDTH // 2) - 200 // 2 + 36, (HEIGHT // 2) - 50 // 2 + 10))
    screen.blit(text_button_quit, ((WIDTH // 2) - 200 // 2 + 10, (HEIGHT // 2) - 50 // 2 + 110))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            if button_quit.clicked(event):
                sys.exit()

            if button_start.clicked(event):
                play_menu()

            if button_settings.clicked(event):
                settings_menu()

        pg.display.flip()

def play_menu():
    f = open("menu_materials/levels.txt")
    s = f.readline()
    f.close()
    screen.fill((0, 0, 0))
    background = pg.image.load("menu_materials/фон.png")
    screen.blit(background, (0, 0))

    level1_button = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2 - 100, (HEIGHT // 2) - 50 // 2 - 100, 100, 100))
    level2_button = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2 + 50, (HEIGHT // 2) - 50 // 2 - 100, 100, 100))
    level3_button = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2 + 200, (HEIGHT // 2) - 50 // 2 - 100, 100, 100))
    button_back = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2, (HEIGHT // 2) - 50 // 2 + 100, 200, 50))

    font = pg.font.Font(None, 100)
    font1 = pg.font.Font(None, 40)
    text_level1_button = font.render('1', True, (180, 0, 0))
    text_level2_button = font.render('2', True, (180, 0, 0))
    text_level3_button = font.render('3', True, (180, 0, 0))
    text_button_back = font1.render('Назад', True, (180, 0, 0))

    screen.blit(text_level1_button, ((WIDTH // 2) - 200 // 2 - 100 + 28, (HEIGHT // 2) - 50 // 2 - 100 + 18))
    screen.blit(text_level2_button, ((WIDTH // 2) - 200 // 2 + 50 + 28, (HEIGHT // 2) - 50 // 2 - 100 + 18))
    screen.blit(text_level3_button, ((WIDTH // 2) - 200 // 2 + 200 + 28, (HEIGHT // 2) - 50 // 2 - 100 + 18))
    screen.blit(text_button_back, ((WIDTH // 2) - 200 // 2 + 56, (HEIGHT // 2) - 50 // 2 + 100 + 12, 200, 50))

    if s.count("+") < 2:
        pg.draw.line(screen, pg.color.Color("grey"), ((WIDTH // 2) - 200 // 2 + 50, (HEIGHT // 2) - 50 // 2 - 100), ((WIDTH // 2) - 200 // 2 + 150, (HEIGHT // 2) - 50 // 2 - 0), 10)
        pg.draw.line(screen, pg.color.Color("grey"),((WIDTH // 2) - 200 // 2 + 150, (HEIGHT // 2) - 50 // 2 - 100), ((WIDTH // 2) - 200 // 2 + 50, (HEIGHT // 2) - 50 // 2 - 0), 10)
    if s.count("+") < 3:
        pg.draw.line(screen, pg.color.Color("grey"), ((WIDTH // 2) - 200 // 2 + 200, (HEIGHT // 2) - 50 // 2 - 100), ((WIDTH // 2) - 200 // 2 + 300, (HEIGHT // 2) - 50 // 2 - 0), 10)
        pg.draw.line(screen, pg.color.Color("grey"), ((WIDTH // 2) - 200 // 2 + 300, (HEIGHT // 2) - 50 // 2 - 100), ((WIDTH // 2) - 200 // 2 + 200, (HEIGHT // 2) - 50 // 2 - 0), 10)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if button_back.clicked(event):
                menu()

        pg.display.flip()

def settings_menu():
    images_sound = ["menu_materials/sound_unactive.png", "menu_materials/sound_active.png"]
    global SOUND_VOLUME
    global MUSIC_VOLUME

    sprite_sound = pg.sprite.Sprite()
    if SOUND_VOLUME == 0:
        sprite_sound.image = pg.image.load(images_sound[0])
    else:
        sprite_sound.image = pg.image.load(images_sound[1])
    sprite_sound.rect = sprite_sound.image.get_rect()
    sprite_sound.rect.x = 300
    sprite_sound.rect.y = 150
    
    sprite_music = pg.sprite.Sprite()
    if MUSIC_VOLUME == 0:
        sprite_music.image = pg.image.load(images_sound[0])
    else:
        sprite_music.image = pg.image.load(images_sound[1])
    sprite_music.rect = sprite_sound.image.get_rect()
    sprite_music.rect.x = 300
    sprite_music.rect.y = 250

    plus = pg.image.load("menu_materials/plus.png")
    minus = pg.image.load("menu_materials/minus.png")
    plus1 = pg.image.load("menu_materials/plus.png")
    minus1 = pg.image.load("menu_materials/minus.png")


    font = pg.font.Font(None, 52)
    text_sound = font.render('Звук', True, (180, 0, 0))
    text_music = font.render('Музыка', True, (180, 0, 0))

    font1 = pg.font.Font(None, 40)
    text_button_back = font1.render('Назад', True, (180, 0, 0))


    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if sprite_sound.rect.collidepoint(event.pos):
                    if SOUND_VOLUME == 0:
                        SOUND_VOLUME = 1
                    else:
                        SOUND_VOLUME = 0

                if sprite_music.rect.collidepoint(event.pos):
                    if MUSIC_VOLUME == 0:
                        MUSIC_VOLUME = 1
                    else:
                        MUSIC_VOLUME = 0


                if pg.rect.Rect((450, 215, 32, 32)).collidepoint(event.pos) and SOUND_VOLUME != 1:
                    SOUND_VOLUME = round(SOUND_VOLUME + 0.1, 1)

                if pg.rect.Rect((300, 215, 32, 32)).collidepoint(event.pos) and SOUND_VOLUME != 0:
                    SOUND_VOLUME = round(SOUND_VOLUME - 0.1, 1)

                if pg.rect.Rect((450, 315, 32, 32)).collidepoint(event.pos) and MUSIC_VOLUME != 1:
                    MUSIC_VOLUME = round(MUSIC_VOLUME + 0.1, 1)

                if pg.rect.Rect((300, 315, 32, 32)).collidepoint(event.pos) and MUSIC_VOLUME != 0:
                    MUSIC_VOLUME = round(MUSIC_VOLUME - 0.1, 1)

            if button_back.clicked(event):
                f = open("menu_materials/settings.txt", "w")
                f.write(str(SOUND_VOLUME) + "\n")
                f.write(str(MUSIC_VOLUME))
                f.close()
                menu()

        sound_channel.set_volume(SOUND_VOLUME)
        music_channel.set_volume(MUSIC_VOLUME)

        screen.fill((0, 0, 0))
        background = pg.image.load("menu_materials/фон.png")
        screen.blit(background, (0, 0))

        if SOUND_VOLUME != 0:
            sprite_sound.image = pg.image.load(images_sound[1])
        else:
            sprite_sound.image = pg.image.load(images_sound[0])

        if MUSIC_VOLUME != 0:
            sprite_music.image = pg.image.load(images_sound[1])
        else:
            sprite_music.image = pg.image.load(images_sound[0])

        button_back = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2, (HEIGHT // 2) - 50 // 2 + 100, 200, 50))

        screen.blit(sprite_sound.image, sprite_sound.rect)
        screen.blit(sprite_music.image, sprite_music.rect)

        text_s = font1.render(str(SOUND_VOLUME), True, (0, 180, 0))
        text_m = font1.render(str(MUSIC_VOLUME), True, (0, 180, 0))

        screen.blit(plus, (450, 215))
        screen.blit(minus, (300, 215))
        screen.blit(plus1, (450, 315))
        screen.blit(minus1, (300, 315))

        screen.blit(text_sound, ((WIDTH // 2) - 200 // 2 + 100 - 16, (HEIGHT // 2) - 50 // 2 - 110))
        screen.blit(text_music, ((WIDTH // 2) - 200 // 2 + 100 - 16, (HEIGHT // 2) - 50 // 2 - 10))
        screen.blit(text_s, ((WIDTH // 2) - 200 // 2 + 90, (HEIGHT // 2) - 50 // 2 - 55))
        screen.blit(text_m, ((WIDTH // 2) - 200 // 2 + 90, (HEIGHT // 2) - 50 // 2 + 45))
        screen.blit(text_button_back, ((WIDTH // 2) - 200 // 2 + 56, (HEIGHT // 2) - 50 // 2 + 100 + 12, 200, 50))
        pg.display.flip()

if __name__ == "__main__":
    music_channel.play(menu_music)
    menu()