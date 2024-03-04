import pygame as pg
from world.levelManager import LevelManager
from world.worldGeneration.worldBuilder import WorldBuilder

class Game:
    def __init__(self):
        self.width = 80
        self.height = 80
        self.active_x_zero = 0
        self.active_y_zero = 0
        self.worldBuilder = WorldBuilder(worldWidth=self.width, worldHeight=self.height)

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
