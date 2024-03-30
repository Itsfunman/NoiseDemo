import pygame

class LevelManager:

    def __init__(self, fileName):
        self.tiles = self.loadLevel(fileName)

    def drawLevel(self, window):
        tile_size = 5  # Adjust the tile size as needed
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
        if tile < 80:
            return (0, 0, 255)
        elif tile < 210:
            return (0, 255, 0)
        else:
            return (110,110,110)