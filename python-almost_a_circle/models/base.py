#!/usr/bin/python3
"""Class Base"""

import json
import csv


class Base:
    """
    Base class
    Attributes:
        __nb_objects (int): Counter for automatically assigned IDs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("")
            else:
                fieldnames = list_objs[0].to_dictionary().keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Reads a CSV file and deserializes it into a list of objects."""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                list_objs = []
                for row in reader:
                    row = {key: int(value) for key, value in row.items()}
                    list_objs.append(cls.create(**row))
                return list_objs
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set based on the dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
