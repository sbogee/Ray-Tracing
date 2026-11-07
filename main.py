from vec3 import Vec3, unit_vector, dot
from hitable import Hitable, hit_record
from ray import Ray
from sphere import Sphere
from hitable_list import Hitable_list
from camera import Camera
import random
import math

MAXFLOAT = 3.4028235e+38

def random_in_unit_sphere() -> Vec3:
    while True:
        x = 2.0 * random.random() - 1.0
        y = 2.0 * random.random() - 1.0
        z = 2.0 * random.random() - 1.0
        if x**2 + y**2 + z**2 < 1.0:
            return Vec3(x, y, z)

def color(r: Ray, world: Hitable) -> Vec3:
    rec = hit_record()
    attenuation = 1.0
    while world.hit(r, 0.001, MAXFLOAT, rec):
        target = rec.p + rec.normal + random_in_unit_sphere()
        r = Ray(rec.p, target - rec.p)
        attenuation *= 0.5

    unit_direction = unit_vector(r.direction())
    t = 0.5 * (unit_direction.y + 1.0)
    sky_color = (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)
    return attenuation * sky_color


def main():
    with open("file.ppm", "w", encoding="utf-8") as f:
        nx = 200
        ny = 100
        ns = 100

        f.write(f"P3\n{nx} {ny}\n255\n")

        list = [Sphere(Vec3(0, 0, -1), 0.5), Sphere(Vec3(0, -100.5, -1), 100)]
        world = Hitable_list(list, 2)

        cam = Camera()

        for j in range(ny-1, -1, -1):
            row = []
            for i in range(nx):
                col = Vec3(0, 0, 0)

                for s in range(ns):
                    u = (i + random.random()) / nx
                    v = (j + random.random()) / ny
                    r = cam.get_ray(u, v)
                    col += color(r, world)

                col.itruediv_scalar(ns)
                col = Vec3(math.sqrt(col[0]), math.sqrt(col[1]), math.sqrt(col[2]))
                ir = int(255.99 * col[0])
                ig = int(255.99 * col[1])
                ib = int(255.99 * col[2])
                row.append(f"{ir} {ig} {ib}\n")
            f.write("".join(row))


main()