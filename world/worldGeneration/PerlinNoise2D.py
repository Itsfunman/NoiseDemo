import math
import random


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
                self.map[i][j] = random.randint(0, 1)

    def noise(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if j % 20 == 0:
                    pass
                else:
                    self.map[i][j] = self.calculateValue(i,j)

    def calculateValue(self, i, j):
        # Calculate distance to corner points (j mod 20 = predefined value)
        # get float based on distance values no clue what to do then
        # maybe make calculations based on where the point is and the distance
        # if 8 from point A (being 0) and 12 (being 1) from point B it is 0.4
        # but how would the second axis affect this?
        # say it is 5 from C (0) and 15 from D (1) it would be 0.25
        # How would 0.25 and 0.4 combine? middle (0.25 + 0.4 = 0.65 / 2 = 0.325)?


        # Let's just build a coordinate system for now which combines theses valuess
        border_A = i - (i % 2)
        border_B = border_A + 20
        border_C = j - (j % 20)
        border_D = border_C + 20

        point_A = self.map[border_A][border_C]
        point_B = self.map[border_A][border_D]
        point_C = self.map[border_B][border_C]
        point_D = self.map[border_B][border_D]

        diff_AD = (point_D - point_A) * -1
        diff_BC = (point_C - point_B) * -1

        x = i % 20
        y = j % 20

        val_one = self.get_pos_val(diff_AD, x, y)
        val_two = self.get_pos_val(diff_BC, x, y)

        val = (val_one + val_two) / 2
        return val

    def get_pos_val(self, diff, x, y):

        dis_one = self.calc_dis_down(x,y)
        dis_two = self.calc_dis_up(x,y)

        dis = dis_one + dis_two
        brackets = diff / dis
        return brackets * dis_one

    def calc_dis_down(self, x, y):
        hypo = math.sqrt(x**2 + y**2)
        return hypo

    def calc_dis_up(self, x, y):
        x1 = 20 - x
        y1 = 20 - y

        hypo = math.sqrt(x1 ** 2 + y1 ** 2)
        return hypo

