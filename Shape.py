from abc import ABC, abstractmethod
import math

# Class to initialize abstract base class of Shape
class Shape(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Method to return the shape name, area, and perimeter
    def __str__(self):
        return f"{self.name}, area: {self.area()}, perimeter: {self.perimeter()}"

# Concrete Shape Classes
# Class to initialize circle shape
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

# Method to return area of circle
    def area(self):
        return math.pi * self.radius ** 2

# Method to return perimeter of Circle
    def perimeter(self):
        return 2 * math.pi * self.radius

# Class to initialize square shape
class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

# Method to return area of Square
    def area(self):
        return self.side ** 2

# Method to return perimeter of Square
    def perimeter(self):
        return 4 * self.side

# Class to initialize Rectangle shape
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

# Method to return area of Rectangle
    def area(self):
        return self.length * self.width

# Method to return perimeter of Rectangle
    def perimeter(self):
        return 2 * (self.length + self.width)

# Class to initialize Triangle shape
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

# Method to return area of Triangle
    def area(self):
        return 0.5 * self.base * self.height

# Method to return perimeter of Triangle
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
