from hitable import Hitable, hit_record
from vec3 import Vec3, dot
from ray import Ray
import math
from material import Material

class Sphere(Hitable):
    def __init__(self, cen: Vec3=None, r: float=None, m: Material=None):
        self.center = cen
        self.radius = r
        self.material = m

    def hit(self, r: Ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        origin = r.origin()
        direction = r.direction()
        ocx = origin.x - self.center.x
        ocy = origin.y - self.center.y
        ocz = origin.z - self.center.z
        a = dot(direction, direction)
        b = ocx * direction.x + ocy * direction.y + ocz * direction.z
        c = ocx * ocx + ocy * ocy + ocz * ocz - self.radius * self.radius
        discriminant = b*b - a*c
        if discriminant > 0:
            sqrt_discriminant = math.sqrt(discriminant)
            temp = (-b - sqrt_discriminant) / a
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = Vec3(
                    origin.x + temp * direction.x,
                    origin.y + temp * direction.y,
                    origin.z + temp * direction.z,
                )
                rec.normal = Vec3(
                    (rec.p.x - self.center.x) / self.radius,
                    (rec.p.y - self.center.y) / self.radius,
                    (rec.p.z - self.center.z) / self.radius,
                )
                rec.mat_ptr = self.material
                return True
            temp = (-b + sqrt_discriminant) / a
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = Vec3(
                    origin.x + temp * direction.x,
                    origin.y + temp * direction.y,
                    origin.z + temp * direction.z,
                )
                rec.normal = Vec3(
                    (rec.p.x - self.center.x) / self.radius,
                    (rec.p.y - self.center.y) / self.radius,
                    (rec.p.z - self.center.z) / self.radius,
                )
                rec.mat_ptr = self.material
                return True
        return False