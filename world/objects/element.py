from world.entity import Entity


class Element(Entity):

    def __init__(self, x, y, width, height, id):
        super().__init__(x, y, width, height)
        self.id = id
