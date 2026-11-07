from hitable import Hitable, hit_record
from vec3 import Vec3, dot
from ray import Ray
import math

class Sphere(Hitable):
    def __init__(self, cen: Vec3=None, r: float=None):
        self.center = cen
        self.radius = r

    def hit(self, r: Ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        oc = r.origin() - self.center
        a = dot(r.direction(), r.direction())
        b = dot(oc, r.direction())
        c = dot(oc, oc) - self.radius * self.radius
        discriminant = b*b - a*c
        if discriminant > 0:
            temp = (-b - math.sqrt(b*b - a*c)) / a
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = r.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                return True
            temp = (-b + math.sqrt(b*b - a*c)) / a
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = r.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                return True
        return False