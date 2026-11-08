from material import Material
from ray import Ray
from hitable import hit_record
from vec3 import Vec3, dot, unit_vector

def reflect(v: Vec3, n: Vec3) -> Vec3:
    return v - 2 * dot(v, n) * n

class Metal(Material):
    def __init__(self, a: Vec3):
        self.albedo = a

    def scatter(self, r_in: Ray, rec: hit_record) -> bool:
        reflected = reflect(unit_vector(r_in.direction()), rec.normal)
        scattered = Ray(rec.p, reflected)
        return dot(scattered.direction(), rec.normal) > 0, self.albedo, scattered