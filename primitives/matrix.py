from numbers import Number
from primitives import Vector
from typing import Iterable


class Matrix:
    """
    Simple matrix class
    Stores components as tuple of tuples (for consistency)
    """
    def __init__(self, rows: Iterable[Iterable[Number]] = None,
                 cols: Iterable[Iterable[Number]] = None):
        """
        Expects either rows or cols to be set, not both
        if rows are set, cols will be ignored
        """
        if rows:
            self.components = tuple(tuple(row) for row in rows)
        elif cols:
            rows = zip(*cols)
            self.components = tuple(rows)
        else:
            raise ValueError('Either rows or cols must be set')

    def __repr__(self):
        result = 'Matrix: \n'
        for row in self.components:
            result += repr(row) + '\n'
        return result

    def __getitem__(self, key):
        return self.components[key]

    def __mul__(self, other: Vector):
        return Vector(Vector(row).dot(other) for row in self.components)

    def __rmul__(self, other: Vector):
        return self.__mul__(other)

    def __eq__(self, other: 'Matrix'):
        return self.components == other.components
