import pygame


class LevelManager:

    def __init__(self, fileName):
        self.tiles = self.loadLevel(fileName)

    def drawLevel(self, window):
        tile_size = 25  # Adjust the tile size as needed
        for row_index, tileRow in enumerate(self.tiles):
            for col_index, tile in enumerate(tileRow):
                pygame.draw.rect(window, (255, 255, 255, int(tile)),
                                 (col_index * tile_size, row_index * tile_size, tile_size, tile_size))

    def loadLevel(self, filename):
        tiles = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                elements = line.strip().split(',')
                row = []
                for element in elements:
                    try:
                        # First, attempt to convert to float
                        num = int(element)
                        row.append(num)
                    except ValueError:
                        # If conversion fails, keep the original string
                        row.append(element)
                tiles.append(row)
        return tiles
