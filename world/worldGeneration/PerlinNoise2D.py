import random

import numpy


class PerlinNoise2D():

    # width and height should be dividable by 20, 10 and 5
    def __init__(self, width, height):
        self.map = [[0 for _ in range(width)] for _ in range(height)]
        self.build()

    def build(self):

        self.build_one()
        self.calculate()

        for row in self.map:
            print(row)

    def build_one(self):
        round_key = 20
        # Iterate over the rows with a step of roundKey
        for i in range(0, len(self.map), round_key):
            # Iterate over the columns with a step of roundKey
            for j in range(0, len(self.map[i]), round_key):
                # Modify the element at position [i][j]
                self.map[i][j] = random.randint(0, 1) * 10

    def calculate(self):
        pass