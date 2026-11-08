from vec3 import Vec3, unit_vector
from hitable import Hitable, hit_record
from ray import Ray
from sphere import Sphere
from hitable_list import Hitable_list
from camera import Camera
import random
import math
from lambertian import Lambertian
from metal import Metal

MAXFLOAT = 3.4028235e+38

def color(r: Ray, world: Hitable, depth: int) -> Vec3:
    rec = hit_record()
    if world.hit(r, 0.001, MAXFLOAT, rec):
        scatter_result, attenuation, scattered = rec.mat_ptr.scatter(r, rec)
        if depth < 50 and scatter_result:
            return attenuation * color(scattered, world, depth + 1)
        else:
            return Vec3(0, 0, 0)
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

        list = [Sphere(Vec3(0, 0, -1), 0.5, Lambertian(Vec3(0.8, 0.3, 0.3))), 
                Sphere(Vec3(0, -100.5, -1), 100, Lambertian(Vec3(0.8, 0.8, 0.0))),
                Sphere(Vec3(1, 0, -1), 0.5, Metal(Vec3(0.8, 0.6, 0.2))),
                Sphere(Vec3(-1, 0, -1), 0.5, Metal(Vec3(0.8, 0.8, 0.8)))]
        world = Hitable_list(list, 4)

        cam = Camera()

        for j in range(ny-1, -1, -1):
            row = []
            for i in range(nx):
                col = Vec3(0, 0, 0)

                for s in range(ns):
                    u = (i + random.random()) / nx
                    v = (j + random.random()) / ny
                    r = cam.get_ray(u, v)
                    p = r.point_at_parameter(2.0)
                    col += color(r, world, 0)

                col.itruediv_scalar(ns)
                col = Vec3(math.sqrt(col[0]), math.sqrt(col[1]), math.sqrt(col[2]))
                ir = int(255.99 * col[0])
                ig = int(255.99 * col[1])
                ib = int(255.99 * col[2])
                row.append(f"{ir} {ig} {ib}\n")
            f.write("".join(row))


main()