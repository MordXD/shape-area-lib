"""shape_area_lib.shapes – базовые фигуры и их площади."""
from __future__ import annotations

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Shape(ABC):
    """Абстракция геометрической фигуры."""

    @abstractmethod
    def area(self) -> float:
        """Площадь фигуры."""


# ---------- Круг ---------- #
@dataclass(frozen=True)
class Circle(Shape):
    radius: float

    def __post_init__(self) -> None:
        if self.radius <= 0:
            raise ValueError("radius must be positive")

    def area(self) -> float:
        return math.pi * self.radius**2


# ---------- Треугольник ---------- #
@dataclass(frozen=True)
class Triangle(Shape):
    a: float
    b: float
    c: float

    def __post_init__(self) -> None:
        sides = sorted((self.a, self.b, self.c))
        if sides[0] <= 0:
            raise ValueError("sides must be positive")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("not a triangle")

    def area(self) -> float:
        # Формула Герона
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @property
    def is_right(self) -> bool:
        sides = sorted((self.a, self.b, self.c))
        return math.isclose(
            sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9
        )
