from math import sin, cos, pi
from numbers import Number

from primitives import Matrix


def rotation_2d(rad: Number=None, deg: Number=None) -> Matrix:
    """
    Returns 2d rotation matrix for given angle in radians or degrees
    """
    angle = _radianize(rad, deg)
    return Matrix(rows=(
        (cos(angle), -sin(angle)),
        (sin(angle), cos(angle)),
    ))


def _radianize(rad: Number=None, deg: Number=None) -> Number:
    """
    Takes angle in radians or degrees, returns angle in radians
    """
    if rad:
        return rad
    elif deg:
        return deg * pi / 180
    else:
        raise ValueError('Either rad or deg must be set')
