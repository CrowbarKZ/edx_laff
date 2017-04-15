from numbers import Number
from primitives import Vector


def axpy(a: Number, x: Vector, y: Vector) -> Vector:
    """
    Returns a sum of vector a and scaled vector b
    so called 'axpy' (a * x plus y) operation
    """
    return a * x + y


def linear_combination(a: Number, x: Vector, b: Number, y: Vector) -> Vector:
    """
    Returns a sum of scaled vectors x and y
    a * x + b * y
    """
    return a * x + b * y
