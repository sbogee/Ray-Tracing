from vec3 import Vec3, unit_vector, dot
from ray import Ray
import math

def hit_sphere(center: Vec3, radius: float, r: Ray) -> float:
    oc = r.origin() - center
    a = dot(r.direction(), r.direction())
    b = 2.0 * dot(oc, r.direction())
    c = dot(oc, oc) - radius * radius
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return 0
    else:
        return (-b - math.sqrt(discriminant)) / (2.0 * a)


def color(r: Ray) -> Vec3:
    t = hit_sphere(Vec3(0, 0, -1), 0.5, r)
    if t > 0.0:
        N = unit_vector(r.point_at_parameter(t) - Vec3(0, 0, -1))
        return 0.5 * Vec3(N.x + 1, N.y + 1, N.z +1)
    unit_direction = unit_vector(r.direction())
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)


def main():
    with open("file.ppm", "w", encoding="utf-8") as f:
        nx = 200
        ny = 100

        f.write(f"P3\n{nx} {ny}\n255\n")

        lower_left_corner = Vec3(-2.0, -1.0, -1.0)
        horizontal = Vec3(4.0, 0.0, 0.0)
        vertical = Vec3(0.0, 2.0, 0.0)
        origin = Vec3(0.0, 0.0, 0.0)

        for j in range(ny-1, -1, -1):
            for i in range(nx):
                u = i / nx
                v = j / ny
                r = Ray(origin, lower_left_corner + u*horizontal + v*vertical)
                col = color(r)
                ir = int(255.99 * col[0])
                ig = int(255.99 * col[1])
                ib = int(255.99 * col[2])
                f.write(f"{ir} {ig} {ib}\n")

        f.close()

main()