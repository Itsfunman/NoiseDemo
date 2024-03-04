import os.path
import random

import numpy

from world.worldGeneration.PerlinNoise2D import PerlinNoise2D


class WorldBuilder:

    def __init__(self, worldWidth, worldHeight):
        self.worldWidth = int(worldWidth)
        self.worldHeight = int(worldHeight)

        self.perlinNoise2D = PerlinNoise2D(worldWidth,worldHeight)
        self.worldFile = self.buildWorld()

    def buildWorld(self):
        while True:
            randomLevelName = str(''.join(str(random.randint(0,9)) for _ in range(20)))
            randomLevelName += ".txt"
            directory = "world/levels"
            if not os.path.exists(directory):
                os.makedirs(directory)
            else:
                if randomLevelName not in os.listdir(directory):
                    randomLevelName = os.path.join(directory, randomLevelName)
                    break

        with open(randomLevelName, "w") as file:

            for i in range(self.worldHeight):
                for k in range(self.worldWidth):
                    file.write(str(int(numpy.round(self.perlinNoise2D.map[i][k] * 255))) + ",")
                file.write("\n")

        return randomLevelName