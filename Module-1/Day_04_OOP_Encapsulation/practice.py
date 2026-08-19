"""
Day 04 - OOP Practice & Coding Challenges
"""
import math

class Student:
    """Exercise 1: Student class with private grades attribute."""
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self._grades = []

    def add_grade(self, grade: float):
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")

    def get_average(self) -> float:
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    @property
    def grades(self):
        return list(self._grades)


class Rectangle:
    """Exercise 3: Rectangle with validated properties."""
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, val: float):
        if val <= 0:
            raise ValueError("Width must be positive")
        self._width = val

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, val: float):
        if val <= 0:
            raise ValueError("Height must be positive")
        self._height = val

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)


class Vector2D:
    """Challenge 9: Vector 2D with operator overloading."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


if __name__ == "__main__":
    s = Student("Bethlehem", "ST001")
    s.add_grade(95)
    s.add_grade(85)
    print(f"Student {s.name} Avg:", s.get_average())

    rect = Rectangle(5, 10)
    print("Rectangle Area:", rect.area())

    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    print("v1 + v2 =", v1 + v2)
    print("v1 magnitude =", v1.magnitude())
