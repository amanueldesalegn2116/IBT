"""
Day 05 - OOP II Practice Exercises
"""
from abc import ABC, abstractmethod
import math

class Vehicle:
    """Exercise 1: Vehicle Base Class."""
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def describe(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def drive(self) -> str:
        return f"Driving {self.describe()} on the road."


class ElectricCar(Vehicle):
    """Subclass inheriting from Vehicle."""
    def __init__(self, make: str, model: str, year: int, battery_kwh: float):
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh

    def drive(self) -> str:
        return f"Driving electric {self.describe()} silently!"

    def recharge(self) -> str:
        return f"Recharging {self.battery_kwh} kWh battery..."


class Shape(ABC):
    """Exercise 2: Abstract Base Class for Shapes."""
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Notifier(ABC):
    """Exercise 3: Abstract Notifier for Polymorphism."""
    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        pass


class EmailNotifier(Notifier):
    def send(self, recipient: str, message: str) -> str:
        return f"Email sent to {recipient}: {message}"


class SMSNotifier(Notifier):
    def send(self, recipient: str, message: str) -> str:
        return f"SMS sent to {recipient}: {message}"


if __name__ == "__main__":
    ev = ElectricCar("Tesla", "Model 3", 2024, 75.0)
    print(ev.drive())
    print(ev.recharge())

    circle = Circle(5.0)
    print("Circle Area:", round(circle.area(), 2))

    notifiers = [EmailNotifier(), SMSNotifier()]
    for n in notifiers:
        print(n.send("user@example.com", "Your ETB account was credited."))
