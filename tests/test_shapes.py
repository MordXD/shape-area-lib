import math
import pytest
from shape_area_lib.shapes import Circle, Triangle


def test_circle_area():
    assert math.isclose(Circle(2).area(), math.pi * 4)


def test_triangle_area_and_right():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6)
    assert t.is_right is True


def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 1, 3)
