import os
import random

from world.worldGeneration.PerlinNoise2D import PerlinNoise2D

class WorldBuilder:
    def __init__(self, worldWidth, worldHeight, base_dist):
        self.worldWidth = int(worldWidth)
        self.worldHeight = int(worldHeight)
        self.base_dist = int(base_dist)
        self.map = [[0 for _ in range(self.worldWidth)] for _ in range(self.worldHeight)]
        self.createMap()
        self.worldFile = self.buildWorld()

    def buildWorld(self):
        directory = "world/levels"
        if not os.path.exists(directory):
            os.makedirs(directory)
        while True:
            randomLevelName = ''.join(str(random.randint(0,9)) for _ in range(20)) + ".txt"
            fullPath = os.path.join(directory, randomLevelName)
            if not os.path.exists(fullPath):
                break

        with open(fullPath, "w") as file:
            for row in self.map:
                file.write(",".join(map(str, row)) + "\n")

        return fullPath

    def createMap(self):
        # Assuming PerlinNoise2D is properly returning a map with values
        self.height_map = PerlinNoise2D(self.worldWidth, self.worldHeight, self.base_dist).map
        self.temperature_map = PerlinNoise2D(self.worldWidth, self.worldHeight, self.base_dist).map
        self.vegetation_map = PerlinNoise2D(self.worldWidth, self.worldHeight, self.base_dist).map

        self.convert_height_map()
        self.convert_temperature_map()
        self.convert_vegetation_map()

    def convert_height_map(self):
        for row_index, tileRow in enumerate(self.height_map):
            for col_index, tile in enumerate(tileRow):
                if tile < 80:
                    self.map[row_index][col_index] = 1
                elif tile < 210:
                    self.map[row_index][col_index] = 2
                else:
                    self.map[row_index][col_index] = 3


    def convert_temperature_map(self):
        for row_index, tileRow in enumerate(self.temperature_map):
            for col_index, tile in enumerate(tileRow):
                self.map[row_index][col_index] *= 10
                if tile < 40:
                    self.map[row_index][col_index] += 1
                elif tile < 210:
                    self.map[row_index][col_index] += 2
                else:
                    self.map[row_index][col_index] += 3

    def convert_vegetation_map(self):
        for row_index, tileRow in enumerate(self.vegetation_map):
            for col_index, tile in enumerate(tileRow):
                self.map[row_index][col_index] *= 10
                if tile < 190:
                    self.map[row_index][col_index] += 1
                else:
                    self.map[row_index][col_index] += 2