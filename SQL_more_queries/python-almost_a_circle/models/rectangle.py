#!/usr/bin/python3
"""Class Rectangle that inherits from Base"""

from .base import Base


class Rectangle(Base):
    """
    Class Rectangle inheriting Base
    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        x (int): The x coordinate
        y (int): The y coordinate
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self.__validate_integer(value, "width")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        self.__validate_integer(value, "height")
        self.__height = value

    @property
    def x(self):
        """X coordinate getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X coordinate setter"""
        self.__validate_integer(value, "x")
        self.__x = value

    @property
    def y(self):
        """Y coordinate getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y coordinate setter"""
        self.__validate_integer(value, "y")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the rectangle using the `#` character."""
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Updates attributes."""
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def __validate_integer(self, value, name):
        """Validates that the input is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0 and name in ("x", "y"):
            raise ValueError(f"{name} must be >= 0")
        if value <= 0 and name in ("width", "height"):
            raise ValueError(f"{name} must be > 0")

