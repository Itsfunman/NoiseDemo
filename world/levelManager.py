import pygame

class LevelManager:

    def __init__(self, fileName):
        self.tiles = self.loadLevel(fileName)

    def drawLevel(self, window):
        tile_size = 25  # Adjust the tile size as needed
        for row_index, tileRow in enumerate(self.tiles):
            for col_index, tile in enumerate(tileRow):
                if tile == 0:
                    pygame.draw.rect(window, (0, 0, 255),
                                     (col_index * tile_size, row_index * tile_size, tile_size, tile_size))
                elif tile == 1:
                    pygame.draw.rect(window, (0, 255, 0),
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
                        row.append(int(element))
                    except ValueError:
                        row.append(element)

                tiles.append(row)

        return tiles