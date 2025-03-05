#!/usr/bin/python3
"""Test for Base, Rectangle, and Square"""

from base import Base
from rectangle import Rectangle
from square import Square

if __name__ == "__main__":
    # Test Rectangle CSV Serialization/Deserialization
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)
    print("Rectangles saved to file.")

    list_rectangles_output = Rectangle.load_from_file_csv()
    print("Rectangles loaded from file:")

    for rect in list_rectangles_output:
        print(rect)

    print("---")

    # Test Square CSV Serialization/Deserialization
    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file_csv(list_squares_input)
    print("Squares saved to file.")

    list_squares_output = Square.load_from_file_csv()
    print("Squares loaded from file:")

    for square in list_squares_output:
        print(square)

    print("OK")

