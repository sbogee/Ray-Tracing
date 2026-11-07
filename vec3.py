import math
import sys

class Vec3:
    def __init__(self, e0: float=0.0, 
                       e1: float=0.0, 
                       e2: float=0.0):
        self.e = [e0, e1, e2]

    @property
    def x(self) -> float: return self.e[0]

    @property
    def y(self) -> float: return self.e[1]

    @property
    def z(self) -> float: return self.e[2]

    @property
    def r(self) -> float: return self.e[0]

    @property
    def g(self) -> float: return self.e[1]

    @property
    def b(self) -> float: return self.e[0]

    def __pos__(self) -> 'Vec3':
        return self

    def __neg__(self) -> 'Vec3':
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, i: int) -> float:
        return self.e[i]

    def __setitem__(self, i: int, value: float) -> None:
        self.e[i] = value

    def __iadd__(self, other: 'Vec3') -> 'Vec3':
        self.e[0] += other.e[0]
        self.e[1] += other.e[1]
        self.e[2] += other.e[2]
        return self

    def __isub__(self, other: 'Vec3') -> 'Vec3':
        self.e[0] -= other.e[0]
        self.e[1] -= other.e[1]
        self.e[2] -= other.e[2]
        return self

    def __imul__(self, other: 'Vec3') -> 'Vec3':
        self.e[0] *= other.e[0]
        self.e[1] *= other.e[1]
        self.e[2] *= other.e[2]
        return self

    def __itruediv__(self, other: 'Vec3') -> 'Vec3':
        self.e[0] /= other.e[0]
        self.e[1] /= other.e[1]
        self.e[2] /= other.e[2]
        return self

    def imul_scalar(self, t: float) -> 'Vec3':
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def itruediv_scalar(self, t: float) -> 'Vec3':
        k = 1.0 / t
        self.e[0] *= k
        self.e[1] *= k
        self.e[2] *= k
        return self

    def squared_length(self) -> float:
        return self.e[0]**2 + self.e[1]**2 + self.e[2]**2

    def length(self) -> float:
        return math.sqrt(self.squared_length())

    def make_unit_vector(self):
        if self.length != 0:
            k = 1.0 / self.length()
            self.e[0] *= k
            self.e[1] *= k
            self.e[2] *= k

    @classmethod
    def from_stream(cls, stream=sys.stdin) -> 'Vec3':
        line = stream.readline()
        tokens = line.split()
        return cls(float(tokens[0]), float(tokens[1]), float(tokens[2]))

    def __str__(self) -> str:
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def __repr__(self) -> str:
        return f"Vec3({self.e[0]}, {self.e[1]}, {self.e[2]})"

    def __add__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])

    def __sub__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])

    def __mul__(self, other) -> 'Vec3':
        if isinstance(other, Vec3):
            return Vec3(self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2])
        elif isinstance(other, (int, float)):
            return Vec3(self.e[0] * other, self.e[1] * other, self.e[2] * other)

    def __rmul__(self, other: float) -> 'Vec3':
        return self.__mul__(other)

    def __truediv__(self, other)-> 'Vec3':
        if isinstance(other, Vec3):
            return Vec3(self.e[0] / other.e[0], self.e[1] / other.e[1], self.e[2] / other.e[2])
        elif isinstance(other, (int, float)):
            return Vec3(self.e[0] / other, self.e[1] / other, self.e[2] / other)

def dot(v1: Vec3, v2: Vec3) -> float:
    return v1.e[0]*v2.e[0] + v1.e[1]*v2.e[1] + v1.e[2]*v2.e[2]

def cross(v1: Vec3, v2: Vec3) -> Vec3:
    return Vec3(
        (v1.e[1] * v2.e[2] - v1.e[2] * v2.e[1]),
        (-(v1.e[0] * v2.e[2] - v1.e[2] * v2.e[0])),
        (v1.e[0] * v2.e[1] - v1.e[1] * v2.e[0])
    )

def unit_vector(v: Vec3) -> Vec3:
    return v / v.length()