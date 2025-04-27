from shape3d import Shape3D
from math import pi


class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        return 'Cylinder'

    def surface_area(self):
        area = 2 * pi * self.radius * (self.radius + self.height)
        return area

    def volume(self):
        volume = pi * self.radius ** 2 * self.height
        return volume


