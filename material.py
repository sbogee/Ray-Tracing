from __future__ import annotations

from abc import ABC, abstractmethod
from ray import Ray
from vec3 import Vec3
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hitable import hit_record

class Material(ABC):
    @abstractmethod
    def scatter(self, r_in: Ray, rec: hit_record, attenuation: Vec3, scattered: Ray) -> bool:
        pass