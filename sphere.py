from shape3d import Shape3D
import math


class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return 'Sphere'

    def surface_area(self):
        area = 4 * math.pi * self.radius ** 2
        return area

    def volume(self):
        volume = 4/3 * math.pi * self.radius ** 3
        return volume








