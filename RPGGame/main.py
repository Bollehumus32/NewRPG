import pygame as pg
from config import *
from sprites import *
import sys

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font = pg.font.Font('assets/Retro Gaming.ttf', 20)
        self.running = True

    def new(self):
        # new game starts
        self.playing = True
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.blocks = pg.sprite.LayeredUpdates()
        self.enemies = pg.sprite.LayeredUpdates()
        self.attacks = pg.sprite.LayeredUpdates()

        self.player = Player(self, 1, 2)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pg.display.update()

    def loop(self):
        # Game Loop:
        while self.playing:
            self.events()
            self.update()
            self.draw()

        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass


def main():
    g = Game()
    g.intro_screen()
    g.new()
    while g.running:
        g.loop()
        g.game_over()

    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()

        
