from __future__ import annotations

from ray import Ray
from vec3 import Vec3
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from material import Material

@dataclass
class hit_record:
    t: float = 0.0
    p: Vec3 = field(default_factory=Vec3)
    normal: Vec3 = field(default_factory=Vec3)
    mat_ptr: Material | None = None

class Hitable(ABC):
    @abstractmethod
    def hit(self, r: Ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        pass