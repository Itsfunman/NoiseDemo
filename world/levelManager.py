import pygame

class LevelManager:

    def __init__(self, fileName):
        self.tiles = self.loadLevel(fileName)

    def drawLevel(self, window):
        tile_size = 1 # Adjust the tile size as needed
        for row_index, tileRow in enumerate(self.tiles):
            for col_index, tile in enumerate(tileRow):

                rgb_color = self.color_from_tile(tile)

                rect = pygame.Rect(col_index * tile_size, row_index * tile_size, tile_size, tile_size)
                pygame.draw.rect(window, rgb_color, rect)

    def loadLevel(self, filename):
        tiles = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                elements = line.strip().split(',')
                row = []
                for element in elements:
                    if element:  # Check if the element is not an empty string
                        try:
                            num = int(element)
                            row.append(num)
                        except ValueError:
                            # If conversion fails, keep the original string
                            row.append(element)
                    # Optionally, handle empty strings differently here if needed
                tiles.append(row)
        return tiles

    def color_from_tile(self, tile_str):
        tile = int(tile_str)

        #water
        if tile == 111 or tile == 112 or tile == 121 or tile == 122 or tile == 131 or tile == 132:
            return (0,0,255)
        #snow
        elif tile == 211:
            return (255,255,255)
        #snow fir
        elif tile == 212:
            return (17,66,30)
        #grass
        elif tile == 221:
            return (0,255,0)
        #forest
        elif tile == 222:
            return (68,179,97)
        #desert
        elif tile == 231:
            return (244,250,90)
        elif tile == 232:
            return (244,250,90)
        #mountain
        elif tile == 311 or tile == 312 or tile == 321 or tile == 322:
            return (91,91,91)
        #snowy mountain
        elif tile == 331 or tile == 332:
            return (143,143,143)