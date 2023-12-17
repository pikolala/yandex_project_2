import pygame as pg
import sys

FPS = 60
WIDTH = 800
HEIGHT = 600

pg.init()
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
                return True

def menu():
    screen.fill((0, 0, 0))
    background = pg.image.load("menu_materials/фон.png")
    screen.blit(background, (0, 0))
    button_start = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2, (HEIGHT // 2) - 50 // 2 - 100, 200, 50))
    button_quit = Button(screen, pg.Color("darkslategray4"), ((WIDTH // 2) - 200 // 2, (HEIGHT // 2) - 50 // 2 - 0, 200, 50))

    font = pg.font.Font(None, 36)
    text_button_start = font.render('Играть', True, (180, 0, 0))
    text_button_quit = font.render('Выйти из игры', True, (180, 0, 0))

    screen.blit(text_button_start, ((WIDTH // 2) - 200 // 2 + 100 - 36, (HEIGHT // 2) - 50 // 2 - 100 + 25 - 12))
    screen.blit(text_button_quit, ((WIDTH // 2) - 200 // 2 + 10, (HEIGHT // 2) - 50 // 2 + 10))

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

if __name__ == "__main__":
    menu()