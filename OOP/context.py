# Вы работаете в компании, занимающейся разработкой программного
# обеспечения для архитектурных проектов.
# Вам необходимо разработать программу для расчёта площади различных
# геометрических фигур, таких как круги, прямоугольники и треугольники.
#
# Задача
# Создайте:
#
# класс Shape, который будет базовым классом для всех фигур и будет
# хранить пустой метод area, который наследники должны переопределить;
# класс Circle;
# класс Rectangle;
# класс Triangle.
# Классы Circle, Rectangle и Triangle наследуют от класса Shape и
# реализуют метод для вычисления площади фигуры.
#
# Дополнительно: изучите информацию о работе с абстрактными классами.
#
# На основе этой информации сделайте так, чтобы:
#
# Нельзя было создавать объекты класса Shape.
# Наследники класса Shape переопределяли его метод area, чтобы объекты этих классов можно было использовать.
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
circle_area = circle.area()  # Вычисление площади круга
print(round(circle_area, 2))

rectangle = Rectangle(4, 6)
rectangle_area = rectangle.area()  # Вычисление площади прямоугольника
print(rectangle_area)

triangle = Triangle(3, 8)
triangle_area = triangle.area()  # Вычисление площади треугольникаибку
print(triangle_area)
