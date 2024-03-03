import os.path
import random

from world.worldGeneration.PerlinNoise2D import PerlinNoise2D


class WorldBuilder:

    def __init__(self, worldWidth, worldHeight):
        self.worldWidth = int(worldWidth)
        self.worldHeight = int(worldHeight)

        self.worldFile = self.buildWorld()
        perlinNoise2D = PerlinNoise2D(100,100)

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
                    file.write(str(random.randint(0,1)) + ",")
                file.write("\n")

        return randomLevelName