# shape-area-lib

Библиотека для расчёта площадей фигур.

## Установка

```bash
pip install shape-area-lib
```

## Быстрый старт

```python
from shape_area_lib import Circle, Triangle

print(Circle(radius=2).area())
print(Triangle(a=3, b=4, c=5).area())
```

## Roadmap

- Круг и треугольник (MVP)
- Документация и тесты
- Расширяемость: новые фигуры