from world.entity import Entity
from world.objects.element import Element


class Tile(Entity):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.isOccupied = False
        self.occupyingElement = None

    def entered(self, element: Element):
        self.occupyingElement = element.id
        self.isOccupied = True

    def left(self):
        self.occupyingElement = None
        self.isOccupied = False

