import math
import random


class PerlinNoise2D():

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.map = [[0 for _ in range(self.width)] for _ in range(self.height)]


        self.build()

    def build(self):

        self.build_one()
        self.noise()


    def build_one(self):
        round_key = 20
        # Iterate over the rows with a step of roundKey
        for i in range(0, len(self.map), round_key):
            # Iterate over the columns with a step of roundKey
            for j in range(0, len(self.map[i]), round_key):
                # Modify the element at position [i][j]
                self.map[i][j] = random.randint(0, 360)

    def noise(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                # Skip only if both i and j are multiples of 20, but not at (0, 0)
                if i % 20 == 0 and j % 20 == 0:
                    continue
                else:
                    self.map[i][j] = self.calculateValue(i, j)

    def calculateValue(self, i, j):

        # Calculate distance to corner points (j mod 20 = predefined value)
        # get float based on distance values no clue what to do then
        # maybe make calculations based on where the point is and the distance
        # if 8 from point A (being 0) and 12 (being 1) from point B it is 0.4
        # but how would the second axis affect this?
        # say it is 5 from C (0) and 15 from D (1) it would be 0.25
        # How would 0.25 and 0.4 combine? middle (0.25 + 0.4 = 0.65 / 2 = 0.325)?


        # Let's just build a coordinate system for now which combines theses valuess
        # Calculate border points based on i, j within the map
        border_A = i - (i % 20)
        border_B = border_A + 20
        border_C = j - (j % 20)
        border_D = border_C + 20

        # Ensure border_B does not exceed map height
        if border_B > self.height:
            print(f"border_B ({border_B}) out of bounds. Adjusting to self.height ({self.height}).")
            border_B = self.height

        # Ensure border_D does not exceed map width
        if border_D > self.width:
            print(f"border_D ({border_D}) out of bounds. Adjusting to self.width ({self.width}).")
            border_D = self.width

        # Ensure border_A is within height bounds
        if border_A >= self.height or border_A < 0:
            print(f"border_A ({border_A}) out of bounds.")

        # Ensure border_C is within width bounds
        if border_C >= self.width or border_C < 0:
            print(f"border_C ({border_C}) out of bounds.")

        point_A = self.map[border_A][border_C] if border_A < self.height and border_C < self.width else 0
        point_B = self.map[border_A][border_D - 1] if border_A < self.height and border_D <= self.width else 0
        point_C = self.map[border_B - 1][border_C] if border_B <= self.height and border_C < self.width else 0
        point_D = self.map[border_B - 1][border_D - 1] if border_B <= self.height and border_D <= self.width else 0

        x_frac = (i % 20) / 20
        y_frac = (j % 20) / 20

        val_AB = point_A + (point_B - point_A) * x_frac
        val_CD = point_C + (point_D - point_C) * x_frac
        val_final = val_AB + (val_CD - val_AB) * y_frac

        return val_final