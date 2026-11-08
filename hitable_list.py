from hitable import Hitable, hit_record
from vec3 import Vec3, dot
from ray import Ray
import math

class Hitable_list(Hitable):
    def __init__(self, l: list['Hitable'], n: int):
        self.list = l
        self.list_size = n

    def hit(self, r: Ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        temp_rec = hit_record()
        hit_anything = False
        closest_so_far = t_max
        for i in range(self.list_size):
            if self.list[i].hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.mat_ptr = temp_rec.mat_ptr
        return hit_anything