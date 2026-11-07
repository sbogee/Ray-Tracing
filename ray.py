from vec3 import Vec3

class Ray:
    def __init__(self, a: Vec3, b: Vec3):
        self.A = a
        self.B = b

    def origin(self) -> Vec3:
        return self.A

    def direction(self) -> Vec3:
        return self.B

    def point_at_parameter(self, t: float) -> Vec3:
        return self.A + t * self.B