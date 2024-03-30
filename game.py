import pygame as pg
from world.levelManager import LevelManager
from world.worldGeneration.worldBuilder import WorldBuilder

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.base_dist = 20
        self.active_x_zero = 0
        self.active_y_zero = 0
        self.worldBuilder = WorldBuilder(self.width, self.height, self.base_dist)

    def run(self):
        pg.init()
        window = pg.display.set_mode((self.width, self.height))

        filename = self.worldBuilder.worldFile
        level_manager = LevelManager(filename)

        while True:
            self.checkInput()

            level_manager.drawLevel(window)
            pg.display.update()

    def checkInput(self):
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
