from vec3 import Vec3, unit_vector, dot
from hitable import Hitable, hit_record
from ray import Ray
from sphere import Sphere
from hitable_list import Hitable_list
from camera import Camera
import random

MAXFLOAT = 3.4028235e+38

def random_in_unit_sphere() -> Vec3:
    while True:
        p = 2.0 * Vec3(random.random(), random.random(), random.random()) - Vec3(1, 1, 1)
        if p.squared_length() < 1.0:
            break
    return p

def color(r: Ray, world: Hitable) -> Vec3:
    rec = hit_record()
    if world.hit(r, 0.0, MAXFLOAT, rec):
        target = rec.p + rec.normal + random_in_unit_sphere()
        return 0.5 * color(Ray(rec.p, target - rec.p), world)
    else:
        unit_direction = unit_vector(r.direction())
        t = 0.5 * (unit_direction.y + 1.0)
        return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)


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
            for i in range(nx):
                col = Vec3(0, 0, 0)

                for s in range(ns):
                    u = (i + random.random()) / nx
                    v = (j + random.random()) / ny
                    r = cam.get_ray(u, v)
                    p = r.point_at_parameter(2.0)
                    col += color(r, world)

                col.itruediv_scalar(ns)
                ir = int(255.99 * col[0])
                ig = int(255.99 * col[1])
                ib = int(255.99 * col[2])
                f.write(f"{ir} {ig} {ib}\n")

        f.close()

main()