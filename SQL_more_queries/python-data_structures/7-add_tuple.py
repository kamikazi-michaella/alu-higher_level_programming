#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements by padding with zeros
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Create a new tuple with the sum of the first and second elements
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
