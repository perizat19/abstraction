from shape3d import Shape3D


class Cube(Shape3D):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return 'Cube'

    def surface_area(self):
        area = 6 * self.side ** 2
        return area

    def volume(self):
        volume = self.side ** 3
        return volume

