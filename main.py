from vec3 import Vec3, unit_vector
from ray import Ray

def color(r: Ray) -> Vec3:
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