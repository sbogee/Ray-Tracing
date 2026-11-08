import random

from vec3 import Vec3


def random_in_unit_sphere() -> Vec3:
    while True:
        x = 2.0 * random.random() - 1.0
        y = 2.0 * random.random() - 1.0
        z = 2.0 * random.random() - 1.0
        if x**2 + y**2 + z**2 < 1.0:
            return Vec3(x, y, z)
