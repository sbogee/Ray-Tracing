from material import Material
from ray import Ray
from hitable import hit_record
from vec3 import Vec3
from random_utils import random_in_unit_sphere

class Lambertian(Material):
    def __init__(self, a: Vec3):
        self.albedo = a

    def scatter(self, r_in: Ray, rec: hit_record) -> bool:
        target = rec.p + rec.normal + random_in_unit_sphere()
        scattered = Ray(rec.p, target - rec.p)
        return True, self.albedo, scattered