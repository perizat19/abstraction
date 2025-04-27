import random
from cylinder import Cylinder
from sphere import Sphere
from cube import Cube


objects_list = []
for i in range(10):
    shape_choices = ['Cylinder', 'Cube', 'Sphere']
    shape_type = random.choice(shape_choices)
    if shape_type == 'Cylinder':
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        obj = Cylinder(radius, height)
        area = obj.surface_area()
        volume = obj.volume()
    elif shape_type == 'Cube':
        side = random.randint(1, 10)
        obj = Cube(side)
        area = obj.surface_area()
        volume = obj.volume()
    elif shape_type == 'Sphere':
        radius = random.randint(1, 10)
        obj = Sphere(radius)
        area = obj.surface_area()
        volume = obj.volume()
    objects_list.append(obj)

for i in objects_list:
    print(obj.__str__())
    print(f'Surface area: {area}')
    print(f'Volume: {volume}')

