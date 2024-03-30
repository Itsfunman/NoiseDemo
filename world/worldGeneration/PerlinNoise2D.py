import random

class PerlinNoise2D:
    def __init__(self, width, height, base_dist):
        self.width = width
        self.height = height
        self.base_dist = base_dist
        self.map = [[170 for _ in range(self.width)] for _ in range(self.height)]
        self.build()


    def build(self):
        self.build_one()
        self.fill_lines()
        self.noise()

    def build_one(self):
        # Ensuring we stay within bounds
        for i in range(0, self.height, self.base_dist):
            for j in range(0, self.width, self.base_dist):
                self.map[i][j] = random.choice([0,255])

    def fill_lines(self):
        self.noise_v()
        self.noise_h()

    def noise(self):
        for i in range(0, self.height):
            if (i % self.base_dist) != 0:
                for j in range(0, self.height):
                    if (j % self.base_dist) != 0:
                        val_h = self.calc_h(i,j)
                        val_v = self.calc_v(i,j)

                        val = int((val_h + val_v) / 2)
                        self.map[i][j] = val


    def noise_h(self):
        for i in range(0, self.height, self.base_dist):
            for j in range(0, self.width):
                if (j % self.base_dist) != 0 and self.map[i][j] != 0 and self.map[i][j] != 255:
                    val = self.calc_h(i,j)

                    self.map[i][j] = val

    def noise_v(self):
        for j in range(0, self.width, self.base_dist):
            for i in range(0, self.height):
                if (i % self.base_dist) != 0 and self.map[i][j] != 0 and self.map[i][j] != 255:

                    val = self.calc_v(i,j)
                    self.map[i][j] = val

    def calc_h(self, i, j):
        base_diff = j % self.base_dist
        base_point = self.map[i][j - base_diff]

        # Ensure the index for opp_point does not exceed self.width - 1
        opp_index = min(j + (self.base_dist - base_diff), self.width - 1)
        opp_point = self.map[i][opp_index]

        return self.calc_diff(base_point, opp_point, base_diff)

    def calc_v(self, i, j):
        base_diff = i % self.base_dist
        base_point = self.map[i - base_diff][j]

        # Ensure the index for opp_point does not exceed self.width - 1
        opp_index = min(i + (self.base_dist - base_diff), self.height - 1)
        opp_point = self.map[opp_index][j]

        return self.calc_diff(base_point, opp_point, base_diff)

    def calc_diff(self, base_point, opp_point, base_diff):
        if base_point == opp_point:
            return base_point
        else:
            val_diff = abs(base_point - opp_point)
            if base_point > opp_point:
                return self.calc_val(val_diff, self.base_dist - base_diff, base_point, opp_point)
            else:
                return self.calc_val(val_diff, base_diff, base_point, opp_point)


    def calc_val(self, val_diff, diff, base_point, opp_point):
        val = int(((val_diff / self.base_dist) * diff) + min(base_point, opp_point))
        val += random.randint(-5, 5)
        if val < 0:
            return 0
        elif val > 255:
            return 255
        else:
            return val