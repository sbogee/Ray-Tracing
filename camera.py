from vec3 import Vec3
from ray import Ray

class Camera:
    def __init__(self):
        self.lower_left_corner = Vec3(-2.0, -1.0, -1.0)
        self.horizontal = Vec3(4.0, 0.0, 0.0)
        self.vertical = Vec3(0.0, 2.0, 0.0)
        self.origin = Vec3(0.0, 0.0, 0.0)

    def get_ray(self, u: float, v: float) -> Ray:
        return Ray(self.origin, 
                   self.lower_left_corner + 
                   u * self.horizontal + 
                   v * self.vertical - self.origin)