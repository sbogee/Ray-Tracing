from vec3 import Vec3

def main():
    with open("file.ppm", "w", encoding="utf-8") as f:
        nx = 200
        ny = 100

        f.write(f"P3\n{nx} {ny}\n255\n")

        for j in range(ny-1, -1, -1):
            for i in range(nx):
                col = Vec3(i / nx, j / ny, 0.2)
                ir = int(255.99 * col[0])
                ig = int(255.99 * col[1])
                ib = int(255.99 * col[2])
                f.write(f"{ir} {ig} {ib}\n")

        f.close()

main()