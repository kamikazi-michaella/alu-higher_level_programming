#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Class Square inheriting Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.
        Args:
            size (int): Size of the square (width and height).
            x (int): X-coordinate position of the square.
            y (int): Y-coordinate position of the square.
            id (int): Unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size.
        Updates both width and height to maintain square dimensions.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.
        Format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.
        Keys: id, size, x, y
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }

    def update(self, *args, **kwargs):
        """
        Updates the square attributes.
        Args:
            *args: List of arguments:
                1st arg: id (int)
                2nd arg: size (int)
                3rd arg: x (int)
                4th arg: y (int)
            **kwargs: Key-value pairs to update attributes.
        """
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

